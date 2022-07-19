
# Python program to explain shutil.disk_usage() method 
      
# importing os and sys module 
import os
import sys

# an empty dictionary to hold the files and the dictionary of all files
files_dict = {}

# Parse the file name from user cli argument
user_input = sys.argv[1]

# Check whether Directory path exists or not
if os.path.exists(user_input):
	print("Directory is :",os.path.basename(user_input))

	# an empty dictionary to hold the files and the size of files in bytes
	file_dict ={}

	# using os.walk, will give the files in a directory and sub-directories
	for (dirPath,dirNames,dirFiles) in os.walk(user_input):
		for f in dirFiles:
			# os.path.abspath makes sure a path is absolute.
			dirFilePath= os.path.abspath(os.path.join(dirPath,f))
			
			# Using os.stat() method to get all stats of the file
			fsize = os.stat(dirFilePath)
			
			# extract file size using .st_size object and assign it to the files Dictionary
			file_dict[f]=fsize.st_size

	# assign the file dictionary to suit desired output
	files_dict['files']=[file_dict]

	# print the dictionary for result
	print(files_dict)

else:
    print ("Directory not exists.")

		
