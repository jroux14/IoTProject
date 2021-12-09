import sys
import csv

infile = open(sys.argv[1])
reader = csv.reader(infile)
headings = []
rows = []

maxTemp = 0
minTemp = 99
averageTemp = 0

headings = reader.next()

for line in reader:
    rows.append(float(line[1]))
    if float(line[1]) > maxTemp:
        maxTemp = float(line[1])
    if float(line[1]) < minTemp:
        minTemp = float(line[1])

total = sum(rows)
averageTemp = total/len(rows)

print "Temp Report"
print "Average: ", averageTemp
print "Maximum: ", maxTemp
print "Minimum: ", minTemp

