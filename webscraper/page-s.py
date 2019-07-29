import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://www.bazekalim.com/archive/')
soup = BeautifulSoup(response.text,'html.parser')

articles = soup.find_all(class_='postpic')

with open('posts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','Link']
    csv_writer.writerow(headers)

    for post in articles:
        title=post.find_all('a')[1].get_text()
        link = post.find_all('a')[1]['href']
        #print(title,link)
        csv_writer.writerow([title,link])
