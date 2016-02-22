# scrambled
Tools and resources for scrambling sentences using dependency parses, and creating MTurk HITs for descrambling the sentences.


## parse_parse.py

Takes a well-formed stanford dependency parse corpus on stdin, and prints
the sentences as |||-delimimted chunks. An integer argument 'depth' must
be provided; it states the maximum depth to which the dependency tree
is parsed, definine the chunk size.

## hit_maker.py

Generates MTurk HIT CSV rows given information about cost, and sentences.

## res/stanford-english-trees.txt
An example of a well-formed dependency parse corpus. 

## hit.html

HIT interface for workers to unscramble sentences.
