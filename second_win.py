from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel, QLineEdit)

from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        '''окно в котором проводится опрос'''
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        '''graficheskie elementy'''
        self.btn_next = QPushButton(txt_sendresults)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.text_name = QLabel(text_name)