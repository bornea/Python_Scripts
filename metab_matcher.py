import sys

input_file = open(sys.argv[1])
metabs = open(sys.argv[2], "r")
outfile = open(sys.argv[3], "a")

for line in input_file:
	w = line.split()
	for metab in metabs:
		if metab in w:
			outfile.write(str(line) + "\n")



		



