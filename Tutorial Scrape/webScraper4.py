# import os
# import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QUrl, QEventLoop
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
# from bs4 import BeautifulSoup
# import requests


# class Client(QWebEnginePage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebEnginePage.__init__(self)
#         self.loadFinished.connect(self._loadFinished)
#         self.load(QUrl(url))
#         self.app.exec_()

#     def _loadFinished(self):
#         self.app.quit()


# url = 'https://pythonprogramming.net/parsememcparseface/'
# client_response = Client(url)

# #I think the issue is here at LINE 26
# source = client_response.mainFrame().toHtml()

# soup = BeautifulSoup(source, "html.parser")
# js_test = soup.find('p', class_='jstest')
# print(js_test.text)


import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

app = None

class Page(QWebEnginePage):
    def __init__(self, url):
        # self.app = QApplication(sys.argv)
        global app
        app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        # self.app.exec_()
        app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        # self.app.quit()
        global app 
        app.quit()


def main():
    page = Page('https://pythonprogramming.net/parsememcparseface/')
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('p', class_='jstest')
    print (js_test.text)
    print(__name__)

if __name__ == '__main__': main()