import requests
from bs4 import BeautifulSoup
from csv import writer

urls = ['https://www.wodconnect.com/workout_lists','https://www.wodconnect.com/workout_lists?page=2','https://www.wodconnect.com/workout_lists?page=3','https://www.wodconnect.com/workout_lists?page=4','https://www.wodconnect.com/workout_lists?page=5','https://www.wodconnect.com/workout_lists?page=6','https://www.wodconnect.com/workout_lists?page=7','https://www.wodconnect.com/workout_lists?page=8','https://www.wodconnect.com/workout_lists?page=9','https://www.wodconnect.com/workout_lists?page=10','https://www.wodconnect.com/workout_lists?page=11','https://www.wodconnect.com/workout_lists?page=12','https://www.wodconnect.com/workout_lists?page=13','https://www.wodconnect.com/workout_lists?page=14','https://www.wodconnect.com/workout_lists?page=15','https://www.wodconnect.com/workout_lists?page=16','https://www.wodconnect.com/workout_lists?page=17','https://www.wodconnect.com/workout_lists?page=18','https://www.wodconnect.com/workout_lists?page=19','https://www.wodconnect.com/workout_lists?page=20','https://www.wodconnect.com/workout_lists?page=21','https://www.wodconnect.com/workout_lists?page=22','https://www.wodconnect.com/workout_lists?page=23']

with open('wodconnect.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Type','Name','The workout','Url']
    csv_writer.writerow(headers)

    for url in urls:
        response = requests.get(url)
        wods_page_soup = BeautifulSoup(response.text,'html.parser')
        wods_page_urls = wods_page_soup.find_all(class_="card")

        for url_link in wods_page_urls:
            tt="https://www.wodconnect.com"+url_link.find('a')["href"]
            print(tt)

            url = tt
            response = requests.get(url)

            soup = BeautifulSoup (response.text,'html.parser')
            wods = soup.find_all(class_='workout_info')

            for wd in wods:
                title = wd.find(class_='name').find('a').get_text()
                wodtype = wd.find(class_='item_type_badge').get_text()
                description = wd.find(class_='markdown_content').get_text().replace('“',"'").replace('”',"'").replace(' – ',' - ').replace('push ups','push-ups').replace('pull ups','pull-ups')
                csv_writer.writerow([wodtype,title,description,tt])