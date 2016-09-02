# trace.py
# compile a compressed csv from the lca trace data
#
# Authors: Weston D. Hill & Ronald Macmaster
# Date: 9/2/16

import re
import csv
import gzip

# regular expression to find the information we need in each line
regex = '.*cycle:(\S+)\s+pc:v:(\S+)\s+isWrite:\S+\s+type:(.+?)\s+paddr:p:(\S+)\s+coreid:(\S+)\s+inst:(\S+)$'

# compile the regex into an object
matcher = re.compile(regex)

# print a header to the csv file
print ','.join(('cycle','pc','type','paddr','coreid','inst'))
with open("line.txt") as traceFile:
	for line in traceFile:
		group = matcher.match(line)
        print ','.join(group.groups())
