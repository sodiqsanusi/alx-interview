#!/usr/bin/python3
"""
Log parsing
"""


import sys
# Importing the 'sys' module to access system-specific parameters and functions.

if __name__ == '__main__':
    # The script starts here.

    filesize, count = 0, 0
    # Initializing two variables 'filesize' and 'count' to 0.

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    # Creating a list 'codes' containing status codes.

    stats = {k: 0 for k in codes}
    # Creating a dictionary 'stats' with status codes as keys and initial count as 0.

    def print_stats(stats: dict, file_size: int) -> None:
        # Defining a function 'print_stats' that takes a dictionary 'stats' and an integer 'file_size' as arguments.
        # The function does not return anything (None).

        print("File size: {:d}".format(filesize))
        # Printing the total file size.

        for k, v in sorted(stats.items()):
            # Looping through the items in the 'stats' dictionary.

            if v:
                # Checking if the count (v) is not 0.

                print("{}: {}".format(k, v))
                # Printing the status code (k) and its count (v).

    try:
        # Starting a try-except block to handle potential exceptions.

        for line in sys.stdin:
            # Looping through each line from the standard input (stdin).

            count += 1
            # Incrementing the 'count' variable.

            data = line.split()
            # Splitting the line into a list 'data' using whitespace as the separator.

            try:
                status_code = data[-2]
                # Accessing the second-to-last element (status code) from the 'data' list.

                if status_code in stats:
                    # Checking if the status code is in the 'stats' dictionary.

                    stats[status_code] += 1
                    # Incrementing the count of the corresponding status code in the 'stats' dictionary.

            except BaseException:
                # Handling any potential exceptions during the status code processing.

                pass
                # Continuing to the next iteration without raising an error.

            try:
                filesize += int(data[-1])
                # Accessing the last element (file size) from the 'data' list and adding it to the 'filesize' variable.

            except BaseException:
                # Handling any potential exceptions during the file size processing.

                pass
                # Continuing to the next iteration without raising an error.

            if count % 10 == 0:
                # Checking if the 'count' is a multiple of 10.

                print_stats(stats, filesize)
                # Printing the statistics using the 'print_stats' function.

        print_stats(stats, filesize)
        # Printing the final statistics after the loop ends.

    except KeyboardInterrupt:
        # Handling the KeyboardInterrupt exception (CTRL + C).

        print_stats(stats, filesize)
        # Printing the current statistics before raising the exception.
        raise
        # Raising the KeyboardInterrupt exception to exit the script gracefully.
