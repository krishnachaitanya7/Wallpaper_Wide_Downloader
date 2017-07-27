import magic
import glob
import os
def file_checker_and_deleter():
	mime = magic.Magic(mime=True)
	for file_jpg in glob.glob("*.jpg"):
		if mime.from_file(str(file_jpg)) == 'text/html':
			os.remove(str(file_jpg))
if __name__ == "__main__":
	file_checker_and_deleter()
        	
        	
	
		

