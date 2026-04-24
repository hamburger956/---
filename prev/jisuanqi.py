#这是一个计算器程序
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os

#创建主窗口
root = tk.Tk()

#加载图片
image_1 = Image.open(r"D:\自己的项目\计算器\background.jpg")
image_1 = image_1.resize((319,292))
photo = ImageTk.PhotoImage(image_1)

#设置窗口参数
root.title("简单计算器")
root.geometry("560x296")
root.config(bg="#d4d4d4")
root.iconbitmap(r"D:\自己的项目\计算器\favicon.ico")
root.resizable(False,False)
stayle = ttk.Style()
stayle.theme_use("darkly")

#创建变量参数
num_show = tk.StringVar()

#创建容器记录数据
list_num = list()
list_record = [] #用来记录显示的数字的awa
list_fuhao = [] #用来记录符号的awa

#设置所有事件
#创建加号
def add():
    list_record.clear()
    list_fuhao.append('+')
    num_show.set(f"{''.join(list_fuhao)}")
    list_num.append('+')
#创建减号
def sub():
    list_record.clear()
    list_fuhao.append('-')
    num_show.set(f"{''.join(list_fuhao)}")
    list_num.append('-')
#创建乘号
def plus():
    list_record.clear()
    list_fuhao.append('x')
    num_show.set(f"{''.join(list_fuhao)}")
    list_num.append('*')
#创建除号
def div():
    list_record.clear()
    list_fuhao.append('÷')
    num_show.set(f"{''.join(list_fuhao)}")
    list_num.append('/')
    
#点
def point():
    list_fuhao.clear()
    list_record.append('.')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('.')

#等号
def eva():
    global list_num
    try:
        num_show.set(f'{str(eval(''.join(list_num))):.15}')
        list_num = [f'{eval(''.join(list_num))}']
        list_record.clear()
        list_fuhao.clear()
    except Exception:
        os.startfile("https://www.bilibili.com/video/BV1GJ411x7h7/")
        num_show.set(f'Error!')
        messagebox.showinfo(title="终于上当了",
                            message="彩蛋！",)

#数字
def one():
    list_fuhao.clear()
    list_record.append('1')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('1')

def two():
    list_fuhao.clear()
    list_record.append('2')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('2')

def three():
    list_fuhao.clear()
    list_record.append('3')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('3')

def four():
    list_fuhao.clear()
    list_record.append('4')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('4')

def five():
    list_fuhao.clear()
    list_record.append('5')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('5')

def six():
    list_fuhao.clear()
    list_record.append('6')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('6')

def senven():
    list_fuhao.clear()
    list_record.append('7')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('7')

def eight():
    list_fuhao.clear()
    list_record.append('8')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('8')

def nine():
    list_fuhao.clear()
    list_record.append('9')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('9')

def zero():
    list_fuhao.clear()
    list_record.append('0')
    num_show.set(f'{''.join(list_record)}')
    list_num.append('0')

#清空
def clear():
    num_show.set('')
    list_num.clear()
    list_record.clear()
    list_fuhao.clear()

#回退
def back():
    try:
        if list_fuhao:
            list_fuhao.pop(len(list_fuhao)-1)
            num_show.set(f"{''.join(list_fuhao)}")
        else:
            list_record.pop(len(list_record)-1)
            num_show.set(f'{''.join(list_record)}')
        list_num.pop(len(list_num)-1)
    except Exception:
        pass

#显示当前的计算式
def Ans():
    num_show.set(f"{''.join(list_num)}")

#创建标签
#显示框
show_labol = tk.Label(master=root,
                      bg="#d9eef9",
                      font=("黑体",20),
                      textvariable=num_show,
                      relief=tk.RIDGE,
                     )

#图片显示
image_labol = tk.Label(master=root,
                       image=photo,
                       bg = "#d9eef9")


#创建按钮

#运算按钮
btn_add = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=add,
                    text="+",
                    relief="groove")

btn_sub = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=sub,
                    text="-",
                    relief="groove")

btn_plus = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=plus,
                    text="x",
                    relief="groove")

btn_div = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=div,
                    text="÷",
                    relief="groove")

btn_eval = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=eva,
                    text="=",
                    relief="groove")

btn_point = tk.Button(master=root,
                      font=("黑体",20),
                      activebackground="#e7e5e5",
                      activeforeground="#000000",
                      bg="#ffefef",
                      command=point,
                      text=".",
                      relief="groove")

#数字按钮
btn_one = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=one,
                    text="1",
                    relief="groove")

btn_two = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=two,
                    text="2",
                    relief="groove")

btn_three = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=three,
                    text="3",
                    relief="groove")

btn_four = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=four,
                    text="4",
                    relief="groove")

btn_five = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=five,
                    text="5",
                    relief="groove")

btn_six = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=six,
                    text="6",
                    relief="groove")

btn_senven = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=senven,
                    text="7",
                    relief="groove")

btn_eight = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=eight,
                    text="8",
                    relief="groove")

btn_nine = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=nine,
                    text="9",
                    relief="groove")

btn_zero = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=zero,
                    text="0",
                    relief="groove")

#清空按钮
btn_clear = tk.Button(master=root,
                    font=("黑体",20),
                    activebackground="#e7e5e5",
                    activeforeground="#000000",
                    bg="#ffefef",
                    command=clear,
                    text="清空",
                    relief="groove")

#回退
btn_back =  tk.Button(master=root,
                      font=("黑体",20),
                      activebackground="#e7e5e5",
                      activeforeground="#000000",
                      bg="#ffefef",
                      command=back,
                      text="<-",
                      relief="groove")

#显示当前计算式
btn_Ans = tk.Button(master=root,
                      font=("黑体",20),
                      activebackground="#e7e5e5",
                      activeforeground="#000000",
                      bg="#ffefef",
                      command=Ans,
                      text="Ans",
                      relief="groove")

#设置布局

show_labol.grid(row=0,rowspan=1,column=0,columnspan=6,sticky='nwse')

btn_add.grid(row=1,rowspan=1,column=3,columnspan=2,sticky='nwse')
btn_sub.grid(row=2,rowspan=1,column=3,columnspan=2,sticky='nwse')
btn_plus.grid(row=3,rowspan=1,column=3,columnspan=2,sticky='nwse')
btn_div.grid(row=4,rowspan=1,column=3,columnspan=2,sticky='nwse')

btn_one.grid(row=1,rowspan=1,column=0,columnspan=1,sticky='nwse')
btn_two.grid(row=1,rowspan=1,column=1,columnspan=1,sticky='nwse')
btn_three.grid(row=1,rowspan=1,column=2,columnspan=1,sticky='nwse')
btn_four.grid(row=2,rowspan=1,column=0,columnspan=1,sticky='nwse')
btn_five.grid(row=2,rowspan=1,column=1,columnspan=1,sticky='nwse')
btn_six.grid(row=2,rowspan=1,column=2,columnspan=1,sticky='nwse')
btn_senven.grid(row=3,rowspan=1,column=0,columnspan=1,sticky='nwse')
btn_eight.grid(row=3,rowspan=1,column=1,columnspan=1,sticky='nwse')
btn_nine.grid(row=3,rowspan=1,column=2,columnspan=1,sticky='nwse')
btn_zero.grid(row=4,rowspan=1,column=0,columnspan=1,sticky='nwse')

btn_eval.grid(row=4,rowspan=1,column=2,columnspan=1,sticky='nwse')
btn_clear.grid(row=4,rowspan=1,column=1,columnspan=1,sticky='nwse')
btn_point.grid(row=3,rowspan=1,column=5,columnspan=1,sticky='nwse')
btn_back.grid(row=1,rowspan=2,column=5,columnspan=1,sticky='nwse')
btn_Ans.grid(row=4,rowspan=1,column=5,columnspan=1,sticky='nwse')

image_labol.grid(row=0,rowspan=5,column=6,columnspan=1,sticky='nwse')
#主窗口循环
root.mainloop()