#!/usr/bin/python
# trace.py
# compile a compressed csv from the lca trace data
#
# Authors: Weston D. Hill & Ronald Macmaster
# Date: 9/2/16

import re
import gzip
import sys

if(not len(sys.argv) == 3):
	print("usage: trace.py <input.gz> <output.gz>")
	exit(1)

# regular expression to find the information we need in each line
regex = '.*cycle:(\S+)\s+pc:v:(\S+)\s+isWrite:\S+\s+type:(.+?)\s+paddr:p:(\S+)\s+coreid:(\S+)\s+inst:(\S+)$'

# compile the regex into an object
matcher = re.compile(regex)

# print a header to the csv file
header = ','.join(('cycle','pc','type','paddr','coreid','inst'))
with gzip.open(sys.argv[1]) as traceFile, gzip.open(sys.argv[2], "w+") as csvFile:
	csvFile.write(header + "\n")
	for line in traceFile:
		group = matcher.match(line)
		csvString = ','.join(group.groups())
		csvFile.write(csvString + "\n")
