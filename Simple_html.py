from bs4 import BeautifulSoup

SIMPLE_HTML = ''<HTML>
<head></head>
<body>
<h1>This is a title</h1>
<p class = "subtitle>"sdfsdfsdfsdfsdfsdfsdfsdf</p>
<p>Another p withot a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>


simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

print(simple_soup.find('h1'))