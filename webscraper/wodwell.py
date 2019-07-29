import requests
from bs4 import BeautifulSoup
from csv import writer

print('88888888888888888888888888888888888888888888888888888888888888888888888888888888')
print('88888888888888888888888888888888888888888888888888888888888888888888888888888888')
url = 'https://wodwell.com/wods/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
#print(response.content.decode())


soup = BeautifulSoup (response.text,'html.parser')
wods = soup.find_all(class_='wod-description')

for wd in wods:
    title = wd.find(class_='wod-title').get_text()
    description = wd.find(class_='wod-preview-entry').get_text().replace('"<br/>"','')
    #print(wd)
    #print(title)
    print (description)
    print('--------------------')

