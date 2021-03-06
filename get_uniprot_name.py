import urllib2
from bs4 import BeautifulSoup
import lxml
import sys

uniprot_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')
uniprot_set = set(uniprot_file) #Turns into set so only unique ids are run
uniprot_list = list(uniprot_set) #Turns set back into list

def get_name(uniprot_accession_in):
	try: #Protects from bad ids if the id is bad then it is returned as an error and passed
		data_name = urllib2.urlopen("http://www.uniprot.org/uniprot/" + uniprot_accession_in + ".xml") #Acquires .xml data
	except:
		return "Error" 
		pass 
	soup_name = BeautifulSoup(data_name, "xml") #Puts .xml into bs4
	soup_name = soup_name.find_all(type="primary") #Limits the tags to those that have a mass
	if len(soup_name) > 0: #Ensures that there is mass for the id if not return N/A
		for sources in soup_name:
			name_pri = sources.string
		return name_pri
	else: 
		return "N/A"	

for id in uniprot_list:
    id = id.replace("\n","") #remove \n for input into function or else it isn't formatted correctly
    id = id.replace("\r","") #ditto for \r
    output_file.write(id + "\t" + str(get_name(id)) + "\n")

uniprot_file.close()
output_file.close()