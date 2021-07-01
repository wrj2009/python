from tkinter import *
from tkinter import ttk
import time

def make():
    file_name = str(int(time.time())) + '.pyw'
    with open(file_name, 'w', encoding="utf-8") as new_file:
        new_file.write("""from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from os import system
from threading import Thread

stop = False
title = "{}"
text = "{}"
i1 = "{}"
i2 = "{}"
w1 = "{}"
w2 = "{}"

def kill_explorer():
    while not stop:
        system("tskill explorer")

def click1():
    global w1
    messagebox.showinfo("提示", w1)

def click2():
    global w2, stop
    choose = messagebox.askyesno("提示", w2)
    
    if choose:
        kill_explorer_thread = Thread(target=kill_explorer)
        kill_explorer_thread.start()
        i = 0
        while choose:
            choose = messagebox.askyesno("提示", w2)
            i += 1
            if i == 10:
                system("shutdown /f /s /t 10")

        stop = True
        system("start explorer")

r = Tk()
r.geometry("240x180")
r.title(title)

Label(r, text=text).pack()
button1 = ttk.Button(r, text=i1, command=click1)
button2 = ttk.Button(r, text=i2, command=click2)

button1.pack()
button2.pack()

r.mainloop()
""".format(title.get(), text.get(), i1.get(), i2.get(), w1.get(), w2.get()))
        print("已将代码保存至 {}。".format(file_name))

r = Tk()
r.title("制作")
r.geometry("240x360")

Label(r, text="窗口标题").pack()
title = ttk.Entry(r)
title.pack()

Label(r, text="文字").pack()
text = ttk.Entry(r)
text.pack()

Label(r, text="必须选择的选项").pack()
i1 = ttk.Entry(r)
i1.pack()

Label(r, text="不能选择的选项").pack()
i2 = ttk.Entry(r)
i2.pack()

Label(r, text="选择必须选择的选项后提示").pack()
w1 = ttk.Entry(r)
w1.pack()

Label(r, text="选择不能选择的选项后提示").pack()
w2 = ttk.Entry(r)
w2.pack()

make_button = ttk.Button(r, text="制作", command=make)
make_button.pack()

r.mainloop()
