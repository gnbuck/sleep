import os
import sys
import time
import argparse

# Create parser and its driver
props = ["sec", "s", "min", "m", "hrs", "H"]
parser = argparse.ArgumentParser()
parser.add_argument("--sec", type=int)
parser.add_argument("-s", type=int)
parser.add_argument("--min", type=int)
parser.add_argument("-m", type=int)
parser.add_argument("--hrs", type=int)
parser.add_argument("-H", type=int)
args = parser.parse_args()

# Register the timer in a variable
def get_timer():
    for prop in props:
        attr = (getattr(args, prop), prop)
        if attr[0] is not None:
            return attr
    return (1600, "sec")
t = get_timer()

# Wait before sleep the system
def wait(t):
    print(f"Waiting for {t} seconds")
    time.sleep(t)
    os.system("shutdown -h")


# Convert seconds
if t[1] in ("sec", "s"):
    t = t[0]

# Convert minutes into seconds
elif t[1] in ("min", "m"):
    t = t[0]*60

# Convert hours into seconds
elif t[1] in ("hrs", "H"):
    t = t[0]*3600

# print(t)
try:
    wait(t)
except KeyboardInterrupt:
    print("\nOperation aborted")
