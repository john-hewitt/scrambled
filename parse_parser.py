#!/bin/bash/python2
#
# Takes a well-formed Stanford sentence dependency parse file on stdin, as well
# as an integer difficulty level (level of granularity of chunks to spit out)
# On stdout, prints sentences, |||-split 
#
# Author: John Hewitt | johnhew@seas.upenn.edu

import argparse

argp = argparse.ArgumentParser()
argp.add_argument('difficulty', help='integer, from 1 to 3, which determines\
        the level of granularity of the parse')

args = argp.parse_args()

for line in stdin:
    pass()




