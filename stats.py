#!/usr/bin/env python3
import sys

# Option variables
column = None
filename = None

def usage(msg=None):
    if msg:
        print(msg, "\n")
    print("Usage: stat.py [-c <positiveinteger>] <filename>")
    sys.exit(1)

# -------------------------
# Command line parsing
# -------------------------
args = sys.argv[:]   # copy
args.pop(0)          # remove program name

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
                # Read only the specified column
                try:
                    value = float(parts[column - 1])
                    numbers.append(value)
                except (IndexError, ValueError):
                    # Ignore malformed lines or non-numeric values
                    pass
            else:
                # Read all numeric values from all columns
                for p in parts:
                    try:
                        numbers.append(float(p))
                    except ValueError:
                        pass

except FileNotFoundError:
    usage(f"File not found: {filename}")


