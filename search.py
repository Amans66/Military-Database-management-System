def search():
     import mysql.connector as mc
     mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
     if mycon.is_connected():
          print("connection established sucessfully")
     mycur=mycon.cursor()
     sno=input("enter sevice no")
     query=f"select * from m_wts where seviceno>={sno}"
     mycur.execute(query)
     data=mycur.fetchall()
     print("Sno","%15s"%"Service no","%15s"%"WTS","%15s"%"WTS ID","%15s"%"DT Out","%25s"%"DT In","%20s"%"Reason""%20s"%"BASE Location")
     print("------------------------------------------------------------------------------------------------------------------")
     print('\n')
     a=1
     for i in data :
          print(a,"%15s"%i[0],"%15s"%i[1],"%15s"%i[2],"%23s"%i[3],"%25s"%i[4],"%15s"%i[5],"%15s"%i[6])
          a+=1

