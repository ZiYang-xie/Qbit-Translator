# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\代码\version1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from lang import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Search_button = QtWidgets.QPushButton(MainWindow)
        self.Search_button.setGeometry(QtCore.QRect(360, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Search_button.setFont(font)
        self.Search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_button.setMouseTracking(False)
        self.Search_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(26, 164, 255);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:8px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(128, 194, 255);\n"
"}")
        self.Search_button.setAutoDefault(True)
        self.Search_button.setDefault(False)
        self.Search_button.setFlat(False)
        self.Search_button.setShortcut('enter')
        self.Search_button.setObjectName("Search_button")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 441, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane /* The tab widget frame */  \n"
"{\n"
"    top:20px;\n"
"    border:none;\n"
"}\n"
"QTabBar::tab:first        /*第一个页面上面的标签tab*/\n"
"{\n"
"    color:#333333;\n"
"    background:transparent;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:14px;\n"
"    padding-left:-9px;\n"
"    padding-right:-9px;\n"
"    width:105px;\n"
"    height:30px;\n"
"    margin-left:10px;\n"
"    margin-right:40px;\n"
"}\n"
"QTabBar::tab:last        /*最后一个页面上面的标签tab*/\n"
"{\n"
"    color:#333333;\n"
"    background:transparent;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:14px;\n"
"    padding-left:-9px;\n"
"    padding-right:-9px;\n"
"    width:95px;\n"
"    height:30px;\n"
"    margin-left:10px;\n"
"    margin-right:40px;\n"
"}\n"
"QTabBar::tab:selected,QTabBar::tab:hover\n"
"{\n"
"    color:#618BE5;\n"
"    background:transparent;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:14px;\n"
"    border-bottom:2px solid #618BE5;\n"
"}\n"
"QTabBar{\n"
"    color:#618BE5;\n"
"    background:transparent;\n"
"    font-family:\"微软雅黑\";\n"
"    font-size:14px;\n"
"}\n"
"QTabWidget::tab-bar {          /*整个最上面的tab栏*/\n"
"    alignment: left;  \n"
"    top:2px;\n"
"    left:10px;\n"
"} \n"
"#detailWgt, #appealReasonWgt    /*设置下面的单个widget没有边框*/\n"
"{\n"
"    border:none;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.MeanText = QtWidgets.QPlainTextEdit(self.tab)
        self.MeanText.setGeometry(QtCore.QRect(10, 10, 401, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MeanText.sizePolicy().hasHeightForWidth())
        self.MeanText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MeanText.setFont(font)
        self.MeanText.setTabletTracking(True)
        self.MeanText.setAutoFillBackground(False)
        self.MeanText.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.MeanText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MeanText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MeanText.setLineWidth(0)
        self.MeanText.setTabChangesFocus(True)
        self.MeanText.setDocumentTitle("")
        self.MeanText.setReadOnly(True)
        self.MeanText.setPlainText("")
        self.MeanText.setOverwriteMode(False)
        self.MeanText.setBackgroundVisible(False)
        self.MeanText.setCenterOnScroll(False)
        self.MeanText.setPlaceholderText("")
        self.MeanText.setObjectName("MeanText")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.syText = QtWidgets.QPlainTextEdit(self.tab_2)
        self.syText.setGeometry(QtCore.QRect(10, 10, 401, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.syText.sizePolicy().hasHeightForWidth())
        self.syText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.syText.setFont(font)
        self.syText.setTabletTracking(True)
        self.syText.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.syText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.syText.setLineWidth(0)
        self.syText.setReadOnly(True)
        self.syText.setPlainText("")
        self.syText.setBackgroundVisible(False)
        self.syText.setObjectName("syText")
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(358, 73, 91, 21))
        self.comboBox.setStyleSheet("")
        self.comboBox.addItems(list(lang_dict.keys()))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(300, 75, 51, 21))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Search_text = QtWidgets.QLineEdit(MainWindow)
        self.Search_text.setGeometry(QtCore.QRect(20, 20, 441, 50))
        self.Search_text.setMaximumSize(QtCore.QSize(600, 50))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.Search_text.setFont(font)
        self.Search_text.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(235, 235, 235);\n"
"    border-radius:6px\n"
"}")
        self.Search_text.setFrame(False)
        self.Search_text.setObjectName("Search_text")
        self.Search_text.raise_()
        self.Search_button.raise_()
        self.tabWidget.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小Q开源翻译器-Beta-V1"))
        self.Search_button.setText(_translate("MainWindow", "查   询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   释义   "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "近义词"))
        self.label.setText(_translate("MainWindow", "翻译模式"))
        self.Search_text.setPlaceholderText(_translate("MainWindow", " 请输入您要查询的内容"))

    def update_message(self, MainWindow):
        self.update_message = QtWidgets.QMessageBox(MainWindow)
        choice =self.update_message.question(None, "检查更新-Update_Check","有最新的版本更新，请检查更新。"+"\n"+"There is new version released,Please check.",self.update_message.Ok | self.update_message.Cancel)
        self.update_message.setObjectName("update_message")
        return choice
