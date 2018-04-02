import os
import exifread

cwd = os.getcwd()


print("This program will rename the pictures in the folders you executed it in, according to its EXIF-information")
print("Your current directory is: " + cwd)


list_of_files_with_no_exif = []
double_names_nr =0
name_of_double=""
new_name_of_last_picture = ""
nr_of_subdirs = 0
list_of_all_dirs = []
dir_seperator = "/"

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
	print("processing file: %s " % filepath)
	dateTime_renamed = str(dateTime).replace(":", "_")
	global double_names_nr
	global name_of_double
	global dir_seperator
	
###TODO:: Wenn ein anderes DOPPELTES Bild bereits benannt wurde und nun nochmal benannt werden soll gibt es eine 
### EXCEPTION IN DER EXCEPTION! FIX IT!

	try:		
		print("renaming: " + filepath)
		os.rename(filepath, current_folder + dir_seperator + str(dateTime_renamed) + filetype)
		#check localy for doubles and rename them without global var...
		
	except FileExistsError:
		os.rename(filepath, os.getcwd()+ dir_seperator + str(dateTime_renamed) + str(double_names_nr) + filetype)
		double_names_nr += 1


def count_and_process_files(process):
	global dir_seperator
	global list_of_all_dirs
	nr_of_pictures = 0
	if not process:
		for current_folder in list_of_all_dirs:		
			for filename in os.listdir(current_folder):
				if filename.endswith(".JPG"):
					nr_of_pictures +=1
				if filename.endswith(".jpg"):
					nr_of_pictures +=1
				if filename.endswith(".png"):
					nr_of_pictures +=1
				if filename.endswith(".jpeg"):
					nr_of_pictures +=1
		print("I found " + str(nr_of_pictures) + " pictures.")

	if process:
		global double_names_nr
		for current_folder in list_of_all_dirs:	
			double_names_nr = 0	
			for filename in os.listdir(current_folder):
				if filename.endswith(".JPG"):
					rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
					nr_of_pictures +=1
				if filename.endswith(".jpg"):
					rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
					nr_of_pictures +=1
				if filename.endswith(".png"):
					rename(current_folder + dir_seperator + filename, ".png", current_folder)
					nr_of_pictures +=1
				if filename.endswith(".jpeg"):
					rename(current_folder + dir_seperator + filename, ".JPG", current_folder)
					nr_of_pictures +=1
				
def show_files_missing_EXIF():
	global list_of_files_with_no_exif
	print("there were " + str(len(list_of_files_with_no_exif)) + "Pictures that i couldnt rename, because there was no EXIF-Information")
	wanna_show = input("do you wish to see a list of these pictures? (True/False): ")
	if wanna_show :
		for pics in list_of_files_with_no_exif:
			print(pics)



list_of_all_dirs.append(cwd)
check_for_subdirectories(cwd)
print("total directories (including current dir): " + str(nr_of_subdirs))

#for direc in list_of_all_dirs:
#	print(direc)

#check_for_doubles()
count_and_process_files(False)
process = input("do you want to rename all the Files? (True/False): ")
count_and_process_files(process)
show_files_missing_EXIF()
