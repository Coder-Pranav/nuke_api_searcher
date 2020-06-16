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
                records.append(value)
            except:
                pass

# parser()
# print link_dict
#     json_list = json.dumps(records, indent=4)
#     with open('nk_api.json','w') as f:
#         f.write(json_list)

# print records

with open('nk_api.json', 'r') as openfile:
    json_read = json.load(openfile)


from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()


        self.layout = QHBoxLayout()
        self.font = QFont()
        self.font.setPointSize(15)
        self.font.setItalic(True)

        self.lineEdit = QLineEdit()


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


        self.layout.addWidget(self.lineEdit)

        self.setLayout(self.layout)
        self.setMinimumWidth(800)
        self.setMinimumHeight(200)
        self.setWindowTitle('Nuke API Searcher')


app = QApplication(sys.argv)
panel = Panel()
panel.show()
sys.exit(app.exec_())