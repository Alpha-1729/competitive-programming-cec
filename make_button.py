#link refernce
#link:  https://stackoverflow.com/questions/2307464/what-is-the-difference-between-root-destroy-and-root-quit
#link on lift method: https://stackoverflow.com/questions/1892339/how-to-make-a-tkinter-window-jump-to-the-front
import os
from tkinter import *
from tkinter import ttk
def make_file():
    os.startfile("make_file.bat")
root=Tk()
root.geometry('30x30+{}+{}'.format(+1300,+550))
#root.title("")
button=Button(root,text="M",font=('Arial Bold', '12'),command=make_file) #font,height,width parameter work for tkinter Button and not for ttk Button
button.pack()
root.update()
#create the gui window above all other apps
root.attributes("-topmost", True)
root.overrideredirect(True)
root.lift()
#root.destroy()
root.mainloop()
