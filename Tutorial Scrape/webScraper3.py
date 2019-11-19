import bs4 as bs
import urllib.request
import pandas as pd

# sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# # 	Not sure if I need to close since I never save urlopen as an object.
# # urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').close()
# soup = bs.BeautifulSoup(sauce, 'lxml')


# # table = soup.table
# table = soup.find('table')
# # print(table)

# table_rows = table.findAll('tr')

# for tr in table_rows:
# 	td = tr.findAll('td')
# 	row = [i.text for i in td]
# 	print(row)


# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
# for df in dfs:
# 	print(df)


# 	A xml file is usually used as a sitemap for a website (e.g. News website storing links to all articles in this neat xml file).
# 		A sitemap is just all the urls on the website.
# 	So if web scraping a news website for new articles, best to do it through the sitemap.
sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce, 'xml')


# 	Prints all links in the sitemap.
for url in soup.findAll('loc'):
	print(url.text)