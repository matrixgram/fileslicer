#!/usr/bin/env python3
import pandas
import sys

if __name__ == "__main__":
    input_file, column_number, output_file = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    excel = pandas.read_excel(input_file)
    new_excel = excel.iloc[:, column_number]
    new_excel.to_csv(output_file)
