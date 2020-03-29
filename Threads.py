from PyQt5.Qt import QThread
from Update import *
from Voice_Api import Voice
from UI import *

class Update_Thread(QThread):  # 更新检测线程
    def __init__(self,choice):
        super(Update_Thread,self).__init__()
        self.choice = choice

    def run(self):
        update_check(self.choice)

class Voice_Thread(QThread):  # 更新检测线程
    def __init__(self,Trans_RList):
        super(Voice_Thread,self).__init__()
        self.Trans_RList = Trans_RList

    def run(self):
        Voice(self.Trans_RList)
        




