import socket
import subprocess
import sys
from datetime import datetime

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

target = raw_input(bcolors.UNDERLINE + bcolors.OKBLUE +  "Enter Target URL or IP > " + bcolors.ENDC)
targetIP = socket.gethostbyname(target)

subprocess.call('clear', shell=True)



print "-" * 60
print "Started scanning " + target+"("+targetIP+")"
print "-" * 60

print ""
print ""
print
print (bcolors.BOLD + bcolors.OKGREEN + "#  888  /             ,e,               ,d88~~\                            " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  888 /      /~~~8e      888-~88e      8888     e88~~\   /~~~8e  888-~88e " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  888/\          88b 888 888  888 ____ `Y88b   d888          88b 888  888 " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  888  \    e88~-888 888 888  888       `Y88b, 8888     e88~-888 888  888 " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  888   \  C888  888 888 888  888         8888 Y888    C888  888 888  888 " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  888    \    8_-888 888 888  888      \__88P'   88__/   88_-888 888  888 " + bcolors.ENDC)
print (bcolors.BOLD + bcolors.OKGREEN + "#  By KainAlive                                                         V.01  " + bcolors.ENDC)
print ("")
print ("")
print ("")

tstart = datetime.now()

try:
    for port in range(1, 45000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, port))
        if res == 0:
            print (bcolors.OKGREEN +  "Port open: " + str(port) + bcolors.ENDC)
        sock.close()

except Exception:
    print (bcolors.FAIL + "Ups...There was an error!" + bcolors.ENDC)
    sys.exit()
except KeyboardInterrupt:
    tendbyu = datetime.now()
    tdiffbyU = tendbyu - tstart
    print (bcolors.FAIL + "Stoped scan after " + str(tdiffbyU)+ bcolors.ENDC)
    sys.exit()
except socket.gaierror:
    tendbysock = datetime.now()
    tdiffbysock = tendbysock - tstart
    print (bcolors.FAIL + "Could not resolve target! Stopped scan after " + str(tdiffbysock) + bcolors.ENDC)
    sys.exit()
except socket.error:
    tendbytar = datetime.now()
    tdiffbytar = tendbytar - tstart
    print (bcolors.FAIL + "Could not connect  target! Stopped scan after " + str(tdiffbytar) + bcolors.ENDC)
    sys.exit()

tend = datetime.now()
tdiff = tend - tstart

print (bcolors.WARNING +  "Scan done in " + str(tdiff)  + bcolors.ENDC)
