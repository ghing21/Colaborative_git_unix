#!/usr/bin/env python3
import sys

# Option variables
column = None
do_average = False
filename = None

def usage(msg=None):
    if msg:
        print(msg, "\n")
    print("Usage: stat.py [-c <positiveinteger>] [-a] <filename>")
    sys.exit(1)

def average(values):
    if not values:
        return None
    return sum(values) / len(values)

# -------------------------
# Command line parsing
# -------------------------
args = sys.argv[:]
args.pop(0)

while args:
    arg = args.pop(0)

    if arg == "-c":
        if not args:
            usage("Missing number after -c")
        try:
            column = int(args.pop(0))
            if column < 1:
                raise ValueError
        except ValueError:
            usage("Column number must be a positive integer")

    elif arg == "-a":
        do_average = True

    elif filename is None:
        filename = arg

    else:
        usage("Too many arguments or unknown option")

if filename is None:
    usage("You must specify a filename")

# -------------------------
# Reading the file
# -------------------------
numbers = []

try:
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("\t")

            if column is not None:
                try:
                    value = float(parts[column - 1])
                    numbers.append(value)
                except (IndexError, ValueError):
                    pass
            else:
                for p in parts:
                    try:
                        numbers.append(float(p))
                    except ValueError:
                        pass

except FileNotFoundError:
    usage(f"File not found: {filename}")

# -------------------------
# Option: -a (print average)
# -------------------------
if do_average:
    avg = average(numbers)
    if avg is not None:
        print(avg)
