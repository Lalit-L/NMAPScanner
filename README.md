# NMAPScanner
A simple NMAP scanner developed in Python

---------------------------------------------------------------------------------------

Edit 1: Added a basic input system that takes in the address that should be scanned

Thoughts: Overall pretty simple, no problems at all

---------------------------------------------------------------------------------------

Edit 2: Added a SYN ACK scan. This performs a SYN ACK scan on the address provided by the user. It also checks for open ports (between ports 1 and 10000), and checks whether or not the address given is up or down. It also provides the protocols being scanned

Thoughts: It was pretty interesting to learn about the different types of scans that exist, as my classes never really went over things like this. It took a while to learn how to go about coding it, but it was pretty fun!

---------------------------------------------------------------------------------------

Edit 3: Added a UDP scan as well. This will scan for open UDP Ports on the address entered, which the user can use if they are opting for a faster scan. Due to there not being acknowledgement of a receipt, it is a less reliable scan method, but it is also a little more stealthy compared to the SYN ACK scan I implemented before

Thoughts: It was fun learning about a different scan method, considering I thought there would be only so many ways to scan for ports and openings on an address. The speed of the UDP scan is quite nice, but I can see how the reliability is lacking. The stealth aspect of the scan is cool though, as some firewalls and systems might not log its activity as much. Overall it wasn't difficult to implement and was enjoyable

---------------------------------------------------------------------------------------

Edit 4: FINAL EDIT. Added a comprehensive scan and a check to make sure that a correct option is chosen. Also added user input for the ports to be scanned using a range. Cleaned up other comments while adding some to the Comprehensive scan portion

Thoughts: FINAL THOUGHTS. This was fun! It felt really gratifying to finish a project like this, because I had never really done something like this. I did the port scanner, which was a nice buildup to this because of how it functions with each scan, but this was still super informative. The Comprehensive Scan does take a while to fully scan, but it does make sense given the amount it has to go through. Overall, this was a very rewarding project.
