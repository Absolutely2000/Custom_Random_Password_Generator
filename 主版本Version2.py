#使用ttk模块创建GUI
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import secrets
import pyperclip

# 定义可选的字符集
# digits = "0123456789"
# lowercase = "abcdefghijklmnopqrstuvwxyz"
# uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# symbols = "!@#$%^&*()_+-=[{]}|;:,./<>?"

#创建窗口
root = tkinter.Tk()
root.title("密码生成器")
root.geometry("240x200")

c1=tkinter.IntVar()#生成整型变量
c1.set(0)#变量初始化
c2=tkinter.IntVar()#生成整型变量
c2.set(0)#变量初始化
c3=tkinter.IntVar()#生成整型变量
c3.set(0)#变量初始化
c4=tkinter.IntVar()#生成整型变量
c4.set(0)#变量初始化

check1=ttk.Checkbutton(root,text="数字",variable=c1,onvalue=1,offvalue=0)#创建复选框，设置复选框显示的文本，复选框关联的变量，设置未选中时的变量值，设置未选中时的变量值
check1.pack()
check2=ttk.Checkbutton(root,text="小写字母",variable=c2,onvalue=1,offvalue=0)#创建复选框，设置复选框显示的文本，复选框关联的变量，设置未选中时的变量值，设置未选中时的变量值
check2.pack()
check3=ttk.Checkbutton(root,text="大写字母",variable=c3,onvalue=1,offvalue=0)#创建复选框，设置复选框显示的文本，复选框关联的变量，设置未选中时的变量值，设置未选中时的变量值
check3.pack()
check4=ttk.Checkbutton(root,text="特殊符号",variable=c4,onvalue=1,offvalue=0)#创建复选框，设置复选框显示的文本，复选框关联的变量，设置未选中时的变量值，设置未选中时的变量值
check4.pack()

#创建密码长度询问框
label1 = ttk.Label(root, text="密码长度 ：")
label1.pack()
entry1 = ttk.Entry(root)
entry1.pack()
length=1

#创建生成密码的函数
def main_func():
    charset = ""
    value1=c1.get()
    value2=c2.get()
    value3=c3.get()
    value4=c4.get()
    # tkinter.messagebox.showinfo(value1)
    if value1 == 0 and value2 == 0 and value3 == 0 and value4 == 0:
        tkinter.messagebox.showinfo("提示","请至少选择一种字符类型")
        return
    if value1 == 1:
        charset += "0123456789"
    if value2 == 1:
        charset += "abcdefghijklmnopqrstuvwxyz"
    if value3 == 1:
        charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if value4 == 1:
        charset += "!@#$%^&*()_+-=[{]}|;:,./<>?"
    # text_length_a=entry1.get()
    password = ""
    # tkinter.messagebox.showinfo(charset,text_length_a)
    try:
        text_length_a = int(entry1.get())
        if text_length_a>0:
            for i in range(text_length_a):
                password += secrets.choice(charset)
            pyperclip.copy(password)
            tkinter.messagebox.showinfo("密码",f"按照您的要求已生成以下密码：\n{password}\n并且已经复制到剪贴板")
        else:
            tkinter.messagebox.showinfo("提示","密码长度必须大于0")
    except:
        tkinter.messagebox.showinfo("提示","输入的不是数字，请重新输入")
    # if type(text_length_a)==int:
    #     if int(text_length_a)>0:
    #         for i in range(int(text_length_a)):
    #             password += secrets.choice(charset)
    #             tkinter.messagebox.showinfo("密码",password)
    #     else:
    #         tkinter.messagebox.showinfo("提示","密码长度必须大于0")
    # else:  
    #     tkinter.messagebox.showinfo("提示","输入的不是数字，请重新输入")
    # return
#创建生成按钮
button_main = ttk.Button(root,text="生成（可重复生成）",command=main_func)
button_main.pack(side=BOTTOM)

root.mainloop()