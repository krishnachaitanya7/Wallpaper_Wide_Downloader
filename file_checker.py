import magic
import glob
import os
mime = magic.Magic(mime=True)
for file_jpg in glob.glob("*.jpg"):
        if mime.from_file(str(file_jpg)) == 'text/html':
		os.remove(str(file_jpg))
        	
        	
	
		

