#!C:\Python36\python

print("Content-type:text/html")
print("")

import cgi, cgitb, mysql.connector
from code import loadFile
cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("submit")

role=""
if submit!=None:
    login_id=obj.getvalue("login_id")
    xpass=obj.getvalue("login_pass")
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="select * from login where id='%s'"%login_id
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    resultfine=result[0]
    passw=resultfine[1]
    role=resultfine[2]
    if passw==xpass:
        print("Login successful")
        
    else:
        print("Login not successful")    
    

log=loadFile("login.html")
print(log)