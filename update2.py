from tkinter import *
import mysql.connector as mc
def call():
    class MyWindow:
        def __init__(self, win):
            self.lb=Label(win,text="UPDATE",font="STENCIL 18",relief=RIDGE,bg="gold",fg="black",bd=4)
            self.lb.place(x =0, y = 0)
            self.lbl1=Label(win, text='Service No :-',relief=RIDGE,font="arial ")
            self.lbl2=Label(win, text='Choice no :-',relief=RIDGE,font="arial ")
            self.lbl3=Label(win, text=' Massage---> ',relief=RIDGE,font="arial ")
            self.lbl4=Label(win, text='Enter Detail :-',relief=RIDGE,font="arial ")
            a="1:Gender of the service person :- "
            b="2:DOB of the service person :-"
            c="3:F_name of the service person :-"
            d="4:M_name of the service person"
            e="5:Phone_no of the service person"
            g="6:Salary of the service person"
            h="7:Marital_status of the service person"
            i="8:Join_in of the service person"
            j="9:Retirement of the service person"
            k="10:Home_town of the service person"
            f="=======CHOICES========"
            self.lb=Label(win,text =f,font='bold')
            self.lb.place(x = 100, y = 110)
            self.lb=Label(win,text =a,font='bold')
            self.lb.place(x = 100, y = 135)
            self.lb=Label(win,text =b,font='bold')
            self.lb.place(x = 100, y = 159)
            self.lb= Label(win,text =c,font='bold')
            self.lb.place(x = 100, y = 180)
            self.lb=Label(win,text =d,font='bold')
            self.lb.place(x = 100, y = 200)
            self.lb=Label(win,text =e,font='bold')
            self.lb.place(x = 100, y = 220)
            self.lb=Label(win,text =g,font='bold')
            self.lb.place(x = 100, y = 240)
            self.lb=Label(win,text =h,font='bold')
            self.lb.place(x = 100, y = 260)
            self.lb=Label(win,text =i,font='bold')
            self.lb.place(x = 100, y = 280)
            self.lb=Label(win,text =j,font='bold')
            self.lb.place(x = 100, y = 300)
            self.lb=Label(win,text =k,font='bold')
            self.lb.place(x = 100, y = 320)
            
            
            self.t1=Entry(bd=4)
            self.t2=Entry(bd=4)
            self.t3=Entry(bd=4)
            self.t4=Entry(bd=4)
            self.btn1 = Button(win, text='Update',font=" STENCIL ",bd=5)
            self.btn2=Button(win, text='Exit',font=" STENCIL ",bd=5)
            self.lbl1.place(x=100, y=30)
            self.t1.place(x=200, y=30)
            self.lbl4.place(x=100, y=70)
            self.t4.place(x=200, y=70)
            self.lbl2.place(x=100, y=50)
            self.t2.place(x=200, y=50)
            self.b1=Button(win, text='Update',font=" STENCIL ",bg ='green3',fg="white",bd=5,command=self.update)
            self.b2=Button(win, text='Exit',bg ='red',font="STENCIL",command=win.destroy,bd=5,fg="white")
            self.b2.bind('<Button-1>')
            self.b1.place(x=100, y=350)
            self.b2.place(x=200, y=350)
            self.lbl3.place(x=100, y=400)
            self.t3.place(x=200, y=400 ,width=150)
        def update(self):
            self.t3.delete(0, 'end')
            sno=int(self.t1.get())
            ch=int(self.t2.get())
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
            if mycon.is_connected():
                 print("connection established sucessfully")
            mycur=mycon.cursor()
            if ch==1:
               g=self.t4.get()
               query=f"update M_info set gender='{g}' where service_no={sno}"
            elif ch==2:
                d=self.t4.get()
                query=f"update M_info set ='{d}' where service_no={sno}"
            elif ch==3:
                f=self.t4.get()
                query=f"update M_info set F_name='{f}' where service_no={sno}"
            elif ch==4:
                m=self.t4.get()
                query=f"update M_info set M_name='{m}' where service_no={sno}"
            elif ch==5:
                p=self.t4.get()
                query=f"update M_info set phone_no='{p}' where service_no={sno}"
            elif ch==6:
                s=self.t4.get()
                query=f"update M_info set salary='{s}' where service_no={sno}"
            elif ch==7:
                ms=input("enter marital_status :-")
                query=f"update M_info set marital_status='{ms}' where service_no={sno}"
            elif ch==8:
                j=self.t4.get()
                query=f"update M_info set join_in='{j}' where service_no={sno}"
            elif ch==9:
                r=self.t4.get()
                query=f"update M_info set retirement='{r}' where service_no={sno}"
            elif ch==10:
                h=self.t4.get()
                query=f"update M_info set home_town='{h}' where service_no={sno}"
            mycur.execute(query)
            mycon.commit()
            result="data updated sucessfully"
            self.t3.insert(END, str(result))

    window=Tk()
    mywin=MyWindow(window)
    window.title('Update M_WPS')
    window.geometry("500x450+10+10")
    window.configure(bg="orange")
    window.mainloop()
