import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# 	Not sure if I need to close since I never save urlopen as an object.
# urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').close()
soup = bs.BeautifulSoup(sauce, 'lxml')


nav = soup.nav

# print(nav)

# for url in nav.findAll('a'):
# 		Some websites might have duplicate code for nav bar for mobile users and pc users.
# 	print(url.get('href'))


body = soup.body

# for paragraph in body.findAll('p'):
# 	print(paragraph.text)

# for div in soup.findAll('div'):
# 	print(div.text)

# 	Finding a specific div to read.
# 		In this case we are looking for the div that is titled 'body'.
for div in soup.findAll('div', class_='body'):
	print(div.text)