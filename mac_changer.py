#!/usr/bin/env python

import subprocess
import optparse
import re

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

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read mac address")

opt = get_args()
current_mac = get_current_mac(opt.interface)
print("Current Mac "+ str(current_mac))
mac_changer(opt.interface, opt.new_mac)
current_mac = get_current_mac(opt.interface)
if current_mac == opt.new_mac:
    print("[+] MAC address was successfully changed to "+ opt.new_mac)
else:
    print("[-] MAC address did not get changed")
