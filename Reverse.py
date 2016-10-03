#!/usr/bin/python
from Stack import Stack
from decimal import Decimal
import sys, getopt
import os
import fileinput
import argparse

ifile = None
ofile = None


class Reverse():
    """class Reverse to reverse the sound file"""
    def __init__(self, ifilename, ofilename):
        self.ifile = ifilename
        self.ofile = ofilename

    def open_read_file(self, ifile, ofile):
        s = Stack()
        fileIn = open(self.ifile, "r")
        #fileOut = open(self.ofile, "w")

        str = fileIn.readline()
        list = []
        list = str.split(" ")
        sampleRate = list[3]
        counter = 0
        while fileIn.readline() != None:
            strtemp = fileIn.readline()
            if 'str' in strtemp:
                break
            else:
                print(strtemp)
                counter += 1
        print(counter)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and write file')
    parser.add_argument("--ifile", help="Input file path/name")
    parser.add_argument("--ofile", help="Output file path/name")

    args = parser.parse_args()


    r = Reverse(args.ifile, args.ofile)
    r.open_read_file(ifile, ofile)










