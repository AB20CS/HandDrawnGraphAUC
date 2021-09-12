# Purpose: Calculates the area under the blood pressure curves
#
# Anindro Bhattacharya
#
# Preconditions:
#  - size of each square in grid is 1000 pixels
#  - 1 square = 10 mm Hg * 5 min = 50 mm Hg*min
#     ==> Unit for final area: mm Hg * min
#  - length of 1 square = 30 pixels
#

####### IMPORTS #######

import os
import csv

####### CONSTANTS #######

CSV_OUT_FILENAME = 'area_log.csv' # CSV file name of output log

PIXELS_PER_SQUARE = 1000
AREA_PER_SQUARE = 50
AREA_PER_PIXEL = AREA_PER_SQUARE / PIXELS_PER_SQUARE

MINUTES_PER_UNIT_LENGTH = 5
PIXELS_PER_LENGTH = 30

HEIGHT_CUT_OFF = 50

#########################

out = open(CSV_OUT_FILENAME, 'w', newline='')
csv_out = csv.writer(out)
csv_out.writerow(['file_name', 'area'])

for file in os.listdir():
    if (file.endswith('.csv') and file != CSV_OUT_FILENAME):
        with open(file, newline='') as csv_file:
            csv_file.readline() # skips first row in CSV (contains column headers)
            num_pixels = 0
            time_pixels = 0
            for row in csv_file:
                if float(row.split(',')[6].strip()) == 0:
                    num_pixels += float(row.split(',')[1].strip()) # 2nd column in CSV is area
                else:
                    time_pixels += float(row.split(',')[6].strip()) # 7th column in CSV is area

            area_cut_off = (time_pixels / PIXELS_PER_LENGTH) * MINUTES_PER_UNIT_LENGTH * HEIGHT_CUT_OFF
            area = (num_pixels * AREA_PER_PIXEL) + area_cut_off # FINAL AREA VALUE

            csv_out.writerow([csv_file.name, area])
            print("File Name:", csv_file.name[0:-4], "\tArea:", area, "\n")

out.close()