#!/bin/bash/python2
#
# Gobbles a file on stdin containing chunked sentences of 1 difficulty level
# Takes, as an argument, 1 OR 2 OR 3, an integer corresponding to 
# (easy, medium, hard) -- the difficulty level of descrambling the sentences
# Hard-coded in are 3 payment levels.
# Output, on stdout, is 9 CSV lines (corresponding to 9 unique turkers) for 
# each combination of (payment, difficuly). 
#
# CSV Format:
#   columns 1-30    column 31   column 32     
#   sentence 1-30   difficulty  payment
#

costs = (0.1, 0.3, 0.5)

import sys
import unicodecsv as csv

if len(sys.argv) < 2:
    exit(1)

difficulty = sys.argv[1]

# All 30 sentences should be used in the CSV
sentences = []
for line in sys.stdin:
    sentences.append(line.strip())

# Write the titles of the columns.
rows = []
for i in range(0,30):
    rows.append('column' + str(i))
rows.append('cost')
rows.append('difficulty')


# Each line should have a difficulty and a cost
with open('HIT_csv', 'a') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(rows)
    for cost in costs:
        sentences.append(str(cost))
        sentences.append(str(difficulty))
        for i in range(0,9):
            csv_out.writerow(sentences)
        sentences = sentences[:-2]

