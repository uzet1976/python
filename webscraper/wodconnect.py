import requests
from bs4 import BeautifulSoup
from csv import writer

url='https://www.wodconnect.com/workout_lists'
response = requests.get(url)
wods_page_soup = BeautifulSoup(response.text,'html.parser')
wods_page_urls = wods_page_soup.find_all(class_="card")

for url_link in wods_page_urls:
    tt="https://www.wodconnect.com"+url_link.find('a')["href"]
    print(tt)

#tt="https://www.wodconnect.com"+wods_page_urls[1].find('a')["href"]
#print(tt)


url = 'https://www.wodconnect.com/workout_lists/cf8000-high-camp'

#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url)#, headers=headers)


soup = BeautifulSoup (response.text,'html.parser')
wods = soup.find_all(class_='workout_info')

with open('wodconnect.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['type','name','The workout']
    csv_writer.writerow(headers)

    for wd in wods:
        #title = wd.find(class_='metcon name').get_text().replace('High Camp; ','').replace('High Camp: ','')
        title = wd.find(class_='name').find('a').get_text()
        wodtype = wd.find(class_='item_type_badge').get_text()
        description = wd.find(class_='markdown_content').get_text().replace('“',"'").replace('”',"'")
        csv_writer.writerow([wodtype,title,description])
        #print(title)
        #print(wodtype)
        #print (description)
        #print('--------------------')

