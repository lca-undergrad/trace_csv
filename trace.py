# trace.py
# compile a compressed csv from the lca trace data
#
# Authors: Weston D. Hill & Ronald Macmaster
# Date: 9/2/16

import re
import gzip

# regular expression to find the information we need in each line
regex = '.*cycle:(\S+)\s+pc:v:(\S+)\s+isWrite:\S+\s+type:(.+?)\s+paddr:p:(\S+)\s+coreid:(\S+)\s+inst:(\S+)$'

# compile the regex into an object
matcher = re.compile(regex)

# print a header to the csv file
header = ','.join(('cycle','pc','type','paddr','coreid','inst'))
with gzip.open("trace-short.txt.gz") as traceFile, gzip.open("trace.csv.gz", "w+") as csvFile:
	csvFile.write(header + "\n")
	for line in traceFile:
		group = matcher.match(line)
		csvString = ','.join(group.groups())
		csvFile.write(csvString + "\n")
