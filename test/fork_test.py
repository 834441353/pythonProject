import os
import time

def asa():
    print('as')

def ad():
    print('ad')

def main():
    ret = os.fork()
    if ret == 0:
        ad()
    else:
        asa()