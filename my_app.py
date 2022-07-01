# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle(winTitle)
        self.resize(win_width,win_height)
        self.move(200,100)
    def initUI(self):
        self.helo_txt = QLabel(txt_hello)
        self.instruction=QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        self.VLayout = QVBoxLayout()
        self.VLayout.addWidget(self.helo_txt)
        self.VLayout.addWidget(self.instruction)
        self.VLayout.addWidget(self.button)

        self.setLayout(self.VLayout)




    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()


app=QApplication([])
main_win=MainWin()
app.exec_()
