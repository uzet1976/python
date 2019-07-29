from bs4 import BeautifulSoup

html_doc=""";
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>


<div id="section1">
    <h2>Test section1</h2>
    <img src="http://www.walla.co.il/logo.png">
    <p>Lorem Ipsom</p>
</div>

<div id="section1">
    <h2>Test section2</h2>
    <ul>
        <li class="item"><a href="#">item1</li>
        <li class="item"><a href="#">item2</li>
        <li class="item"><a href="#">item3</li>
        <li class="item"><a href="#">item4</li>
    </ul>
</div>
</body>
</html>

"""

soup = BeautifulSoup(html_doc,'html.parser')

#Direct
#print(soup.body)
#find
#el = soup.findAll('div')


#select
#el = soup.select("#section1")
#el = soup.select("#section1")[0]

#get_text
#el = soup.find(class_='item').get_text()

#for item in soup.select('.item'):
#    print(item.get_text())
el = soup.body.contents[7].contents[3]
print (el)