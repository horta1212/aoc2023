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

data = read_data(__file__, "d1_data.txt")

"""
# These are the equivalent vim commands used to pre-process the data for p2:

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

translate_dict = {'one':'o1e','two':'t2o','three':'t3e','four':'f4r','five':'f5e','six':'s6x','seven':'s7n','eight':'e8t','nine':'n9e'}
def day1(translate_dict={' ':' '}):
    total=0
    for item in data:
        for key, replace in translate_dict.items():
            item = item.replace(key,replace)
        item = ''.join(char for char in item if char.isnumeric())
        if len(item)==1:
            item = item + item
        item = item[0]+item[-1]
        total+=int(item)
    return(total)

import bryces_utils as bu
with bu.Timer('P1'):
    print("P1: ", day1())
with bu.Timer('P2'):
    print("P2: ", day1(translate_dict)) 

