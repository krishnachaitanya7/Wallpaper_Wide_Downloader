# Wallpaper_Wide_Downloader
Used to download wallpapers from wallpaperwide.com of a specific category all at once. In the constants file just specify
from which URL the download needs to be started and how many pages you wanna download. 
# Directions For Use
Below is the sample of Constant_Values.py . It's the only file that needs to be edited unless you are a developer and wants to tweak the code.

type_to_download = 'http://wallpaperswide.com/celebrities-desktop-wallpapers.html' #This is the URL from the site, the category of wallpapers which someone wants to download

first_index_of_wallpapers = 3 #All categories of wallpapers start from 1 but if someone wants to download from 3 No page it needs to be set here like this

last_index_of_wallpapers = 274 #Last page in this category of wallpapers. Needs to be found out manually and set here. The last page constant set here can be less than original last page in the website. Its totally according to the user

Now run "$ python Wallpaperwide_Downloader.py" and all the wallpapers in that category will be downloaded in 136x768 resolution.

# Future Work
Different resolution support needs to be added
