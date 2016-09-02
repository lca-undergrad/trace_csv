# trace.py
# compile a compressed csv from the lca trace data
# 
# Authors: Weston D. Hill & Ronald Macmaster
# Date: 9/2/16

import re
import csv
import gzip


with open("trace-short.txt") as traceFile:
	for line in traceFile:
		print line.rstrip()

