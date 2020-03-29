import os
from PyQt5.QtCore import QUrl
from Text_html import *
from Trans_fuc import *

def Trans_process(self):
    Trans_text = Main_Translate('auto',self.on_comboBox_currentIndexChanged(),self.Search_text.text())
    main_trans = Trans_main_html(Trans_text)
    sy_html(Trans_text[3])
    return [Trans_text,main_trans]

def Trans_process_s(self):
    Trans_text_s = Main_Translate('auto',self.on_comboBox2_currentIndexChanged(),self.textEdit.toPlainText())
    main_trans = Trans_main_html(Trans_text_s)
    return [Trans_text_s,main_trans]

def Html_IO():
    Html_Url1 = str(os.path.abspath('./Trans_html/qbit1.html')).replace('\\','/')
    Html_Url2 = str(os.path.abspath('./Trans_html/qbit2.html')).replace('\\','/')
    return [Html_Url1,Html_Url2]

def Html_IO_s():
    Html_Url = str(os.path.abspath('./Trans_html/qbit1.html')).replace('\\','/')
    return Html_Url

def Html_Set(self,Trans_text,Html_Url1,Html_Url2):
    self.MeanText.load(QUrl(Html_Url1))
    self.syText.load(QUrl(Html_Url2))

def Html_Set_s(self,Trans_text_s,Html_Url):
    self.MeanText_2.load(QUrl(Html_Url))

def Html_Clear(self):
    self.MeanText.load(QUrl('about:blank'))
    self.syText.load(QUrl('about:blank'))

def Html_Clear_s(self):
    self.MeanText_2.load(QUrl('about:blank'))

def Tempfile_Del():
    try:
        for filename in os.listdir('./temp_audio'):
            os.remove('./temp_audio/'+filename)
    except FileNotFoundError as e:
        print(e)

def auto_change(self):
    if(len(self.Search_text.text())==0):
        return 1
    if(is_all_chinese(self.Search_text.text()) and self.comboBox.currentIndex()<2):
        self.comboBox.setCurrentIndex(1)
    elif(self.comboBox.currentIndex()<2):
        self.comboBox.setCurrentIndex(0)

