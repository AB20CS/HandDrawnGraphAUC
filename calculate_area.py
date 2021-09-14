# This program calculates the area under the curve of a graph, given the following pre-conditions:
# - Using ImageJ, the area and length have been measured (according to specifications in README.md)
# - The output CSV files (containing Area and Length) must be saved in the same directory as calculate_are.py

####### IMPORTS #######

import os
import csv

####### INITIALIZE CONSTANTS #######

CSV_OUT_FILENAME = input("Enter the name of the output CSV file: ") + '.csv' # stores name of output CSV file (where AUC will be stored)

PIXELS_PER_SQUARE = input("Pixels per unit square: ")
AREA_PER_SQUARE = input("Area per unit square: ")
AREA_PER_PIXEL = AREA_PER_SQUARE / PIXELS_PER_SQUARE

VALUE_PER_UNIT_LENGTH = input("Value represented by each unit length: ")
PIXELS_PER_LENGTH = input("Number of pixels per unit length: ")

HEIGHT_CUT_OFF = input("Starting value on the y-axis: ")

#########################

out = open(CSV_OUT_FILENAME, 'w', newline='')
csv_out = csv.writer(out)
csv_out.writerow(['file_name', 'area'])

for file in os.listdir():
    if (file.endswith('.csv') and file != CSV_OUT_FILENAME):
        with open(file, newline='') as csv_file:
            csv_file.readline() # skips first row in CSV (contains column headers)
            num_pixels = 0
            length_pixels = 0
            for row in csv_file:
                if float(row.split(',')[6].strip()) == 0:
                    num_pixels += float(row.split(',')[1].strip()) # 2nd column in CSV is area
                else:
                    length_pixels += float(row.split(',')[6].strip()) # 7th column in CSV is area

            area_cut_off = (length_pixels / PIXELS_PER_LENGTH) * VALUE_PER_UNIT_LENGTH * HEIGHT_CUT_OFF
            area = (num_pixels * AREA_PER_PIXEL) + area_cut_off # FINAL AREA VALUE

            csv_out.writerow([csv_file.name, area])
            print("File Name:", csv_file.name[0:-4], "\tArea:", area, "\n")

out.close()
