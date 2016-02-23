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

if len(sys.argv) < 3:
    print >> sys.stderr, "not enough stuff"
    exit(1)

difficulty = sys.argv[1]
write_header_bool = int(sys.argv[2])

# All 30 sentences should be used in the CSV
sentences = []
for line in sys.stdin:
    sentences.append(line.strip())

# However many sentences were used, give as many answer columns.
for i in range(len(sentences)):
    sentences.append('')


# Write the titles of the columns.
row_header = []
for i in range(0,30):
    row_header.append('sentence' + str(i))
for i in range(0,30):
    row_header.append('answer' + str(i))
row_header.append('cost')
row_header.append('difficulty')


# Each line should have a difficulty and a cost
with sys.stdout as out:
    csv_out = csv.writer(out)
    if write_header_bool:
        csv_out.writerow(row_header)
    for cost in costs:
        sentences.append(str(cost))
        sentences.append(str(difficulty))
        for i in range(0,9):
            csv_out.writerow(sentences)
        sentences = sentences[:-2]

