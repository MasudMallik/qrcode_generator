from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
import qrcode
global name,file_name,f,col1,b1,col2,b2,temp1,temp2,sub,show,ex
temp1="black"
temp2="white"
def fg_col():
    global temp1
    temp=colorchooser.askcolor(title="choose a fore-ground color: " )
    temp1=temp[1]
    b1.config(bg=temp1)
def bg_col():
    global temp2
    temp=colorchooser.askcolor(title="choose a back-ground color: " )
    temp2=temp[1]  
    b2.config(bg=temp2)
def submit():
    try:
        data=link1.get(1.0,END).strip()
        fg_coll=temp1
        bg_coll=temp2
        name_file=file_name.get(1.0,END).strip()
        if name_file=="":
            raise NameError("Please enter the name of the file!!")
        elif not name_file.endswith(".png"):
            name_file+=".png"
        if data=="":
           raise ValueError("please enter the link first")
    except ValueError as e:
         messagebox.showerror("ERROR","please enter the link first")
    except NameError as e:
        messagebox.showerror("ERROR",f"{e}")
    except Exception as e:
        messagebox.showinfo("INFO",f"{e}")
    else:
        qr=qrcode.QRCode()
        qr.add_data(data)
        qr.make()
        img=qr.make_image(fill_color=fg_coll,back_color=bg_coll)
        img.save(name_file)
        img.show()
        messagebox.showinfo("showinfo","qrcode succesfully created")
def show_qr():
    data=link1.get(1.0,END).strip()
    if data=="":
        messagebox.showerror("ERROR","please enter the link first")
    else:
        img=qrcode.make(data)
        img.show()

def apply_condition():
    global name,file_name,f,col1,b1,col2,b2,sub,show,ex
    data=k.get()
    if data==1:
        show.destroy()
        ex.destroy()
        name=Label(root,text="enter the name of the file: ")
        name.grid(row=5,column=0)
        file_name=Text(root,height=2,width=50)
        file_name.grid(row=6,column=0)
        f=Frame(root,height=100,width=300)
        f.grid(row=7,column=0)
        col1=Label(f,text="choose foreground color: ")
        col1.grid(row=0,column=0)
        b1=Button(f,text="choose fg color: ",command=fg_col)
        b1.grid(row=1,column=0)
        col2=Label(f,text="choose background color: ")
        col2.grid(row=0,column=2)
        b2=Button(f,text="choose bg color: ",command=bg_col)
        b2.grid(row=1,column=2)
        sub=Button(root,text="SUBMIT",command=submit)
        sub.grid(row=8,column=0,pady=20,padx=20)
        ex=Button(root,text="Exit",height=1,width=7,command=root.destroy)
        ex.grid(row=9,column=0,padx=10,pady=10)
        
        
    else:
        name.destroy()
        file_name.destroy()
        f.destroy()
        col1.destroy()
        b1.destroy()
        col2.destroy()
        b2.destroy()
        sub.destroy()
        show=Button(root,text="Show Qr",command=show_qr)
        show.grid(row=5,column=0)
root=Tk()
root.geometry("500x400")
root.title("Qr-code generator")
#root.maxsize(500,400)
hea=Label(root,text="Qr code generator",font=10)
hea.grid(row=0,column=0,padx=200,pady=5)
link=Label(root,text="enter the link: ")
link.grid(row=1,column=0)
link1=Text(root,height=2,width=50)
link1.grid(row=2,column=0)
k=IntVar()
ch=Checkbutton(root,text="want to save the qrcode.....",variable=k,onvalue=1,offvalue=0)
ch.grid(row=3,column=0)
apply=Button(root,text="APPLY",command=apply_condition)
apply.grid(row=4,column=0,)
show=Button(root,text="Show Qr",command=show_qr)
show.grid(row=5,column=0,padx=5,pady=5)
ex=Button(root,text="Exit",height=1,width=7,command=root.destroy)
ex.grid(row=6,column=0,padx=10,pady=10)
root.mainloop()