import sys 

input_combined = str(sys.argv[1])
input_list = input_combined.split(".")

print input_list

for i in input_list:
	i = i + 'hello' 
	print i

