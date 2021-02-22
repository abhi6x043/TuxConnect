from tkinter import *
import subprocess
import os

root = Tk()
root.title("Add Connection")
root.geometry("640x640")
root.resizable(False, False)

usname = os.getlogin()
bg = PhotoImage(file = "/home/" + usname + "/.Tux_Connect/icons/004_Tux_wall.png") 
label1 = Label(root, image=bg) 
label1.place(x = 0, y = 0) 


#label1 = Label(root, text="Welcome to TuxConnect").grid(row=0)
label1 = Label(root, text="Welcome to TuxConnect").grid(row=0)
label2 = Label(root, text="Designed by abhi6x043").grid(row=1)
spacelabel1=Label(root).grid(row=3)
Label(root).grid(row=4)
#spacelabel1.attributes('-alpha', 1)


label3 = Label(root, text="Enter the connection Name ").grid(row=5, sticky=W)
spaceLabel2 = Label(root, text="  ").grid(row=7)
label4 = Label(root, text="Enter the connection ip address ").grid(row=8, sticky=W)
spaceLabel3 = Label(root, text="  ").grid(row=10)
label5 = Label(root, text="Enter the connection port ").grid(row=11, sticky=W)
spaceLabel4 = Label(root, text="  ").grid(row=13)
label6 = Label(root, text="Enter the connection username ").grid(row=14, sticky=W)
spaceLabel5 = Label(root, text="  ").grid(row=16)
label7 = Label(root, text="Enter the connection password ").grid(row=17, sticky=W)


#Adding a connection
conn_name = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")
conn_ip = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")
conn_port = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")
conn_user = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")
conn_pass = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")

conn_name.grid(row=6)
conn_ip.grid(row=9)
conn_port.grid(row=12)
conn_user.grid(row=15)
conn_pass.grid(row=18)

spaceLabel6 = Label(root, text="  ").grid(row=19)

def clickme():
    name = conn_name.get()
    ip = conn_ip.get()
    port = conn_port.get()
    user = conn_user.get()
    passwd = conn_pass.get()
    usrnm = os.getlogin()
    label8 = Label(root, text="Adding a Connection").grid(row=21)
    subprocess.call(["sh" , "/home/" + usrnm + "/.Tux_Connect/resources/add_conn.sh" , name , ip , port , user , passwd])
    label9 = Label(root, text="Connection added successfully").grid(row=22)

button = Button(root, text="Add Connection", fg="blue", bg="#ffffff", command=clickme)
button.grid(row=20)

root.mainloop()
