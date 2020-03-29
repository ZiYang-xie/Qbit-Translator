from Threads import *
from Lang import *
from IO_fuc import *

def on_Win(app):
    MainWin=myWin()
    MainWin.show()
    sys.exit(app.exec_())

class myWin(QtWidgets.QWidget, Ui_MainWindow):
    m_flag = False
    m_Position = QtGui.QCursor.pos()
    # UI初始化 #
    def __init__(self):
        super(myWin, self).__init__()
        self.setupUi(self)
        self.setIcon(self)
        self.setBackground(self)
        # 检查更新判断 #
        self.update_check_Thread = Update_Thread(self.update_message)
        self.update_check_Thread.start()
        # 连接槽函数 #
        self.Search_text.returnPressed.connect(self.on_Search_button_clicked)
        self.Search_button.clicked.connect(self.on_Search_button_clicked)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)
        self.comboBox2.currentIndexChanged.connect(self.on_comboBox2_currentIndexChanged)
        self.Search_text.textChanged.connect(self.on_Search_text_textChanged)
        self.textEdit.textChanged.connect(self.on_textEdit_textChanged)
        self.Search_button_s.clicked.connect(self.Mean_2_Show)
        self.Mini.clicked.connect(self.Minimize)
        self.Close.clicked.connect(self.close)

    # 按钮事件槽函数 #
    @QtCore.pyqtSlot()
    def on_Search_button_clicked(self):
        if(self.Search_text.text()==''): return
        auto_change(self)
        Tempfile_Del()
        Trans_RList=Trans_process(self)
        Html_RList=Html_IO()
        Html_Set(self,Trans_RList[0],Html_RList[0],Html_RList[1])
        Voice(Trans_RList[1])

    # 下拉框1槽函数 #
    @QtCore.pyqtSlot()
    def on_comboBox_currentIndexChanged(self):
        # 更改翻译模式 #
        for key in lang_dict:
            if(self.comboBox.currentText() == key):
                return lang_dict[key]

    # 下拉框2槽函数 #
    @QtCore.pyqtSlot()
    def on_comboBox2_currentIndexChanged(self):
        # 更改翻译模式 #
        for key in lang_dict:
            if(self.comboBox2.currentText() == key):
                return lang_dict[key]

    # 输入框槽函数 #
    @QtCore.pyqtSlot()
    def on_Search_text_textChanged(self):
        if(len(self.Search_text.text())>= 20):
            self.textEdit.setPlainText(self.Search_text.text())
            self.textEdit.setFocus()
            self.textEdit.moveCursor(self.textEdit.textCursor().End)
            self.Search_text.setText('')
            Html_Clear(self)
            self.stc_trans_frame.setVisible(True)

    # 句子翻译框槽函数 #
    @QtCore.pyqtSlot()
    def on_textEdit_textChanged(self):
        if(len(self.textEdit.toPlainText()) < 18):
            self.Search_text.setText(self.textEdit.toPlainText())
            self.Search_text.setFocus()
            Html_Clear_s(self)
            self.stc_trans_frame.setVisible(False)

    # 句子释义框槽函数 #
    @QtCore.pyqtSlot()
    def Mean_2_Show(self):
        Tempfile_Del()
        Trans_RList=Trans_process_s(self)
        Html_s=Html_IO_s()
        Html_Set_s(self,Trans_RList[0],Html_s)
        Voice(Trans_RList[1])

    # 窗口最小化 #
    @QtCore.pyqtSlot()
    def Minimize(self):
        self.showMinimized()

    
        
            
# 启动主窗口 #
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    on_Win(app)
