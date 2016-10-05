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
        fileOut = open(self.ofile, "w")

        strTemp = fileIn.readline()
        list = []
        list = strTemp.split(" ")
        sampleRate = list[3]
        counter = 0
        for line in fileIn:
            if line == " " or line == "":
                break
            else:
                tempList = line.split(" ")
                if tempList[0] == ";":
                    continue
                else:
                    tempL = []
                    for l in tempList:
                        if l != "":
                            tempL.append(l)
                        else:
                            continue
                    s.push(tempL[1])
                    counter += 1
        numSteps = 0
        tempsamplerate = float(sampleRate)
        fileOut.write("; Sample Rate " + sampleRate)
        while s.size() > 0:
            fileOut.write(str((float(numSteps) / tempsamplerate)) + "\t" + s.peek() + "\n")
            s.pop()
            numSteps += 1

        fileIn.close()
        fileOut.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read and write file')
    parser.add_argument("--ifile", help="Input file path/name")
    parser.add_argument("--ofile", help="Output file path/name")

    args = parser.parse_args()

    r = Reverse(args.ifile, args.ofile)  #creating Reverse object with input and output files
    r.open_read_file(ifile, ofile)










