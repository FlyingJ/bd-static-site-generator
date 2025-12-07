import os
import shutil

def clone_dir(src='.', dest=None):
	'''
	- recursive (call for successive directories)
	- copy all content from src directory to dest directory
	- delete all contents of dest directory first (assure clean copy)
	- copy all files, subdirectories
	- log path of each file copied
	'''
	# ensure source directory has been provided and exists
	# or bail
	if not src:
		raise Exception('  Error: source directory must not be None')
	# the src directory must exist
	src = os.path.abspath(src)
	if not os.path.exists(src):
		raise Exception(f'  Error: source ({src}) does not exist')
	# the src directory must be a directory
	if not os.path.isdir(src):
		raise Exception(f'  Error: source ({src}) is not a directory')
	# or we must panic

	# ensure destination directory has been provided and recreate
	# or bail
	if not dest:
		raise Exception('  Error: destination directory required for cloning')
	dest = os.path.abspath(dest)
	prepare_destination(dest)
	
	# get a list of source directory contents
	# separate files and directories
	# copy files from source to destination
	# call clone_dir for each directory


'''
os.listdir
os.mkdir
os.path.abspath
os.path.exists
os.path.isdir
os.path.isfile
os.path.join
shutil.copy
shutil.rmtree
'''