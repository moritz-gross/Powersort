#!/usr/bin/env python3
import re
import matplotlib.pyplot as plt
import sys

def parse_log(content):

    blocks = re.split(r'File:\s+', content)
    results = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        timsort_match = re.search(r"Timsort timings:\s*Average time per run \(microseconds\):\s*([\d\.]+)", block)
        powersort_match = re.search(r"Powersort timings:\s*Average time per run \(microseconds\):\s*([\d\.]+)", block)

        if timsort_match and powersort_match:
            results.append(float(powersort_match.group(1)) / float(timsort_match.group(1)))
    return results

def main():

    if len(sys.argv) < 2:
        print("Usage: python evaluate_logs.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    try:
        with open(log_file, 'r') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading log file: {e}")
        sys.exit(1)


    results = parse_log(content)
    if not results:
        print("No valid log blocks found.")
        return

    # create histogram
    plt.figure()
    plt.hist(results)
    plt.xlabel("Change from Timsort to Powersort")
    plt.show()

if __name__ == '__main__':
    main()