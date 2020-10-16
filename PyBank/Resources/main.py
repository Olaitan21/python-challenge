
import os
import csv

with open(pybank_path, newline-'') as csvfile:
    csvreader = csv.reader(csvfile, delimiter-',')

total_month = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease =["",0000000000000000000000000000]
total_net = 0

csv_header = next(csvreader)


