# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class FinalWin(QWidget):
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
        self.index=QLabel(txt_index)
        self.workheart=QLabel(txt_workheart)
        self.m_Line=QVBoxLayout()
        self.m_Line.addWidget(self.index,alignment=Qt.AlignCenter)
        self.m_Line.addWidget(self.workheart,alignment=Qt.AlignCenter)
        self.setLayout(self.m_Line)

    def connects(self):
        pass

    def next_click(self):
        pass
