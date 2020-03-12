from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from function import *
from UI import *
from lang import *
from update import *
import webbrowser

class myWin(QtWidgets.QWidget, Ui_MainWindow):
    # UI初始化 #
    def __init__(self):
        super(myWin, self).__init__()
        self.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Qbit_logo_trans.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(self.width(), self.height())
        # 检查更新判断 #
        if(update_check()):
            choice = self.update_message(self)
            if(choice == self.update_message.Ok):
                webbrowser.open(github_url)
        self.Search_text.returnPressed.connect(self.on_Search_button_clicked)
        self.Search_button.clicked.connect(self.on_Search_button_clicked)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

    # 按钮事件槽函数 #
    @QtCore.pyqtSlot()
    def on_Search_button_clicked(self):
        # 中英互译自动切换 #
        if(len(self.Search_text.text())==0):
            return 1
        if(is_all_chinese(self.Search_text.text()) and self.comboBox.currentIndex()<2):
            self.comboBox.setCurrentIndex(1)
        elif(self.comboBox.currentIndex()<2):
            self.comboBox.setCurrentIndex(0)
        # 翻译内容显示 #
        Trans_text = Main_Translate('auto',self.on_comboBox_currentIndexChanged(),self.Search_text.text())
        if isinstance(Trans_text,int):
            self.MeanText.setPlainText('网络异常请稍后重试')
        if isinstance(Trans_text,list):    
            self.MeanText.setPlainText(Trans_text[0])
            self.syText.setPlainText(Trans_text[1])
        if isinstance(Trans_text,str): 
            self.MeanText.setPlainText(Trans_text)
            self.syText.setPlainText('')

    # 下拉框槽函数 #
    @QtCore.pyqtSlot()
    def on_comboBox_currentIndexChanged(self):
        # 更改翻译模式 #
        for key in lang_dict:
            if(self.comboBox.currentText() == key):
                return lang_dict[key]
            
# 启动主窗口 #
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    Widget=myWin()
    Widget.show()
    sys.exit(app.exec_())


