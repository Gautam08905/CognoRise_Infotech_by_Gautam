from tkinter import *
import random
import string
from tkinter.messagebox import *

root=Tk()
root.geometry("650x450")
root.configure(bg="#80BCBD")
root.title("Password Generator")

def generate_password():
    if a.get()=="":
        showerror(
            title="warning",message="Please enter the LENGTH of PASSWORD"
        )
    else:
        length=int(a.get())
        # Define the pool of characters to choose from
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate password using random.choices for Python 3.6+
        password = ''.join(random.choices(characters, k=length))
        b.set(password)


frm=Frame(root,width=600,height=400,bg="#AAD9BB",relief=RIDGE)
frm.pack()
head=Label(frm,text="PASSWORD GENERATOR 🗝️",width=40,font="cambria 20 bold",bg="#AAD9BB")
head.place(x=15,y=0)

l1=Label(frm,text="Enter the desired length for password: ",bg="#D5F0C1",width=32,height=2,font="helvetic 11 bold")
l1.place(x=10,y=90)

a=StringVar()
e1=Entry(frm,textvariable=a,width=16,font="helvetic 20",bg="#F9F7C9",relief=RIDGE)
e1.place(x=340,y=92)

l2=Label(frm,text="Password will be generated here: ",bg="#D5F0C1",width=32,height=2,font="helvetic 11 bold")
l2.place(x=10,y=190)

b=StringVar()
e2=Entry(frm,textvariable=b,width=16,font="helvetic 20",bg="#F9F7C9",relief=RIDGE)
e2.place(x=340,y=192)

but=Button(frm,text="GENERATE 🔍",font="cambria 17 bold",bg="#80BCBD",width=15,height=1,relief=RIDGE,command=generate_password)
but.place(x=210,y=290)




root.mainloop()
