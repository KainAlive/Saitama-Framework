import socket

target = raw_input("Please enter URL: ")
targetIP = socket.gethostbyname(target)
print "IP of " + target + ": " + targetIP
