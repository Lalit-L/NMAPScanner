#!/usr/bin/python3

import nmap
import pyfiglet

scanner = nmap.PortScanner()

banner = pyfiglet.figlet_format("NMAP SCANNER", font = "vortron_")
print(banner)

print("Hello! This is a test version of an NMAP Scanner in Python!")
print("-" * 65)

# Collects the IP Address the user wants to scan
address = input("Please enter the address you wish to scan: ")
print("The address you've entered is: " + address + "\n")


choice = input("Please enter the number of the type of scan you would like to run on the address: \n" +
		" 1) UDP Scan\n 2) SYN ACK Scan\n")

if choice == '1':
	print("\nA UDP scan will be performed on the address given\n")
	print("(Note that this may take some time)\n")

	# Scans the version of NMAP
	print("NMAP Version: ", scanner.nmap_version())

	# Scans from ports 1 to 10000 on the given address, also scans for UDP ports
	scanner.scan(address, '1-10000', '-v -sU')

	# Prints the info gained from the previous line
	print(scanner.scaninfo())

	# Prints whether or not the Address given is up or down
	print("IP Status: ", scanner[address].state())

	# Prints the protocol that is being scanned
	print(scanner[address].all_protocols())

	# Prints the open UDP ports
	print("Open ports: ", scanner[address]['udp'].keys())
elif choice == '2':
	print("\nA SYN ACK scan will be performed on the address given\n")
	print("(Note that this may take some time)\n")

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

	# Prints the open TCP ports
	print("Open ports: ", scanner[address]['tcp'].keys())
