from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">The subtitle</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

#this returns the text in h1
print(simple_soup.find('h1'))

#find only the contents of the h1 tag
print(simple_soup.find('h1').string)

#create a function to find the title in html
def find_title():
    print(simple_soup.find('h1').string)

#function to find the items in a list. find_all method finds all occurances
def find_list_item():
    list_items = simple_soup.find_all('li')
    #assigns varable list contents and uses string method to iterate over items in list
    list_contents = [e.string for e in list_items]
    print(list_contents)

#define a function to find a subtile
def find_paragraph():
    print(simple_soup.find('p', {'class': 'subtitle'}).string)

find_paragraph()

#find all the <p> taggs but remove the subtitle class

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class') ]
    print (other_paragraph[0].string)


find_title()
find_list_item()
find_paragraph()
find_other_paragraph()