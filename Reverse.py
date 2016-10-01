#!/usr/bin/python
from Stack import Stack
import sys, getopt
import os
import fileinput

fileName = None
fileName2 = None

class Reverse():
	"""class Reverse to reverse the sound file"""
	def __init__(self, filename):
		self.fileName = fileName

	def open_read_file(argv):
		inputfile = ''
		outputfile = ''
		try:
			opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
		except getopt.GetoptError:
			print ('Reverse.py -i <inputfile> -o <outputfile>')
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print ('Reverse.py -i <inputfile> -o <outputfile>')
			elif opt in ("-i", "--ifile"):
				inputfile = arg
			elif opt in ("-o", "--ofile"):
				outputfile = arg


r =  Reverse(filename)
Reverse.open_read_file(sys.arg[1:])






