import mysql.connector
import tkinter  as tk 
from tkinter import *
def call():
        my_w = tk.Tk()
        my_w.title("Display")
        my_w.configure(bg="sky blue1")
        my_w.geometry("1400x327")
        Label(my_w,text="displaying data from table                                                                                   ",font="STENCIL 30",bg="black",fg="white").place(x=0,y=225)
        Label(my_w,text="Military Info                                                                                                                  ",font="STENCIL 30",bg="black",fg="white").place(x=0,y=275)
        my_connect = mysql.connector.connect( 
          host="localhost",
          user="root", 
          passwd="1234",
          database="military"
        )
        my_conn = my_connect.cursor()
        ####### end of connection ####
        my_conn.execute("SELECT * FROM m_info")
        my=("SNO","SERVICE NO","Gender","DOB","Father Name ","Mother Name","Phone no","Salary","Marital Status","Join date","Retirement","Home town")
        c = Entry(my_w, width=14, fg='white',bg='black')
        c.grid(row=0, column=11,padx=5,pady=0,ipadx=10) 
        c.insert(END, my[11])
        b=1
        i=5
        for student in my_conn: 
            for j in range(len(student)):
                e = Entry(my_w, width=14, fg='black')
                e.grid(row=i, column=j+1,padx=5,pady=0,ipadx=10) 
                e.insert(END, student[j])
                f= Entry(my_w, width=14, fg='black')
                f.grid(row=i, column=0,padx=5,pady=0,ipadx=10) 
                f.insert(END, b)
                a = Entry(my_w, width=14, fg='white',bg="black")
                a.grid(row=0, column=j,padx=5,pady=0,ipadx=10) 
                a.insert(END, my[j])
            b+=1   
            i=i+1
        my_w.mainloop()

