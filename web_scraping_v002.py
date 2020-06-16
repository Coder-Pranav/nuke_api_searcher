import requests
import urllib3.request
import time
from bs4 import BeautifulSoup
import re
import string
import json

alphabet_string = string.ascii_uppercase
# Create a string of all uppercase letters


alphabet_list = list(alphabet_string)
# Create a list of all uppercase letters

records = []
link_dict = {}
def parser():
    for alpha in alphabet_list:
        try:
            url = 'https://learn.foundry.com/nuke/developers/70/pythonreference/identifier-index-{}.html'.format(alpha)
        except:
            pass
        response = requests.get(url)
        # print response.text

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('td', attrs={'width': '33%', 'class': 'link-index'})

        # print len(results)

        first_result = results[0]
        first_result.find('a')
        first_result.find('a').text
        first_result.find('a')['href'] #gives the link to that knob



        # getting link for second result

        first_result.contents
        first_result.contents[3].find('a')['href']
        first_result.contents[3].find('a').text

        # records = []
        for result in results:
            try:
                knob = result.find('a').text
                module = result.contents[3].find('a').text
                link = result.find('a')['href']
                value = '{} ({})'.format(knob,module)

                linku = {value: link}
                link_dict.update(linku)
                print link
                records.append(str(link))
            except:
                pass
    json_list = json.dumps(records, indent=4)
    with open('nk_api_links.json','w') as f:
        f.write(json_list)





with open('nk_api.json', 'r') as openfile:
    json_read = json.load(openfile)


with open('nk_api_links.json', 'r') as openfile_links:
    json_read_links = json.load(openfile_links)

def goog(word):
    for i in json_read_links:
        if i.find(word) != -1:
            print i



def information(word):
    for ext in json_read_links:
        if ext.find(word) != -1:
            # print ext
            url = 'https://learn.foundry.com/nuke/developers/70/pythonreference/{}'.format(ext)
            print url
            response = requests.get(url)
            # print response.text

            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('td', attrs={"class": "summary"})
            for pikachu in results:
                if (pikachu.text.encode('utf-8')).find(word) != -1:
                    return pikachu.text.encode('utf-8').strip()








from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()


        self.layout = QVBoxLayout()
        self.font = QFont()
        self.font.setPointSize(15)
        self.font.setItalic(True)

        self.lineEdit = QLineEdit()
        self.textEdit = QTextEdit()


        completer =QCompleter(json_read)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.popup().setFont(self.font)
        completer.popup().setAlternatingRowColors(True)
        completer.popup().setStyleSheet("color: rgba(144, 100, 134,255);")
        self.lineEdit.setCompleter(completer)
        self.lineEdit.setTextMargins(50,50,50,50)
        f = self.lineEdit.font()
        f.setPointSize(27)
        self.lineEdit.setFont(f)
        self.lineEdit.setStyleSheet("margin: 2.5px; padding: 2.5px; \
                                 color: rgba(144, 170, 134,255); \
                                 border-style: solid; \
                                 border-radius: 10px; \
                                 border-width: 1px; \
                                 border-color: \
                                 rgba(144, 170, 134,255);")

        self.textEdit.setFont(f)
        self.layout.addWidget(self.lineEdit)
        # self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)
        self.setMinimumWidth(800)
        self.setMinimumHeight(200)
        self.setWindowTitle('Nuke API Searcher')

        self.lineEdit.returnPressed.connect(self.lala)

    def lala(self):
        var = str(self.lineEdit.text()).split(' ')
        # print var[0]
        try:
            without_bra = var[0].replace('()', '')
        except:
            without_bra = var[0]
        self.layout.addWidget(self.textEdit)
        # self.textEdit.setText(information(without_bra))

        self.textEdit.document().setPlainText(information(without_bra))

        font = self.textEdit.document().defaultFont()
        fontMetrics = QFontMetrics(font)
        textSize = fontMetrics.size(0, self.textEdit.toPlainText())

        w = textSize.width() + 10
        h = textSize.height() + 10
        self.resize(800, h*3)
        if self.height() <= 300:
            self.resize(800, 300)
        else:
            pass
        self.textEdit.setReadOnly(True)

        # goog(without_bra)



app = QApplication(sys.argv)
panel = Panel()
panel.show()
sys.exit(app.exec_())



















# number = 21
# first_result = results[number]
# print first_result.contents
# # print first_result.contents[1].find_all('span',attrs={"class": "summary-sig-name"})
# for i in first_result.contents:
#     try:
#         print str(i.find('span',attrs={"class": "summary-sig-name"}).text)
#         if str(i.find('span',attrs={"class": "summary-sig-name"}).text).startswith(word):
#
#             print results[number].text
#     except:
#         pass




