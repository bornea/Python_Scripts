import sys
import re

og_list = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')
for i in range(1):
	line = og_list.next().strip() 
	out_file.write(line + "\t Protein\n")

for i in og_list:
	bob = i[:-1]
	id_lines = re.compile('>sp')
	m = id_lines.match(bob)
	if m:
		lines_split = i.split('|')
		uniport_id = lines_split[1]
	else: 
		out_file.write(bob + "\t" + uniport_id + '\n')
