import os
import shutil

def prepare_destination(dest):
	if 
	print(f' - INFO: removing ')
	shutil.rmtree(dest)
	os.mkdir(dest)

def copy_process_source(src, dest):
	for file in os.listdir(src):



def clone_dir(src='.',dest=None):
	'''
	- recursive (call for successive directories)
	- copy all content from src directory to dest directory
	- delete all contents of dest directory first (assure clean copy)
	- copy all files, subdirectories
	- log path of each file copied
	'''
	# we must be called with a dest directory
	# or we must panic
	if not dest:
		raise Exception('  Error: destination directory required for cloning')
	dest = os.path.abspath(dest)
	prepare_destination(dest)

	# we must be called with a src directory
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
	
	copy_source(src, dest)


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