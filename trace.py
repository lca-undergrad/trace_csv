# trace.py
# compile a compressed csv from the lca trace data
# 
# Authors: Weston D. Hill & Ronald Macmaster
# Date: 9/2/16

import re
import csv
import gzip

regex = '.*cycle:(\S+)\s+pc:v:(\S+)\s+isWrite:\S+\s+type:(.+?)paddr:p:(\S+)\s+coreid:(\S+)\s+inst:(\S+)$'
matcher = re.compile(regex)
print regex
with open("line.txt") as traceFile:
	for line in traceFile:
		group = matcher.match(line)
		print group.groups()
