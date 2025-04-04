import sys, os
from .stein import repr, list, open, stduot, stdout, fake_exit, fake_os_exit

sys.exit = fake_exit
os._exit = fake_os_exit

exit = fake_exit
_exit = fake_os_exit
