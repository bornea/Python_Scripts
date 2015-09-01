import sys
import re
import os

res_file = open(sys.argv[1], "r")
high_value_list = open(sys.argv[2], "r")

#for line in res_file:
#	for pr_ch in high_value_list:
#		p = re.compile(str(pr_ch))
#		w = p.findall(line)
#		if w.count("C") >= 1:
#			print line

for pr_ch in high_value_list:
	p = re.compile(str(pr_ch))
	print p