#!/usr/bin/env python3
import sys

# Option variables
column = None
do_average = False
do_count = False
do_trimmed = False
do_median = False
filename = None

def usage(msg=None):
    if msg:
        print(msg, "\n")
    print("Usage: stat.py [-c <positiveinteger>] [-a] [-m] <filename>")
    sys.exit(1)

def average(values):
    if not values:
        return None
    return sum(values) / len(values)

def median(values):
    if not values:
        return None
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    else:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2

def obs(values):
    return len(values)

def trimmedmean(values):
    # Partner will implement this
    pass

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

    elif arg == "-m":
        do_median = True

    elif filename is None:
        filename = arg

    elif arg == "-n":
    	do_count = True

    elif arg == "-t":
    	do_trimmed = True
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
# Options: -a and -m
# -------------------------
if do_average:
    avg = average(numbers)
    if avg is not None:
        print(avg)

if do_median:
    med = median(numbers)
    if med is not None:
        print(med)

if do_count:
    print(obs(numbers))

if do_trimmed:
    print(trimmedmean(numbers))
