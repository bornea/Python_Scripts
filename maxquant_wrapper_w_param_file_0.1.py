import sys
import os
from bs4 import BeautifulSoup
import lxml

template_file = sys.argv[1]
file_locations_joined = sys.argv[2]
file_locations = file_locations_joined.split(",")
database_file = sys.argv[3] 

cmd = r"copy " + str(template_file) + r" C:\mq_jobs" 
os.system(cmd)

cmd1 = r"rename C:\mq_jobs\\" + str(template_file) + " mqpar.xml"
os.system(cmd1)

template_file1 = open("C:\mq_jobs\mqpar.xml",'r')
template_soup = BeautifulSoup(template_file1, 'xml')

file_path_tag = template_soup.filePaths
#Locates the tag that spcifies the raw file path in soup

file_path_tag.clear()

for i in file_locations: 
   new_tag = template_soup.new_tag("string")
   file_path_tag.append(new_tag)
   #Creates a new tag named <string> inside filePaths
   cmd2 = "copy " + str(i) + r" C:\mq_jobs"
   os.system(cmd2)
   #Copies the dat files to mq_jobs
   new_string = i.split('\\')[-1]
   #Breaks the original file path into the file name w/ extension
   root = new_string.split(".")[0]
   #Creates root which is just the file root
   cmd3 = r"rename C:\mq_jobs\\" + str(new_string) + r" " + str(root) + r".raw"
   os.system(cmd3)
   #Renames the file to .raw
   new_tag.string = r'C:\mq_jobs\\' + str(root) + r".raw"
   #Adds the file path to the string tag (new_tag is named string the .string changes the path inside the string tags)
   #Entire loop does it for every .dat file specified by Galaxy

fasta_path_tag = template_soup.fastaFiles
#Locates the Fasta file path in template
fasta_path_tag.clear()
new_tag = template_soup.new_tag("string")
fasta_path_tag.append(new_tag)
#Creates a new tag named <string> inside fastaFiles
cmd4 = "copy " + str(database_file) + r" C:\mq_jobs"
os.system(cmd4)
#Copies the dat files to mq_jobs
new_string = database_file.split('\\')[-1]
#Breaks the original file path into the file name w/ extension
root = new_string.split(".")[0]
#Creates root which is just the file root
cmd5 = r"rename C:\mq_jobs\\" + str(new_string) + r" " + str(root) + r".fasta"
os.system(cmd5)
#Renames the file to .fasta
new_tag.string = r'C:\mq_jobs\\' + str(root) + r'.fasta'
#Adds the file path to the string tag new_tag is named string the .string changes 

template_file1.close()

template_file2 = open("C:\mq_jobs\mqpar.xml",'w')
template_file2.write(str(template_soup))

template_file2.close()
#Close mqpar.xml so it can be used by MaxQuant

#cmd6 = r"MaxQuantCmd.exe C:\mq_jobs\mqpar.xml"
#os.system(cmd6)
#Runs MaxQuantCMD.exe with newly create mqpar.xml file

cmd7 = r"copy C:\mq_jobs\combined\txt\peptides.txt ."
os.system(cmd7)

os.rename("peptides.txt", str(sys.argv[4]))
#Renames the summary.txt what is specified as the output by Galaxy