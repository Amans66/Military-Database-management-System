import mysql.connector
import tkinter 
from tkinter import *
class MyWindow:
        def __init__(self, win):
              self.lbl1 = Label(win, text='Service No :-', relief=RIDGE, font="arial ")
              self.lbl1.place(x=100, y=30)
              self.lbl2 = Label(win, text='********************DETAILS OF THE EMPLOYEE ************************', relief=RIDGE, font="arial ")
              self.lbl2.place(x=4, y=70)
              self.lbl2 = Label(win, text='NAME :-', relief=RIDGE, font="arial ")
              self.lbl2.place(x=100, y=100)
              self.lbl3 = Label(win, text='SERVING IN :-', relief=RIDGE, font="arial ")
              self.lbl3.place(x=100, y=140)
              self.lbl4 = Label(win, text='RANK :-', relief=RIDGE, font="arial ")
              self.lbl4.place(x=100, y=180)
              self.lbl5 = Label(win, text='TRADE :-', relief=RIDGE, font="arial ")
              self.lbl5.place(x=100, y=220)
              self.lbl6 = Label(win, text='UNIT :-', relief=RIDGE, font="arial ")
              self.lbl6.place(x=100, y=260)


                # add one text box
              self.t1 = Entry(bd=4)
              self.t1.place(x=200, y=30)
              self.t2 = Entry(bd=4)
              self.t2.place(x=200, y=100)
              self.t3 = Entry(bd=4)
              self.t3.place(x=200, y=140)
              self.t4 = Entry(bd=4)
              self.t4.place(x=200, y=180)
              self.t5 = Entry(bd=4)
              self.t5.place(x=200, y=220)
              self.t6 = Entry(bd=4)
              self.t6.place(x=200, y=260)

              self.b1 = Button(win, text='Show Details',height=1, width=12,bg='green',font="STENCIL 11",fg="white",command=self.search)
              self.b1.place(x=350,y=26)




        def search(self):
           self.t2.delete(0, 'end')
           self.t3.delete(0, 'end')
           self.t4.delete(0, 'end')
           self.t5.delete(0, 'end')
           self.t6.delete(0, 'end')

           a=int(self.t1.get())
           my_connect = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="1234",
                  database="military"
                )
           my_conn = my_connect.cursor()
           query=f"SELECT * FROM m_employee WHERE service_no = '{a}' "
           my_conn.execute(query)
           data=my_conn.fetchone()

           D1 = data[1]
           D2 = data[2]
           D3 = data[3]
           D4 = data[4]
           D5 = data[5]

           self.t2.insert(END, str(D1))
           self.t3.insert(END, str(D2))
           self.t4.insert(END, str(D3))
           self.t5.insert(END, str(D4))
           self.t6.insert(END, str(D5))




window = Tk()
mywin = MyWindow(window)
window.title('Update M_employee')
window.geometry("500x450+10+10")
window.configure(bg="orange")
b1 = Button( text='Exit', height=1, width=17, bg='Red',font="STENCIL", bd=5, fg="white", command=window.destroy)
b1.place(x=100, y=310)
window.mainloop()
