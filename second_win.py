# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

from instr import *
#from my_app import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(winTitle)
        self.resize(win_width,win_height)
        self.move(300,300)
    def initUI(self):
        pass
        # self.helo_txt = QLabel(txt_hello)
        # self.instruction=QLabel(txt_instruction)
        # self.button = QPushButton(txt_next)

        # self.VLayout = QVBoxLayout()
        # self.VLayout.addWidget(self.helo_txt)
        # self.VLayout.addWidget(self.instruction)
        # self.VLayout.addWidget(self.button)

        # self.setLayout(self.VLayout)




    def connects(self):
        pass
        # self.button.clicked.connect(self.next_click)

    def next_click(self):
        pass
        # self.hide()
        # self.tw = TestWin()

