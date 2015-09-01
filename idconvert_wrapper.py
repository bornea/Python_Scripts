import os
import sys

#XML file specifies these values based upon options on Galaxy.
input_file = open(sys.argv[1],'r') 
output_file = sys.argv[2]
output_format = sys.argv[3]

#Changes the cmd by the os.system() function based upon desired output.
#idconvert by default writes the file as spectra.format which needs to changed after it has completed the operation so galaxy can identify it. 
if output_format == "mzid":
	cmd = "idconvert " + str(sys.argv[1])
	os.system(cmd)
	open('spectra.mzid')
	os.rename('spectra.mzid', str(sys.argv[2])) 
elif output_format == "pepxml":
	cmd = "idconvert " + str(sys.argv[1]) + " --pepXML"
	os.system(cmd)
	open('spectra.pepXML')
	os.rename('spectra.pepXML', str(sys.argv[2])) 
elif output_format == "text":
	cmd = "idconvert " + str(sys.argv[1]) + " --text"
	os.system(cmd)
	open('spectra.txt')
	os.rename('spectra.txt', str(sys.argv[2])) 