# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import matplotlib
matplotlib.use("Qt5Agg")  # declare using QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
import tweepytextblob


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1499, 760)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(420, 0, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label1.setFont(font)
        self.label1.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet('''
                                      QLabel{border:none;color:white;}
                                      QLabel#left_label{
                                          border:none;
                                          border-bottom:1px solid white;
                                          font-size:18px;
                                          font-weight:700;
                                          font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                      }
                                  ''')
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 411, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('''
                                    QLabel{border:none;color:white;}
                                    QLabel#left_label{
                                        border:none;
                                        border-bottom:1px solid white;
                                        font-size:18px;
                                        font-weight:700;
                                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                                    }
                                ''')
        self.pushButton_Go = QtWidgets.QPushButton(Form)
        self.pushButton_Go.setGeometry(QtCore.QRect(1140, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_Go.setFont(font)
        self.pushButton_Go.setObjectName("pushButton_Go")
        self.pushButton_Go.setStyleSheet(''' 
                                     QPushButton
                                     {text-align : center;
                                     background-color : white;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     QPushButton:pressed
                                     {text-align : center;
                                     background-color : light gray;
                                     font: bold;
                                     border-color: gray;
                                     border-width: 2px;
                                     border-radius: 10px;
                                     padding: 6px;
                                     height : 14px;
                                     border-style: outset;
                                     font : 14px;}
                                     ''')

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 190, 1341, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_SP = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SP.sizePolicy().hasHeightForWidth())
        self.pushButton_SP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_SP.setFont(font)
        self.pushButton_SP.setObjectName("pushButton_SP")
        self.pushButton_SP.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
        self.horizontalLayout.addWidget(self.pushButton_SP)
        self.pushButton_P = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_P.sizePolicy().hasHeightForWidth())
        self.pushButton_P.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_P.setFont(font)
        self.pushButton_P.setObjectName("pushButton_P")
        self.pushButton_P.setStyleSheet('''
                    QPushButton{border:none;color:white;}
                    QPushButton#left_label{
                        border:none;
                        border-bottom:1px solid white;
                        font-size:18px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                ''')
        self.horizontalLayout.addWidget(self.pushButton_P)
        self.pushButton_Neu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Neu.sizePolicy().hasHeightForWidth())
        self.pushButton_Neu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_Neu.setFont(font)
        self.pushButton_Neu.setObjectName("pushButton_Neu")
        self.pushButton_Neu.setStyleSheet('''
                            QPushButton{border:none;color:white;}
                            QPushButton#left_label{
                                border:none;
                                border-bottom:1px solid white;
                                font-size:18px;
                                font-weight:700;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                        ''')
        self.horizontalLayout.addWidget(self.pushButton_Neu)
        self.pushButton_N = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_N.sizePolicy().hasHeightForWidth())
        self.pushButton_N.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_N.setFont(font)
        self.pushButton_N.setObjectName("pushButton_N")
        self.pushButton_N.setStyleSheet('''
                            QPushButton{border:none;color:white;}
                            QPushButton#left_label{
                                border:none;
                                border-bottom:1px solid white;
                                font-size:18px;
                                font-weight:700;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                        ''')
        self.horizontalLayout.addWidget(self.pushButton_N)
        self.pushButton_SN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_SN.sizePolicy().hasHeightForWidth())
        self.pushButton_SN.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_SN.setFont(font)
        self.pushButton_SN.setObjectName("pushButton_SN")
        self.pushButton_SN.setStyleSheet('''
                            QPushButton{border:none;color:white;}
                            QPushButton#left_label{
                                border:none;
                                border-bottom:1px solid white;
                                font-size:18px;
                                font-weight:700;
                                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                            }
                            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                        ''')
        self.horizontalLayout.addWidget(self.pushButton_SN)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 300, 1341, 461))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_SP = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_SP.setFont(font)
        self.textBrowser_SP.setObjectName("textBrowser_SP")
        self.textBrowser_SP.setStyleSheet(''' 
                                             QTextBrowser
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 10px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.horizontalLayout_2.addWidget(self.textBrowser_SP)
        self.textBrowser_P = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_P.setFont(font)
        self.textBrowser_P.setObjectName("textBrowser_P")
        self.textBrowser_P.setStyleSheet(''' 
                                                     QTextBrowser
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        self.horizontalLayout_2.addWidget(self.textBrowser_P)
        self.textBrowser_Neu = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_Neu.setFont(font)
        self.textBrowser_Neu.setObjectName("textBrowser_Neu")
        self.textBrowser_Neu.setStyleSheet(''' 
                                                             QTextBrowser
                                                             {text-align : center;
                                                             background-color : white;
                                                             font: bold;
                                                             border-color: gray;
                                                             border-width: 2px;
                                                             border-radius: 10px;
                                                             padding: 6px;
                                                             height : 14px;
                                                             border-style: outset;
                                                             font : 14px;}
                                                             ''')
        self.horizontalLayout_2.addWidget(self.textBrowser_Neu)
        self.textBrowser_N = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_N.setFont(font)
        self.textBrowser_N.setObjectName("textBrowser_N")
        self.textBrowser_N.setStyleSheet(''' 
                                                                     QTextBrowser
                                                                     {text-align : center;
                                                                     background-color : white;
                                                                     font: bold;
                                                                     border-color: gray;
                                                                     border-width: 2px;
                                                                     border-radius: 10px;
                                                                     padding: 6px;
                                                                     height : 14px;
                                                                     border-style: outset;
                                                                     font : 14px;}
                                                                     ''')
        self.horizontalLayout_2.addWidget(self.textBrowser_N)
        self.textBrowser_SN = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_SN.setFont(font)
        self.textBrowser_SN.setObjectName("textBrowser_SN")
        self.textBrowser_SN.setStyleSheet(''' 
                                                                             QTextBrowser
                                                                             {text-align : center;
                                                                             background-color : white;
                                                                             font: bold;
                                                                             border-color: gray;
                                                                             border-width: 2px;
                                                                             border-radius: 10px;
                                                                             padding: 6px;
                                                                             height : 14px;
                                                                             border-style: outset;
                                                                             font : 14px;}
                                                                             ''')
        self.horizontalLayout_2.addWidget(self.textBrowser_SN)
        self.pushButton_Plot = QtWidgets.QPushButton(Form)
        self.pushButton_Plot.setGeometry(QtCore.QRect(870, 110, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_Plot.setFont(font)
        self.pushButton_Plot.setObjectName("pushButton_Plot")
        self.pushButton_Plot.setStyleSheet(''' 
                             QPushButton
                             {text-align : center;
                             background-color : white;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             QPushButton:pressed
                             {text-align : center;
                             background-color : light gray;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             ''')
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 110, 731, 51))
        self.lineEdit.setPlaceholderText("Type topics to search")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')


        self.retranslateUi(Form)
        self.pushButton_Go.clicked.connect(Form.go)
        self.pushButton_SP.clicked.connect(Form.show_SP)
        self.pushButton_P.clicked.connect(Form.show_P)
        self.pushButton_Neu.clicked.connect(Form.show_Neu)
        self.pushButton_N.clicked.connect(Form.show_N)
        self.pushButton_SN.clicked.connect(Form.show_SN)
        self.pushButton_Plot.clicked.connect(Form.plot)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.setWindowOpacity(0.9)  #set opacity of window
    # set window background transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  #hide window frame

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "Sentiment Analysis App"))
        self.label_2.setText(_translate("Form", "Search for something?"))
        self.pushButton_Go.setText(_translate("Form", "Go!"))
        self.pushButton_SP.setText(_translate("Form", "Strongly Positive"))
        self.pushButton_P.setText(_translate("Form", "Positive"))
        self.pushButton_Neu.setText(_translate("Form", "Neutral"))
        self.pushButton_N.setText(_translate("Form", "Negative"))
        self.pushButton_SN.setText(_translate("Form", "Stongly Negative"))
        self.pushButton_Plot.setText(_translate("Form", "Plot"))

from PyQt5 import QtWidgets
from ui_main import Ui_Form
from sptweets_wordcloud import Ui_Dialog
from ptweets_wordcloud import  Ui_Dialog2
from neutweets_wordcloud import  Ui_Dialog3
from ntweets_wordcloud import  Ui_Dialog4
from sntweets_wordcloud import  Ui_Dialog5

class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.child_dialog1 = MyDialog1(self)
        self.child_dialog2 = MyDialog2(self)
        self.child_dialog3 = MyDialog3(self)
        self.child_dialog4 = MyDialog4(self)
        self.child_dialog5 = MyDialog5(self)


    def go(self):
        shost = self.lineEdit.text()
        tweepytextblob.searchtweets(shost)
        tweepytextblob.stronglypos()
        tweepytextblob.pos()
        tweepytextblob.neg()
        tweepytextblob.neu()
        tweepytextblob.stronglyneg()
        self.textBrowser_SP.append(tweepytextblob.stronglypos()+"\n")
        self.textBrowser_P.append(tweepytextblob.pos()+"\n")
        self.textBrowser_Neu.append(tweepytextblob.neu()+"\n")
        self.textBrowser_N.append(tweepytextblob.neg()+"\n")
        self.textBrowser_SN.append(tweepytextblob.stronglyneg()+"\n")

    def trans_stopword(self):
        trans_stopwords = self.lineEdit.text()



    def show_SP(self):
        self.child_dialog1.show()

    def show_P(self):
        #self.textBrowser_P.append("positive")
        self.child_dialog2.show()

    def show_Neu(self):
        #self.textBrowser_Neu.append("neutral")
        self.child_dialog3.show()

    def show_N(self):
        #self.textBrowser_N.append("negative")
        self.child_dialog4.show()

    def show_SN(self):
        #self.textBrowser_SN.append("strongly negative")
        self.child_dialog5.show()


    def plot(self):

        labels = ['n', 'p', 'sp', 'neu', 'sn']
        sizes = [tweepytextblob.negper(), tweepytextblob.posper(), tweepytextblob.stronglypos_per(), tweepytextblob.neu_per(), tweepytextblob.stronglyneg_per()]
        colors = ['red', 'yellowgreen', 'lightskyblue', 'purple', 'brown', 'pink']
        explode = (0, 0, 0, 0, 0)
        patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                          labeldistance=1.1, autopct='%4.2f%%', shadow=False,
                                          startangle=90, pctdistance=0.6)
        for t in l_text:
            t.set_size = (30)
        for t in p_text:
            t.set_size = (20)
        plt.axis('equal')
        plt.legend()
        plt.show()

class MyDialog1(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, last_form):
        super(MyDialog1, self).__init__()
        self.setupUi(self)
        self.last_form = last_form

    def closall(self):
        self.close()
        self.last_form.close()

class MyDialog2(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self, last_form):
        super(MyDialog2, self).__init__()
        self.setupUi(self)
        self.last_form = last_form

    def closall(self):
        self.close()
        self.last_form.close()

class MyDialog3(QtWidgets.QDialog, Ui_Dialog3):
    def __init__(self, last_form):
        super(MyDialog3, self).__init__()
        self.setupUi(self)
        self.last_form = last_form

    def closeall(self):
        self.close()
        self.last_form.close()

class MyDialog4(QtWidgets.QDialog, Ui_Dialog4):
    def __init__(self, last_form):
        super(MyDialog4, self).__init__()
        self.setupUi(self)
        self.last_form = last_form

    def closeall(self):
        self.close()
        self.last_form.close()


class MyDialog5(QtWidgets.QDialog, Ui_Dialog5):
    def __init__(self, last_form):
        super(MyDialog5, self).__init__()
        self.setupUi(self)
        self.last_form = last_form

    def closeall(self):
        self.close()
        self.last_form.close()

if __name__ == "__main__":
    import sys
    #print(tweepytextblob.gosearch())
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
