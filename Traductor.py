from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from googletrans import Translator
from languages import *

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.button_click()

    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton('reverse')
        self.reset = QPushButton('reset')
        self.submit = QPushButton('Translate Now')
        self.input_option = QComboBox()
        self.output_option = QComboBox()

        self.input_option.addItems(values)
        self.output_option.addItems(values)

        self.title = QLabel('Translator')

        self.master = QHBoxLayout()

        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.reset)

        col2.addWidget(self.input_box)
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box)

        self.master.addLayout(col1, 20)
        self.master.addLayout(col2, 80)

        self.setLayout(self.master)

    def settings(self):
        self.setWindowTitle('Translator')
        self.setGeometry(250,250,600,500)

    def button_click(self):
        self.submit.clicked.connect(self.translate_click)
        self.reverse.clicked.connect(self.rev_click)
        self.reset.clicked.connect(self.reset_app)

    def translate_click(self):
        value_to_key1 = self.output_option.currentText()
        value_to_key2 = self.input_option.currentText()

        key_to_value1 = [k for k,v in LANGUAGES.items() if v == value_to_key1]
        key_to_value2 = [k for k,v in LANGUAGES.items() if v == value_to_key2]

        self.script = self.translate_text(self.input_box.toPlainText(), key_to_value1[0], key_to_value2[0])
        self.output_box.setText(self.script)

    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()

    def translate_text(self, text, dest_lang, src_lang):
        speaker = Translator()
        translation = speaker.translate(text, dest=dest_lang, src= src_lang)
        return translation.text
    
    def rev_click(self):
        s1, l1 = self.input_box.toPlainText(), self.input_option.currentText()
        s2, l2 = self.output_box.toPlainText(), self.output_option.currentText()
        
        self.input_box.setText(s2)
        self.output_box.setText(s1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)

if __name__ == '__main__':
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()