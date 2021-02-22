from tkinter import *
import subprocess
import os

root = Tk()
root.title("Connect to a remote machine")
#root.geometry("640x640")
root.resizable(False, False)

usname = os.getlogin()
bg = PhotoImage(file = "/home/" + usname + "/.Tux_Connect/icons/001_Tux_wall.png") 
label1 = Label(root, image=bg) 
label1.place(x = 0, y = 0) 

#label1 = Label(root, text="TuxConnect")
#label2 = Label(root, text="This is Abhijith")
label3 = Label(root, text="Enter a Connection Name")

#label1.grid(row=0, column=2)
#label2.grid(row=1, column=2)
label3.grid(row=2, column=0, sticky=W)


#Testing a connection
conn_name = Entry(root, width=50, borderwidth=5, fg="blue", bg="white")
conn_name.grid(row=5, column=0)


def clickme():
    conNm = conn_name.get()
    usrnm = os.getlogin()
    label4 = Label(root, text="Testing a Connection").grid(row=4, column=2)
    subprocess.call(["sh" , "/home/" + usrnm + "/.Tux_Connect/resources/connect.sh" , conNm])
    label5 = Label(root, text="Connected to the remote machine successfully").grid(row=7, column=2)

button = Button(root, text="Connect", fg="blue", bg="#ffffff", command=clickme)
button.grid(row=6, column=2)

root.mainloop()
