#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Hello! This is a test version of an NMAP Scanner in Python!")
print("-" * 65)

# Collects the IP Address the user wants to scan
address = input("Please enter the address you wish to scan: ")
print("The address you've entered is: " + address + "\n")

print("A SYN ACK scan will be performed on the address given\n")

# Scans the version of NMAP
print("NMAP Version: ", scanner.nmap_version())

# Scans from ports 1 to 10000 on the given address, also verboses the output and performs a SYN ACK scan
scanner.scan(address, '1-10000', '-v -sS')

# Prints the info gained from the previous line
print(scanner.scaninfo())

# Prints whether or not the Address given is up or down
print("IP Status: ", scanner[address].state())

# Prints the protocol that is being scanned
print(scanner[address].all_protocols())

# Prints the open ports
print("Open ports: ", scanner[address]['tcp'].keys())
