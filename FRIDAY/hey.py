from tkinter import *
from tkinter.simpledialog import SimpleDialog
from turtle import left
from PIL import ImageTk,Image
#from tqdm import tqdm



#for i in tqdm(range(10000000)):
   # pass

root=Tk()
root.title('hello world')
img=ImageTk.PhotoImage(Image.open("D:\\FRIDAY\\images\\J.A.R.V.I.S.jpg"))
lbl=Label(root, image=img).pack()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)

#buttons 
def open():
    global my_img
    top=Toplevel()
    #lbl=Label(top,text="J.A.R.V.I.S").pack()
    my_img=ImageTk.PhotoImage(Image.open("D:\\FRIDAY\\images\\screen.jpg"))
    my_label = Label(top, image=my_img).pack()


    
    

    menu.add_cascade(label='File', menu=filemenu)
    #filemenu.add_separator()
    filemenu.add_command(label='Exit', command= top.destroy)
    filemenu.add_command(label='Exit Terminal', command=root.destroy)
    



    
btn=Button(root,text="ARE YOU READY",fg="black",activebackground="red", command = open).pack()












mainloop()
