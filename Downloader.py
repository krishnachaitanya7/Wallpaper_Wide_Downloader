import requests
def download_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
    r = requests.get(url,headers=headers)
    nameoffile = url.split('/')[-1]
    with open(nameoffile, "wb") as wallsaver:
        wallsaver.write(r.content)