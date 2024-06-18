#!/usr/bin/python3
"""
Log parsing script that reads from standard input and computes metrics.
"""

import sys

def print_stats(stats, filesize):
    """Prints the statistics of logs processed."""
    print("File size: {}".format(filesize))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

if __name__ == '__main__':
    filesize = 0
    count = 0
    stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 2:
                status = parts[-2]
                size = parts[-1]

                if status in stats:
                    stats[status] += 1

                try:
                    filesize += int(size)
                except ValueError:
                    pass

            count += 1
            if count % 10 == 0:
                print_stats(stats, filesize)

    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
    else:
        print_stats(stats, filesize)
