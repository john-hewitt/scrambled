#!/bin/bash
# In case it's not clear, this is how the 81-line HIT is built.
# Run this from the root git directory.

cat res/sentences_easy_30.txt | python2 hit_maker.py 1 1 >> sentence_descramble_hit.csv
cat res/sentences_medium_30.txt| python2 hit_maker.py 2 0 >> sentence_descramble_hit.csv
cat res/sentences_hard_30.txt | python2 hit_maker.py 3 0 >> sentence_descramble_hit.csv
