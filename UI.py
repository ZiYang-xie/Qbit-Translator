from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Lang import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.setFixedSize(self.width(), self.height())
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        
        self.Search_button = QtWidgets.QPushButton(MainWindow)
        self.Search_button.setGeometry(QtCore.QRect(360, 70, 91, 31))
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
        self.tabWidget.setGeometry(QtCore.QRect(20, 120, 441, 201))
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
        # 翻译框 #
        self.MeanText = QWebEngineView(self.tab)
        self.MeanText.setGeometry(QtCore.QRect(10, 10, 401, 161))
        self.MeanText.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.MeanText.setObjectName("MeanText")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # 近义词框 #
        self.syText = QWebEngineView(self.tab_2)
        self.syText.setGeometry(QtCore.QRect(10, 10, 401, 161))
        self.syText.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.syText.setObjectName("syText")
        self.tabWidget.addTab(self.tab_2, "")
        # 语言框 #
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(358, 113, 91, 21))
        self.comboBox.setStyleSheet("")
        self.comboBox.addItems(list(lang_dict.keys()))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(300, 115, 51, 21))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Search_text = QtWidgets.QLineEdit(MainWindow)
        self.Search_text.setGeometry(QtCore.QRect(20, 62, 440, 45))
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
        # 最小化按钮 #
        self.Mini = QtWidgets.QPushButton(MainWindow)
        self.Mini.setGeometry(QtCore.QRect(425, 10, 20, 20))
        self.Mini.setStyleSheet('QPushButton{border-image:url(img/window_button/minimize_main.png)}QPushButton:hover{border-image:url(img/window_button/minimize_hover.png)}')
        self.Mini.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("Mini")

        # 关闭按钮 #
        self.Close = QtWidgets.QPushButton(MainWindow)
        self.Close.setGeometry(QtCore.QRect(450, 10, 20, 20))
        self.Close.setStyleSheet('QPushButton{border-image:url(img/window_button/close_main.png)}QPushButton:hover{border-image:url(img/window_button/close_hover.png)}')
        self.Close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("Close")

#------------------------| 句子翻译 |----------------------------------#
        # Frame #
        self.stc_trans_frame = QtWidgets.QFrame(MainWindow)
        self.stc_trans_frame.setGeometry(QtCore.QRect(-10, 40, 481, 301))
        self.stc_trans_frame.setStyleSheet("#stc_trans_frame:{background-color: rgb(235,235,235,0);}")
        self.stc_trans_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stc_trans_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stc_trans_frame.setVisible(False)
        self.stc_trans_frame.setObjectName("stc_trans_frame")
        # 句子翻译输入框 #
        self.textEdit = QtWidgets.QPlainTextEdit(self.stc_trans_frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 440, 100))
        self.textEdit.setStyleSheet('background-color: rgb(235,235,235);border-radius:6px;')
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        
        # 句子释义框 #
        self.MeanText_2 = QWebEngineView(self.stc_trans_frame)
        self.MeanText_2.setGeometry(QtCore.QRect(40, 160, 425, 100))
        self.MeanText_2.setStyleSheet('background-color: rgb(255, 255, 255);border-radius:4px;')
        self.MeanText_2.setObjectName("MeanText_2")

        # 句子翻译按钮 #
        self.Search_button_s = QtWidgets.QPushButton(self.stc_trans_frame)
        self.Search_button_s.setGeometry(QtCore.QRect(30, 120, 440, 38))
        self.Search_button_s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_button_s.setStyleSheet("QPushButton{\n"
"    background-color: rgb(100, 164, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(120, 184, 255);\n"
"}")
        self.Search_button_s.setShortcut('enter')
        self.Search_button_s.setObjectName("Search_button_s")

        # 语言框 #
        self.comboBox2 = QtWidgets.QComboBox(self.stc_trans_frame)
        self.comboBox2.setGeometry(QtCore.QRect(338, 128, 101, 22))
        self.comboBox2.setStyleSheet('background-color: rgb(255, 255, 255,255);')
        self.comboBox2.setStyleSheet("")
        self.comboBox2.addItems(list(lang_dict.keys()))
        self.comboBox2.setObjectName("comboBox2")

        self.Search_text.raise_()
        self.Search_button.raise_()
        self.tabWidget.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.stc_trans_frame.raise_()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小Q翻译器-Beta-V0.0.3-preview"))
        self.Search_button.setText(_translate("MainWindow", "查   询"))
        self.Search_button_s.setText(_translate("MainWindow", "查   询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   释义   "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "近义词"))
        self.label.setText(_translate("MainWindow", "翻译模式"))
        self.Search_text.setPlaceholderText(_translate("MainWindow", " 请输入您要查询的内容"))

    #--------|设置图标|--------#
    def setIcon(self, MainWindow):
        icon = QtGui.QIcon()  #设置图标
        icon.addPixmap(QtGui.QPixmap("Qbit_logo_trans.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon) 
    
    #--------|设置窗口|--------#
    def setBackground(self, MainWindow):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #无边框
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground) #设置窗口透明
    def drawShadow(self,painter): #绘制阴影
        #绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        self.SHADOW_WIDTH=6
        self.pixmaps=list()
        self.pixmaps.append(str("./img/shadow/left_top.png"))
        self.pixmaps.append(str("./img/shadow/left_bottom.png"))
        self.pixmaps.append(str("./img/shadow/right_top.png"))
        self.pixmaps.append(str("./img/shadow/right_bottom.png"))
        self.pixmaps.append(str("./img/shadow/top_mid.png"))
        self.pixmaps.append(str("./img/shadow/bottom_mid.png"))
        self.pixmaps.append(str("./img/shadow/left_mid.png"))
        self.pixmaps.append(str("./img/shadow/right_mid.png"))
        
        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[0]))   #左上角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[2]))   #右上角
        painter.drawPixmap(0,self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[1]))   #左下角
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[3]))  #右下角
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH)) #左
        painter.drawPixmap(self.width()-self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH, self.height()- 2*self.SHADOW_WIDTH)) #右
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[4]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH)) #上
        painter.drawPixmap(self.SHADOW_WIDTH, self.height()-self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH, QtGui.QPixmap(self.pixmaps[5]).scaled(self.width()-2*self.SHADOW_WIDTH, self.SHADOW_WIDTH))   #下

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.drawShadow(painter)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawPixmap(0, 0, 480, 340, QtGui.QPixmap("img/Background.png")) #设置背景
        painter.drawRect(QtCore.QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width()-2*self.SHADOW_WIDTH, self.height()-2*self.SHADOW_WIDTH))


    #--------|检查更新模块|--------#
    def update_message(self, MainWindow):
        self.update_message = QtWidgets.QMessageBox(MainWindow)
        choice =self.update_message.question(None, "检查更新-Update_Check","有最新的版本更新，请检查更新。"+"\n"+"There is new version released,Please check.",self.update_message.Ok | self.update_message.Cancel)
        self.update_message.setObjectName("update_message")
        return choice

    #--------|鼠标拖动|--------#
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            #self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标
            
    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        #self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


