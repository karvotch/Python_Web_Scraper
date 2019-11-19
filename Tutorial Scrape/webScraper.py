import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# print(soup.title)

# print(soup.findAll('p'))

# for paragraph in soup.findAll('p'):
	# Better to use .text over .string because .text returns unicode as opposed to .string that returns "navigable string"
	# print(paragraph)
	# print(paragraph.string)
	# print(paragraph.text)

# print(soup.getText())


for url in soup.findAll('a'):
	# Get the whole a tag.
	# print(url)
	# Get text of all links.
	# print(url.text)
	# Get the links in each a tag
	print(url.get('href'))

