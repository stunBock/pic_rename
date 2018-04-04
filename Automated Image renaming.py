#Stinkbock-Coding :P#

import os
import exifread

cwd = os.getcwd()


print("This program will rename the pictures in the folders you executed it in, according to its EXIF-information")
print("Your current directory is: " + cwd)


list_of_files_with_no_exif = []
double_names_nr =0
nr_of_subdirs = 0
list_of_all_dirs = []
dir_seperator = "\\"

def check_for_subdirectories(base_directory):
	global nr_of_subdirs
	global list_of_all_dirs
	global dir_seperator
	list_temp_dirs = []

	for file_or_folder in os.listdir(base_directory):		#put all subdirs in one list
		if os.path.isdir(base_directory + dir_seperator + file_or_folder):
			list_temp_dirs.append(file_or_folder)
			
	for y in list_temp_dirs:
		print(y)

	for x in list_temp_dirs:								#entering subdir and recursiveley call funct.
		x_total_dir = base_directory + dir_seperator + x
		print("entering: " + x_total_dir)
		nr_of_subdirs +=1
		list_of_all_dirs.append(x_total_dir)
		check_for_subdirectories(x_total_dir)


def check_for_doubles():		
	print("do you want me to check for doubles within each folder, ")
	print("or do you want me to check for doubles within the entire selected filesystem?")
	print("type (dir) for search only within a directory or (all) if you want to search in all subfolders")
	where_to_check_for_doubles = input("type (none) if u do not wish to search for doubles at all.")
	
	if where_to_check_for_doubles == "dir":
		print(where_to_check_for_doubles)
	elif where_to_check_for_doubles == "all":
		print(where_to_check_for_doubles)
	elif where_to_check_for_doubles == "none":
		print(where_to_check_for_doubles)
	else:
		print("incorrect input! try again..")
		check_for_doubles()

#def brainstorm():
	#list_of_all_dirs
	#list_of_all_files_within_a_dir
	#for x in list_of_all_files_within_a_dir:
	#	open file and get datetime
	#	listOfDatetimeswithinFolder.append()

	
def rename(filepath, filetype, current_folder):
	photo_file = open(filepath, "rb")
	all_info = exifread.process_file(photo_file)
	photo_file.close()
	dateTime = ""
	for tag in all_info.keys():
		if tag == "EXIF DateTimeOriginal":
			dateTime = all_info[tag] #datetime = string mit datetime
	if dateTime == "":
		list_of_files_with_no_exif.append(filepath)
		print(filepath + " is not processable due to missing EXIF-Information")
		return
	
	dateTime_renamed = str(dateTime).replace(":", "_")
	global double_names_nr
	global dir_seperator
	
###TODO:: Wenn ein anderes DOPPELTES Bild bereits benannt wurde und nun nochmal benannt werden soll gibt es eine 
### EXCEPTION IN DER EXCEPTION! FIX IT!
	rename_success = False
	while not rename_success:
		try:		
			print("renaming: " + filepath + " ---> " + current_folder + dir_seperator + str(dateTime_renamed) + filetype)
			os.rename(filepath, current_folder + dir_seperator + str(dateTime_renamed) + filetype)
			#  check localy for doubles and rename them without global var...
			rename_success = True
			print("tibbers")
		
		except FileExistsError:
			print("renaming within exception: " + filepath + " ---> " + current_folder + dir_seperator + str(dateTime_renamed) + str(double_names_nr) + filetype)
			try:
				os.rename(filepath, current_folder + dir_seperator + str(dateTime_renamed) + str(double_names_nr) + filetype)
				double_names_nr += 1
				rename_success = True
			except:
				double_names_nr += 1
				rename_success = False

def count_files(list_of_all_dirs, inside_subdir = False):
	
	nr_of_pictures = 0
	list_temp_files = []
	for current_folder in list_of_all_dirs:		
		for filename in os.listdir(current_folder):
			if filename.endswith(".JPG"):
				nr_of_pictures +=1
				list_temp_files
			if filename.endswith(".jpg"):
				nr_of_pictures +=1
			if filename.endswith(".png"):
				nr_of_pictures +=1
			if filename.endswith(".jpeg"):
				nr_of_pictures +=1
	if not inside_subdir:
		print("I found " + str(nr_of_pictures) + " pictures.")


def process_files():
	global dir_seperator
	global list_of_all_dirs
	

	
	global double_names_nr
	for current_folder in list_of_all_dirs:	
		double_names_nr = 0	
		for filename in os.listdir(current_folder):
			if filename.endswith(".JPG"):
				rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
				
			if filename.endswith(".jpg"):
				rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
				
			if filename.endswith(".png"):
				rename(current_folder + dir_seperator + filename, ".png", current_folder)
				
			if filename.endswith(".jpeg"):
				rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
				
				
def show_files_missing_EXIF():
	global list_of_files_with_no_exif
	if len(list_of_files_with_no_exif) == 0:
		print("All pictures have been processed and are now in the correct format!")
		return

	print("there were " + str(len(list_of_files_with_no_exif)) + "Pictures that i couldnt rename, because there was no EXIF-Information")
	wanna_show = input("do you wish to see a list of these pictures? (True/False): ")
	if wanna_show :
		for pics in list_of_files_with_no_exif:
			print(pics)



list_of_all_dirs.append(cwd)
check_for_subdirectories(cwd)
print("total directories (including current dir): " + str(nr_of_subdirs))


#check_for_doubles()
count_files(list_of_all_dirs)
want_to_process = input("do you want to rename all the Files? (True/False): ")

if want_to_process :
	process_files()
	show_files_missing_EXIF()
else:
	print("Program closed!")