import json
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys


with open('nk_api.json', 'r') as openfile:
    json_read = json.load(openfile)

with open('nk_api_info.json', 'r') as openfile_links:
    json_read_info = json.load(openfile_links)



def nuke_info(word):
    for i in json_read_info:
        try:
            return i[word]
        except:
            pass

class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()


        self.layout = QVBoxLayout()
        self.font = QFont()
        self.font.setPointSize(15)
        self.font.setItalic(True)

        self.lineEdit = QLineEdit()
        self.textEdit = QTextEdit()
        self.textEdit.setWordWrapMode(QTextOption.WordWrap)
        self.checkBox = QCheckBox('filter_startswith')


        self.completer =QCompleter(json_read)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.popup().setFont(self.font)
        self.completer.popup().setAlternatingRowColors(True)
        self.completer.popup().setStyleSheet("color: rgba(144, 100, 134,255);")
        self.lineEdit.setCompleter(self.completer)
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


        tx_font = self.lineEdit.font()
        tx_font.setPointSize(15)

        self.textEdit.setFont(tx_font)
        self.layout.addWidget(self.checkBox)
        self.layout.addWidget(self.lineEdit)


        self.setLayout(self.layout)
        self.setMinimumWidth(800)
        self.setMinimumHeight(200)
        self.setWindowTitle('Nuke API Searcher')

        self.lineEdit.returnPressed.connect(self.lala)
        self.checkBox.stateChanged.connect(self.comb_box_click)

    def lala(self):
        var = str(self.lineEdit.text())
        self.layout.addWidget(self.textEdit)
        # self.textEdit.setText(information(without_bra))

        self.textEdit.document().setPlainText(nuke_info(var))

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
        self.setMaximumHeight(700)

    def comb_box_click(self):
        if self.checkBox.isChecked():
            self.completer.setFilterMode(Qt.MatchStartsWith)
        else:
            self.completer.setFilterMode(Qt.MatchContains)


app = QApplication(sys.argv)
panel = Panel()
panel.show()
sys.exit(app.exec_())





