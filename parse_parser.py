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
depth = int(args.difficulty)


def extract_text(tup, depth):
    '''
    Extracts text from a stanford sentence dependency parse tuple.
    Initial input is a sentence-tuple
    All text assumed to be in 2-tuples of form (POS, token). 
    Inserts ||| delimiters until depth of granularity reached.
    '''
    temp = ''
    if depth > 0:
        temp = '||| '

    # Iterate over all elements in current tuple
    for elem in tup:
        if isinstance(elem, tuple):
            # Look one level deeper to see if next tuple encodes text
            if len(elem) == 2\
                    and isinstance(elem[0], str)\
                    and isinstance(elem[1], str):
                        if depth > 1:
                            temp = temp + " ||| " + elem[1]
                        else:
                            temp = temp + " " + elem[1] #Return the word, not the POS
            #Else, walk further down the tuple
            else:
                temp = temp + extract_text(elem, depth - 1)
        # Strings outside of a 2-tuple are POS tags. Ignore,
        # but match to this case to avoid TypeError
        elif isinstance(elem, str):
            pass
        # Signifies malformed sentence parse tuple
        else:
            raise TypeError
    return temp



# stdin should be a file containing sentence parses.
# sentences may take arbitrary numbers of lines.
# Subsequent sentences must be delimited by an empty line
while stdin:
    line = ''
    try:
        line = stdin.next()
    except StopIteration:
        pass

    # Parse a single sentence
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

    # Format sentence text, eval into tuple
    sentence_buffer = sentence_buffer.strip()[1:-1]
    sentence_buffer = re.sub(r'[A-Z\+\/\-\.\?\d\*\`\,\'\$\!\%\:\;\\]+', lambda x: '"' + x.group() + '"' , sentence_buffer, flags=re.IGNORECASE)
    sentence_array = sentence_buffer.split()
    sentence_tuple_string = ', '.join(sentence_array)
    sentence_tuple = eval(sentence_tuple_string)

    # extract text, splitting to desired granularity
    sentence = re.sub(r'( *\|\|\| *){1,4}', ' ||| ', extract_text(sentence_tuple, depth))

    # Remove prepended '||| '
    sentence = sentence[4:]

    # Print to stdout
    print sentence
