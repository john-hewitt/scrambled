#!/usr/bin/python
#
# Takes an MTurk HIT with reference sentence, and worker-descrambled sentence.
# Evaluates the worker-descrambled sentence based on an a chunk-inversions metric. 
# Writes CSV to new file, including all old information, as well as the score 
# of the de-scrambling, in a new column.
#
# Author : John Hewitt : johnhew@seas.upenn.edu

import sys
import unicodecsv as csv
import math



reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(open('mturk_descramble_scored.csv', 'w'), fieldnames=reader.fieldnames)
for i in range(0,30):
    writer.fieldnames.append('score_percent%i'%i)

writer.fieldnames.append('score_percent')
writer.fieldnames.append('answer_inversions')
writer.fieldnames.append('max_inversions')


for line in reader:
    # Pair together gold standard (index 0) and answer orderings (index 1)
    pairs = []
    for i in range(0,30):
        pairs.append((line['sentence%i'%i], line['answer%i'%i]))

    # For each pair, compute the maximum number of inversions
    for i, pair in enumerate(pairs):
        gold_array = [x.strip() for x in pair[0].split('|||')]
        answer_array = [x.strip() for x in pair[1].split('|||')]
        if len(gold_array) != len(answer_array):
            raise TypeError
        max_inversions = len(gold_array)*(len(gold_array) - 1)/2

        # Store the gold-standard ordering of chunks
        chunk_positions = {}
        for count, chunk in enumerate(gold_array):
            chunk_positions[chunk] = count

        # Compute the number of inversions in the answer ordering
        inversions = 0
        for index, chunk in enumerate(answer_array):
            rank = chunk_positions[chunk]
            inversions += abs(rank - index)

        score_count = max_inversions - inversions
        score_percent = float(score_count) / max_inversions * 100

        line['score_percent%i'%i] = str(score_percent)
    writer.writerow(line)




        


