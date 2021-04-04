#!/usr/bin/env python3
import pandas
import sys

if __name__ == "__main__":
    column = int(sys.argv[2])
    excel = pandas.read_excel(sys.argv[1])
    new_excel = excel.iloc[:, column]
    new_excel.to_csv(sys.argv[3])
f
