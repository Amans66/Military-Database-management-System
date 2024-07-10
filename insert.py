def insert():
    import mysql.connector as mc
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
    if mycon.is_connected():
         print("connection established sucessfully")
    mycur=mycon.cursor()
    sno=int(input("enter service no:"))
    g=input("Enter Weaponry Transpotation System:")
    d=input("Enter Weaponry Transpotation System_ID:")
    f=input("Enter Date Time_out(yyyy-mm-dd hh:mm:ss):")
    m=input("Enter Date Time_in(yyyy-mm-dd hh:mm:ss):")
    p=input("Enter Reason:")
    h=input("Base_Location:")
    query=f"insert into m_wts values({sno},'{g}','{d}','{f}','{m}','{p}','{h}')"
    mycur.execute(query)
    mycon.commit()
    print("data inserted sucessfully")
