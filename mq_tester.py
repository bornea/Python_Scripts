import os
import sys
import subprocess
from bs4 import BeautifulSoup
import os.path

if sys.platform.startswith("win"):
    # Don't display the Windows GPF dialog if the invoked program dies.
    # See comp.os.ms-windows.programmer.win32
    # How to suppress crash notification dialog?, Jan 14,2004 -
    # Raymond Chen's response [1]

    import ctypes
    SEM_NOGPFAULTERRORBOX = 0x0002 # From MSDN
    ctypes.windll.kernel32.SetErrorMode(SEM_NOGPFAULTERRORBOX);
    subprocess_flags = 0x8000000 #win32con.CREATE_NO_WINDOW?
else:
    subprocess_flags = 0

bad_list = []
for root, dirs, files in os.walk(r"C:\MaxQuant\Data"):
	for file in files:
		if r".raw" in str(file):
			par_file = open("C:\MaxQuant\Data\mqpar_pp.xml", 'r')
			template_soup = BeautifulSoup(par_file,"xml")
			file_path_tag = template_soup.filePaths
			file_path_tag.clear()
			new_tag = template_soup.new_tag("string")
			file_path_tag.append(new_tag)
			new_tag.string = str(root) + "\\" + str(file)
			par_file.close()
			par_file = open("C:\MaxQuant\Data\mqpar_pp.xml", 'w')
			par_file.write(str(template_soup))
			par_file.close()
			cmd = r'C:\MaxQuant\bin\MaxQuantCmd.exe C:\MaxQuant\Data\mqpar_pp.xml'
			process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess_flags)
			(stdout, stderr) = process.communicate()
			num_files = len([f for f in os.listdir(r"C:\MaxQuant\Data\combined\proc") if os.path.isfile(os.path.join(r"C:\MaxQuant\Data\combined\proc", f))])
			if num_files < 45:
				bad_list.append(file)
			cmd1 = r"rd /s /q C:\MaxQuant\Data\combined\proc"
			os.system(cmd1)
bad_file = open(r"C:\MaxQuant\Data\bad_files.txt", "w")
for i in bad_list:
	print i
	bad_file.write(str(i) + "\n") 