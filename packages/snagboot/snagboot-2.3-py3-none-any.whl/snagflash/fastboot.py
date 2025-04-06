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

from snagrecover.protocols import fastboot as fb
from snagrecover.utils import usb_addr_to_path, get_usb, cli_error, access_error, prettify_usb_addr
import sys
import logging
logger = logging.getLogger("snagflash")

from snagflash.fastboot_uboot import SnagflashFastbootUboot
import warnings

def fb_interactive_deprecation():
	warnings.warn("Using interactive mode with the '-P fastboot' option is deprecated and will be removed in a future release! Please use the '-P fastboot-uboot' option instead!",
		FutureWarning,
		stacklevel=1)

def fastboot_ready_check(dev):
	try:
		fb.Fastboot(dev)
	except Exception:
		logger.warning(f"Failed to init Fastboot object from USB device at {prettify_usb_addr((dev.bus,dev.port_numbers))}")
		return False

	return True

def fastboot(args):
	if (args.port is None):
		logger.info("Error: Missing command line argument --port vid:pid|bus-port1.port2.[...]")
		logger.error("Error: Missing command line argument --port vid:pid|bus-port1.port2.[...]")
		sys.exit(-1)

	usb_addr = usb_addr_to_path(args.port)
	if usb_addr is None:
		access_error("USB Fastboot", args.port)

	dev = get_usb(usb_addr, ready_check=fastboot_ready_check)
	dev.default_timeout = int(args.timeout)

	fast = fb.Fastboot(dev, timeout = dev.default_timeout)

	# this is mostly there to dodge a linter error
	logger.debug(f"Fastboot object: eps {fast.ep_in} {fast.ep_out}")
	logger.info(args.fastboot_cmd)

	if hasattr(args, "factory"):
		session = SnagflashFastbootUboot(fast)
		session.run(args.interactive_cmds)
		return

	if args.protocol == "fastboot-uboot" and args.fastboot_cmd != []:
		cli_error("The '-f' option is not available with the fastboot_uboot protocol!")

	for cmd in args.fastboot_cmd:
		cmd = cmd.split(":", 1)
		cmd, cmd_args = cmd[0], cmd[1:]
		cmd = cmd.replace("-", "_")
		logger.info(f"Sending command {cmd} with args {cmd_args}")
		if cmd == "continue":
			cmd = "fbcontinue"
		try:
			getattr(fast, cmd)(*cmd_args)
		except Exception as e:
			logger.error(f"{e}")
			sys.exit(-1)

	logger.info("Done")

	session = None

	if args.interactive_cmdfile is not None:
		if args.protocol == "fastboot":
			fb_interactive_deprecation()

		session = SnagflashFastbootUboot(fast)
		logger.info(f"running commands from file {args.interactive_cmdfile}")
		with open(args.interactive_cmdfile, "r") as file:
			cmds = file.read(-1).splitlines()

		session.run(cmds)

	if args.interactive:
		if args.protocol == "fastboot":
			fb_interactive_deprecation()

		if session is None:
			session = SnagflashFastbootUboot(fast)

		session.start()

