import nmap

scanner = nmap.PortScanner()

print("Hello! This is a test version of an NMAP Scanner in Python!")
print("-" * 65)

address = input("Please enter the address you wish to scan: ")
print("The address you've entered is: " + address)
