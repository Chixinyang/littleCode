#codinf:utf-8
from tkinter import *
import tkinter.messagebox as messagebox
import baidufanyi

__author__= "Chixinyang"

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='获取中文结果', command=self.gotrans)
        self.alertButton.pack()
        self.transresult = Text(self,height=2,width=20)
        self.transresult.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

    def gotrans(self):
        name = self.nameInput.get() or '输入为空'
        result = baidufanyi.translater(name)
       # messagebox.showinfo('Message', "翻译结果为 ：{1}".format(result))
        self.transresult.insert(END,result)

app = Application()
# 设置窗口标题:
app.master.title('电子词典')
# 主消息循环:
app.mainloop()