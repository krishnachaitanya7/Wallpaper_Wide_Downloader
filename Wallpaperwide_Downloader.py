import urllib2
from bs4 import BeautifulSoup
import Downloader
import Constant_Values
type_to_download = Constant_Values.type_to_download
first_index_of_wallpapers = Constant_Values.first_index_of_wallpapers
last_index_of_wallpapers = Constant_Values.last_index_of_wallpapers
download_type_base_url = type_to_download[:-5]
for i in range(first_index_of_wallpapers,last_index_of_wallpapers+1):
    page = urllib2.urlopen(download_type_base_url+'/page/'+str(i))
    soup = BeautifulSoup(page)
    tags=soup.findAll('img')
    for j,url_tag in enumerate([tag['src'] for tag in tags]):
        if j < 10:
            print url_tag
            Downloader.download_url('http://wallpaperswide.com/download/'+url_tag.split('/')[-1][:-7]+'-wallpaper-1366x768.jpg')

