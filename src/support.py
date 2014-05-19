import sys, tty, termios
import os
import pyfiglet 

def getAkey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getAline(message):
    print message
    return sys.stdin.readline().strip()

def getKeyOrExit(muffleMessage=False):
    if not muffleMessage:
        print "\nPress any key to continue, but [ESC] to quit"
    ch = getAkey()
    if ch == '\033':
        sys.exit(0)
    return ch

def splashMessage(message, muffleClear=False):
    if not muffleClear:
        os.system("clear")
    pyfiglet.print_figlet(message)
    print ""
