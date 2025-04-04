from .stein import (
    repr, list, open, stduot, stdout,
    fake_exit, fake_os_exit
)

# Export under kql namespace
exit = fake_exit
_exit = fake_os_exit
