import tkinter as tk
from tkinter import *

from tkinter import messagebox
from tkinter import Toplevel, Button, Tk, Menu
from PIL import Image, ImageTk

def Login():
     
     def login():
         import mysql.connector as mc
         mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
         if mycon.is_connected():
               print("connection established sucessfully")
               mycur=mycon.cursor()
         username=Username.get()
         mycur.execute("select username from login where username='"+username+"'")
         pot=mycur.fetchone()
         if pot is not None:
              p="VALID USERNAME!!!!!!"
              lblfrstrow = tk.Label(root,text =p,font='bold',fg='white',bg='green',bd=5)
              lblfrstrow.place(x = 50, y = 380)
              pw=password.get()
              mycur.execute("select password from login where password='"+pw+"'")
              a=mycur.fetchone()
              lblfrstrow = tk.Entry(relief=RIDGE, font='bold',width=25,bd=5,fg='white',bg='green')
              lblfrstrow.place(x=50, y=420)
              if a is not None:
                   l="LOGIN SUCCESSFULL"
                   lblfrstrow.insert(END, str(l))


              elif a is None:
                   l="But User Password Incorrect"
                   lblfrstrow.insert(END, str(l))

    
     root = tk.Tk()
     root.configure(bg="gold")
     root.geometry("310x450")
     root.title(" Login site of Military DB ")

      # Create a photoimage object of the image in the path
     image1 = Image.open("C:\D.jpg")
     test = ImageTk.PhotoImage(image1)

     label1 = tk.Label(image=test)
     label1.image = test

      # Position image
     label1.place(x= '40', y='')

      #create buttun
     lblfrstrow = tk.Label(root,text ="Username -",relief=RIDGE,font='bold 13')
     lblfrstrow.place(x = 50, y = 250)

     Username = tk.Entry(root, width = 100)
     Username.place(x = 150, y = 253, width = 100)

     lblsecrow = tk.Label(root, text ="Password - ",relief=RIDGE,font='bold 13')
     lblsecrow.place(x = 50, y = 280)

     password = tk.Entry(root, width = 100)
     password.place(x = 150, y = 283, width = 100)

     submitbtn = tk.Button(root, text ="Login",bg ='green3',font='bold 18',fg='white',relief=RIDGE, command = login)
     submitbtn1 = tk.Button(root, text ="Exit",bg ='red',font='bold 18',fg='white', relief=RIDGE,command =quit)
     submitbtn.place(x = 70, y = 320, width =70 )
     submitbtn1.place(x = 150, y = 320, width = 70)

     root.mainloop()


Login()
