#!/bin/sh
# This file is part of Snagboot
# Copyright (C) 2023 Bootlin
#
# Written by Romain Gantois <romain.gantois@bootlin.com> in 2023.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# This script will do the following things to setup
# an environment for recovering an AM335x soc via USB:
# 1. Create a new network namespace called $NETNS_NAME
# 2. Run a subprocess that will trigger every time
#    a new ROM code or SPL USB ethernet gadget with a
#    certain PID:VID pair is registered.
#    It will:
#    2.1. Move the network interface to $NETNS_NAME
#    2.2. Add a static IP address to the interface,
#        so that the board can reach the recovery tool
#    2.3. Route an arbitrary client ip to the interface,
#        so that the recovery tool can reach the board
#    3.4. Route 255.255.255.255 to the interface, so
#         that the recovery tool can reach the board
#         using a broadcast, when the board does not
#         know its own IP yet

print_usage () {
	echo "am335x_usb_setup.sh: Create network namespace and udev rules necessary for AM335x USB recovery"
	echo "-r vid:pid ROM Ethernet USB gadget address"
	echo "-s vid:pid SPL Ethernet USB gadget address"
	echo "-n netns_name Name of the network namespace to be created, "
	echo "              this is 'snagbootnet' by default, make sure to "
	echo "              pass this to the recovery tool if you do not "
	echo "              use the default value. You can use the --netns "
	echo "              flag of the recovery tool for this."
	echo "-c Delete the network namespace and udev rules "
	echo "   previously created by this script"
	echo "-h Show this help"
	echo ""
}

fail_on_error () {
	echo "ERROR: $1" >> /dev/stderr
	echo "Operation failed" >> /dev/stderr
	exit 1
}

DEFAULT_ROMUSB="0451:6141"
DEFAULT_SPLUSB="0451:d022"
NETNS_NAME="snagbootnet"
SUDOER="$SUDO_USER"
SUDOER_BASHRC=$(eval echo "~$SUDOER")"/.bashrc"
poller_id=""

#delete the new network namespace and udev rules
cleanup () {
	if [ ! "$poller_id" = "" ]; then
		kill -KILL $poller_id
	fi
	echo "Deleting namespace $NETNS_NAME..."
	ip netns delete "$NETNS_NAME"
}

config_interface () {
	#This sets up the necessary
	#network config inside the recovery namespace

	SERVER_IP="192.168.0.100"
	CLIENT_IP="192.168.0.101"
	IF_NAME=$1

	#move interface to recovery network namespace
	ip link set "$IF_NAME" down
	ip link set "$IF_NAME" netns "$NETNS_NAME"
	ip netns exec "$NETNS_NAME" ip link set "$IF_NAME" up

	#assign static ip to interface, setup ip route
	ip netns exec "$NETNS_NAME" ip addr add dev "$IF_NAME" "$SERVER_IP"
	ip netns exec "$NETNS_NAME" ip route add "255.255.255.255" dev "$IF_NAME"
	ip netns exec "$NETNS_NAME" ip route add "$CLIENT_IP" dev "$IF_NAME"
}


while getopts "r:s:n:ch:" opt; do
  case $opt in
    r) ROMUSB=$OPTARG;;
    s) SPLUSB=$OPTARG;;
    n) NETNS_NAME=$OPTARG;;
    c) cleanup echo "Done"
      exit 0
      ;;
    h) print_usage
      exit 0
      ;;
    :) echo "Option -$OPTARG requires an argument." >&2
      print_usage
      exit 1
      ;;
    *) echo "Invalid option: -$OPTARG" >&2
      print_usage
      exit 1
      ;;
  esac
done

#check user
if [ ! "$(whoami)" = "root" ]; then
	fail_on_error "This script should be run as root!"
fi

#check SUDOER
if [ -z "${SUDOER}" ]; then
	fail_on_error "User name could not be determined on this system"
fi

id "$SUDOER" >/dev/null 2>&1; code=$?
if [ $code -eq 1 ] || [ "$SUDOER" = "root" ]; then
	# SUDO_USER may not work on all systems ...
	PARENT_ID=$(ps -o ppid= -p $$)
	GRANDPARENT_ID=$(ps -o ppid= -p $PARENT_ID)
	SUDOER=$(ps -o user= -p $GRANDPARENT_ID)
	id "$SUDOER" >/dev/null 2>&1; code=$?
	if [ $code -eq 1 ] || [ "$SUDOER" = "root" ]; then
		fail_on_error "Failed to find the username of sudo caller: found $SUDOER"
	fi
fi

if [ ! -f "$SUDOER_BASHRC" ]; then
	fail_on_error "Could not find a valid .bashrc file for user $SUDOER"
fi

#check usb args
USB_REGEX="^[[:xdigit:]]{4}:[[:xdigit:]]{4}$"
if ! echo "$ROMUSB" | grep -qE "$USB_REGEX"; then
	echo "Missing -r flag or invalid format for ROM USB gadget address vid:pid, using default value"
	ROMUSB=$DEFAULT_ROMUSB
fi
if ! echo "$SPLUSB" | grep -qE "$USB_REGEX"; then
	echo "Missing -s flag or invalid format for SPL USB gadget address vid:pid, using default value"
	SPLUSB=$DEFAULT_SPLUSB
fi

#strip leading zeroes and replace colons with slashes
ROMUSB=$(printf "%s/" "$ROMUSB" | sed -e 's/^0*//' -e 's/:0*/:/' -e 's/:/\//')
SPLUSB=$(printf "%s/" "$SPLUSB" | sed -e 's/^0*//' -e 's/:0*/:/' -e 's/:/\//')

echo "Starting polling subprocess..."

poll_interface () {
	UEVENTS=$(grep -s -l "DEVTYPE=usb_interface" /sys/class/net/*/device/uevent)
	ROMNETDEV=$(grep -s -l "PRODUCT=$ROMUSB" $UEVENTS | cut -d '/' -f 5)
	SPLNETDEV=$(grep -s -l "PRODUCT=$SPLUSB" $UEVENTS | cut -d '/' -f 5)
	if [ -n "$ROMNETDEV" ]; then
		config_interface  "$ROMNETDEV" >/dev/null 2>&1
	elif [ -n "$SPLNETDEV" ]; then
		config_interface  "$SPLNETDEV" >/dev/null 2>&1
	fi
}

{
while true; do
	poll_interface
	sleep 0.1
done
} & poller_id=$!

#network namespace
if test -f "/run/netns/$NETNS_NAME"; then
	fail_on_error "The network namespace $NETNS_NAME already exists! Cancelling operation..."
fi
echo "Creating network namespace $NETNS_NAME..."
ip netns add "$NETNS_NAME" || fail_on_error "Could not create namespace $NETNS_NAME"

#iptables rules
ip netns exec "$NETNS_NAME" iptables -t nat -A PREROUTING -p udp --dport 67 -j DNAT --to-destination :9067
ip netns exec "$NETNS_NAME" iptables -t nat -A PREROUTING -p udp --dport 69 -j DNAT --to-destination :9069
ip netns exec "$NETNS_NAME" iptables -t nat -A POSTROUTING -p udp --sport 9067 -j MASQUERADE --to-ports 67
ip netns exec "$NETNS_NAME" iptables -t nat -A POSTROUTING -p udp --sport 9069 -j MASQUERADE --to-ports 69

#start new shell
printf "Logging user %s into new shell\n" "$SUDOER"
echo "===== $NETNS_NAME ====="
echo "You can now setup the board and run the recovery tool."
echo "Please type 'exit' to delete the namespace, stop the polling process and leave the shell when you are done."

echo "cd $(pwd); exec </dev/tty" | SUDO_PS1='(am335_recovery) \u@\h:\w \$' ip netns exec "$NETNS_NAME" sudo -i -u "$SUDOER" bash -i

#leave shell and cleanup
cleanup
echo "Done"
exit

