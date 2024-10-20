#!/usr/bin/env python

import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface use --help for info")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address use --help for info")
    return options

def mac_changer(interface, new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

opt = get_args()
mac_changer(opt.interface, opt.new_mac)