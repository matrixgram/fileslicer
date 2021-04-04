#!/usr/bin/env python3
import pandas
import sys
import argparse
import csv

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument(dest='input_file', help='')
    # args = parser.parse_args()
    #print(args)
    input_file, column_number, output_file, step = (
        sys.argv[1],
        int(sys.argv[2]),
        sys.argv[3],
        int(sys.argv[4]),
    )

    excel = pandas.read_excel(input_file)
    new_excel = excel.iloc[:, column_number]
    s = [i for i in range(0, len(new_excel), step)]
    with open(output_file, "w") as f:
        w = csv.writer(f)
        w.writerow(s)

    # new_excel.to_csv(output_file)
