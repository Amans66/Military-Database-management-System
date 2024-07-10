def delete():
    import mysql.connector as mc
    mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
    if mycon.is_connected():
          print("connection established sucessfully")
    mycur=mycon.cursor()
    sno=int(input("enter Service no for record deletion :-"))
    query=f"delete from m_wts where service_no={sno}"
    mycur.execute(query)
    mycon.commit()
    print("data delelted sucessfully")
