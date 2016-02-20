#!/bin/bash/python2
#
# Takes a well-formed Stanford sentence dependency parse file on stdin, as well
# as an integer difficulty level (level of granularity of chunks to spit out)
# On stdout, prints sentences, |||-split 
# 
# I will arrive at five thirty at the airport
# I will ||| arrive at five thirty ||| at the airport
# I ||| will ||| arrive ||| at five thirty ||| at ||| the airport


# Author: John Hewitt | johnhew@seas.upenn.edu

import argparse
import re
from sys import stdin
import string

argp = argparse.ArgumentParser()
argp.add_argument('difficulty', help='integer, from 1 to 3, which determines\
        the level of granularity of the parse')

args = argp.parse_args()

while stdin:
    line = ''
    try:
        line = stdin.next()
    except StopIteration:
        pass
    sentence_buffer = ''
    while line.strip(' ') != '\n':
        sentence_buffer +=  filter(lambda x: x in string.printable, line.strip()) + ' '
        try:
            line = stdin.next()
        except StopIteration:
            break
    if not sentence_buffer:
        continue

    if not line:
        break
    print len(sentence_buffer)
    sentence_buffer = sentence_buffer.strip()[1:-1]
    sentence_buffer = re.sub(r'[A-Z\+\/\-\.\?\d\*\`\,\'\$\!\%\:\;\\]+', lambda x: '"' + x.group() + '"' , sentence_buffer, flags=re.IGNORECASE)
    print len(sentence_buffer)
    sentence_array = sentence_buffer.split()
    sentence_tuple_string = ', '.join(sentence_array)
    #sentence_tuple_string = re.sub(r'[A-Z\-\.\?\d\*\`]+', lambda x: '"' + x.group() + '"' , sentence_tuple_string, flags=re.IGNORECASE)
    #print sentence_tuple_string
    print eval(sentence_tuple_string)
   # print(eval(sentence_tuple_string)), type(eval(sentence_tuple_string))

def quote(m):
    return  '"' + m.groups(0) + '"'





