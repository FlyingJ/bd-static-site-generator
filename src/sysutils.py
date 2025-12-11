import os
import shutil

def scrub_destination_directory(destination):
	print(f' - scrubbing destination directory ({destination})')
	if os.path.exists(destination):
		print(f' - {destination} already exists')
		if os.path.isdir(destination):
			print(f' - {destination} is a directory...removing...')
			shutil.rmtree(destination)
		elif os.path.isfile(destination):
			raise Exception(f'  Error: destination ({destination}) is a file')
	print(f' - making new directory ({destination})')
	os.mkdir(destination)
	return True

def copy_directory_contents(source='.', destination=None):
	'''
	- recursive (call for successive directories)
	- copy all content from source directory to destination directory
	- delete all contents of destination directory first (assure clean copy)
	- copy all files, subdirectories
	- log path of each file copied
	'''
	# ensure source directory has been provided and exists
	# or bail
	if not source:
		raise Exception('  Error: source directory must not be None')
	# the source directory must exist
	source = os.path.abspath(source)
	if not os.path.exists(source):
		raise Exception(f'  Error: source ({source}) does not exist')
	# the source directory must be a directory
	if not os.path.isdir(source):
		raise Exception(f'  Error: source ({source}) is not a directory')

	# ensure destination directory has been provided and recreate
	# or bail
	if not destination:
		raise Exception('  Error: destination directory required must not be None')
	destination = os.path.abspath(destination)
	print(f' - calling scrub_destination_directory({destination})')
	if not scrub_destination_directory(destination):
		raise Exception(f'  Error: unable to create destination directory ({destination})')
	
	# get a list of source directory contents and
	# process files and directories as they are identified
	for item in os.listdir(source):
		source_item = os.path.join(source, item)
		destination_item = os.path.join(destination, item)
		if os.path.isfile(source_item):
			print(f' - copying file from {source_item} to {destination_item}')
			shutil.copy(source_item, destination_item)
		elif os.path.isdir(source_item):
			print(f' - copying directory contents from {source_item} to {destination_item}')
			copy_directory_contents(source_item, destination_item)
		else:
			raise Exception(f'  Error: what the file ({file})')

	return True

if __name__ == "__main__":
	source, destination = ('./test_source', './test_destination')
	if not copy_directory_contents(source, destination):
		raise Exception(f' - copy_directory_contents({source}, {destination}) failed')

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