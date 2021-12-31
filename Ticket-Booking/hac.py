# -- coding: utf-8 --
"""
Created on Mon Nov 15 11:02:55 2021

@author: bhargav
"""

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.messagebox import askyesno

window =Tk()
window.geometry('450x200')
window.title("HMR")
# buuton clicked

def clicked():
    messagebox.showinfo("TICKET CONFIRMATION",txt1.get()+
                            " Your Metro Ticket has successfully Booked.\n  \nFROM "+click.get()+"  TO  "+click1.get()+
                            "\n""TIME: "+click2.get())
  
window.iconbitmap('hmr.ico')
#label
lbl= Label(window, text="HMR TICKET BOOKING",font=("Arial Bold",15))
lbl.grid(column=1,row=0)
#customer name
lbl= Label(window, text="PASSENGER NAME")
lbl.grid(column=0,row=1)
lbl= Label(window, text="FROM: ")
lbl.grid(column=0,row=2)
lbl= Label(window, text="WHERE TO: ")
lbl.grid(column=0,row=3)
lbl= Label(window, text="TIME:")
lbl.grid(column=0,row=4)
lbl = Label(window, text="Do you need cab?",font=("Arial Bold",8))
lbl.grid(column=0,row=5)


# cab  label
def clicked1():
    lbl= Label(window, text="Enter your drop point ")
    lbl.grid(column=0,row=7)
    
    

def clicked2():
     messagebox.showinfo("TICKET CONFIRMATION",txt1.get()+
                            " Your Metro Ticket has successfully Booked.\n  \nFROM "+click.get()+"  TO  "+click1.get()+
                            "\n""TIME: "+click2.get()+
                            "\n CAB DETAILS""\n  CAB  FROM :" +click1.get()+ " TO " +txt2.get())

# Drop FROM
options = [
    "Select",
    "MIYAPUR",
    "JNTUH COLLEGE",
    "KPHB COLONY",
    "KUKATPALLY",
    "BALNAGAR",
    "MOOSAPET",
    "BHARATH NAGAR",
    "ERRAGADA",
    "ESI HOSPITAL",
    "SR NAGAR",
    "AMEERPET"  
]
click = StringVar() 
click.set( "FROM " ) 
drop = OptionMenu( window , click , *options )
drop.grid(column=1,row=2)
# Drop To 
# Drop Down
options1 = [
    "Select",
    "PUNJAGUTTA",
    "IRRUM MANZIL",
    "KHAIRTHABAD",
    "LAKDIKAPUL",
    "ASSSEMBLY",
    "NAMPALLY",
    "GANDHIBHAVAN",
    "OSMANIA MEDICAL COLLGE",
    "MGBS"
]
click1 = StringVar()  
click1.set( "TO" )  
drop = OptionMenu( window , click1 , *options1 )
drop.grid(column=1,row=3)
options2 = [
    "Select",
    "9:30 to 10:30",
    "10:30 to 11:30",
    "11:30 to 12:30",
    "12:30 to 1:30"
]
click2 = StringVar()
click2.set( "TIME" )
drop = OptionMenu( window , click2 , *options2 )
drop.grid(column=1,row=4)
#entry box
txt1 = Entry(window,width=20)
txt1.grid(column=1,row=1)
txt2 = Entry(window,width=20)
txt2.grid(column=1,row=7)
## submit button 
btn=Button(window,text="YES",command=clicked1)
btn.grid(column=1,row=5)
btn= Button(window,text="NO",command=clicked)
btn.grid(column=2,row=5)
btn=Button(window, text="BOOK",command=clicked2)
btn.grid(column=2,row=7)
window.mainloop()