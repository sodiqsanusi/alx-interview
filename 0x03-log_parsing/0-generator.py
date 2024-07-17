#!/usr/bin/python3

import random
# Importing the 'random' module to generate random numbers.

import sys
# Importing the 'sys' module to access system-specific parameters and functions.

from time import sleep
# Importing the 'sleep' function from the 'time' module to add a delay in the loop.

import datetime
# Importing the 'datetime' module to work with date and time.

for i in range(10000):
    # Starting a 'for' loop that will run 10000 times.

    sleep(random.random())
    # Adding a random delay using 'sleep' function to simulate random log generation.

    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    # Writing a log line to the standard output (stdout).
    # The log line is generated with random IP address, date, status code, and file size.
    # The 'datetime.datetime.now()' function is used to get the current date and time.
    # The 'random.choice()' function selects a random status code from the given list.
    # The 'random.randint()' function generates a random file size between 1 and 1024 bytes.
