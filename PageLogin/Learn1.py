from tkinter import *
from tkinter import ttk
from tkintermapview import TkinterMapView
abdo = Tk()

abdo.geometry('450x450')
abdo.config(bg='silver')
abdo.resizable(False,False)
abdo.iconbitmap('livre.ico')

lb1 = Label(abdo,text='LOGIN SYSTEM',bg='black',fg='white',font=(10))
lb1.pack(fill=X)


fr= Frame(abdo,bg='white',width=340,height=380)
fr.pack(pady=30)

lb2=Label(fr,text='USERNAME :',font=('courier',11),bg='white')
lb2.place(x=15,y=150)
ent2 = Entry(fr,font=(11))
ent2.place(x=125,y=150)


lb3=Label(fr,text='PASSWORD :',font=('courier',11),bg='white')
lb3.place(x=15,y=190)
ent3 = Entry(fr,font=(11))
ent3.place(x=125,y=190)


##check butoon


bt = Checkbutton(fr,text='Forget Password !',font=('courier',15),bg='white')
bt.place(x=60,y=240)

#butto

bt1 = Button(fr,text='Login',bg='#19A7CE',font=('courier',15),width='13')
bt1.place(x=8,y=290)

bt2 = Button(fr,text='SIGN IN',bg='#F78CA2',font=('courier',15),width='13')
bt2.place(x=159,y=290)

#--image

im = PhotoImage(file='pngegg.png')
res = im.subsample(9,9)
bt = Button(fr,image=res)
bt.place(x=110,y=9)

lb0=Label(abdo,text='devloper By 8d1',bg='silver')
lb0.place(x=360,y=430)


abdo.mainloop()