#!/usr/bin/env python3
"""This is main file."""
import csv
import sys

try:
    import pandas
except ImportError as error:
    print(error)

if sys.version_info.major == 3:
    print("[!] Required python 3.x.x")
    sys.exit(-1)

if __name__ == "__main__":
    input_file, column_number, output_file, step = (
        sys.argv[1],
        int(sys.argv[2]),
        sys.argv[3],
        int(sys.argv[4]),
    )

    excel = pandas.read_excel(input_file)
    new_excel = excel.iloc[:, column_number]
    s = list(range(0, len(new_excel), step))
    with open(output_file, "w") as f:
        w = csv.writer(f)
        w.writerow(s)
