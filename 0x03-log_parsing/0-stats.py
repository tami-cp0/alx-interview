#!/usr/bin/python3
"""
Log parser
"""
import signal
import sys
import re
from typing import Tuple

if __name__ == '__main__':

    stats = {}

    def calc_stats(match: Tuple) -> None:
        """
        Processes and stores the stats
        Returns:
            None
        """
        global stats

        stats['size'] = stats.get('size', 0) + int(match[4])
        stats[match[3]] = stats.get(match[3], 0) + 1

    def display() -> None:
        """
        Displays the processed stats
        Returns:
            None
        """
        global stats
        print(f"File size: {stats.get('size')}")

        for stat in sorted(stats.keys()):
            if stat == "size":
                continue
            print(f"{stat}: {stats.get(stat)}")

    def handler(signum, frame):
        """
        Handler for Ctrl + C SIGINT
        Returns:
            None
        """
        display()

    # listens to Ctrl + C then displays the stats
    signal.signal(signal.SIGINT, handler)

    # pattern to match for precessing
    half = r'(\d+\.\d+\.\d+\.\d+) - (\[\d+-\d+-\d+ \d+:\d+:\d+\.\d+\])'

    half2 = r' ("GET /projects/260 HTTP/1.1") (\d{3}) (\d{1,4})'

    input_format = half + half2

    # listens to the output from another script
    count = 1
    for line in sys.stdin:
        match = re.search(input_format, line)
        if match:
            # processes and stores the stats
            calc_stats(match.groups())
        else:
            pass

        if count % 10 == 0:
            # displays the stats if 10 lines has been processed
            display()
        count += 1

    display()
