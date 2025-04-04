import sys, os
from .stein import (
    repr, list, open, stduot, stdout,
    fake_exit, fake_os_exit
)

# Override sys + os exits
sys.exit = fake_exit
os._exit = fake_os_exit

# Also expose as kql.exit and kql._exit
exit = fake_exit
_exit = fake_os_exit
