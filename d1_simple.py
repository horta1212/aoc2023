
#!/usr/bin/env python

import argparse
import concurrent.futures
import importlib
import os
import pathlib
import pdb
import sys
import time
import traceback


def read_data(caller, filename=None):
    """
    Read the specified input data file and strip any extra white space from each line.

    :param caller: The path of the caller, e.g. __file__.
    :param filename: The name of the data file, or None to use the format of "day#.txt".
    :return: List of line strings.
    """
    if filename is None:
        filename = pathlib.Path(caller).stem + '.txt'
    datafile = pathlib.Path(caller).parent / 'data' / filename
    with open(datafile, 'r') as f:
        lines = f.readlines()
    lines = [line.strip('\n\r') for line in lines]
    return lines

data = read_data(__file__, "d1_data_preprocessed.txt")

"""
# These were the vim commands used to pre-process the data for p2:

:%s/one/o1e/g  
:%s/two/t2o/g
:%s/three/t3e/g
:%s/four/f4r/g
:%s/five/f5e/g
:%s/six/s6x/g
:%s/seven/s7n/g
:%s/eight/e8t/g
:%s/nine/n9e/g
:%s/[a-zA-Z]//g
:%s/^\d$/\0\0/
:%s/\(.\).*\(.\)/\1\2


"""
print("P2: ", sum(int(item) for item in data))

