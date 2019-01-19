#!C:\Python36\python
print("Content-type:text/html")
print("")

from code import loadFile, runQuery
import cgi,cgitb,mysql.connector

cgitb.enable()
obj=cgi.FieldStorage()
submit=obj.getvalue("submit")
id=""
passw=""
role="student"

sign=loadFile("signup.html")
print(sign+"")

if submit!=None:
    id=obj.getvalue('id')
    passw=obj.getvalue('pass')
    name=obj.getvalue('name')
    contact=obj.getvalue('contact')
    email=obj.getvalue('email')
    db=mysql.connector.connect(host='localhost',user='root',password='',database='mess')
    cursor=db.cursor()
    query="select id from login where id='"+id+"'"
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    
    if len(result)>0:
        print("<script>alert('Username is already taken. Choose another one.')</script>")
        print("")
    else:
        #cursor=db.cursor()
        query="insert into login values('"+id+"','"+passw+"','student')"
        res = runQuery(query)
        #cursor.execute(query)
        #db.commit()
        query = "insert into signup(name,contact,email,id,pass) values('{nm}','{cnt}','{ml}','{id}','{pd}')".format(nm=name,cnt=contact,ml=email,id=id,pd=passw)
        res = runQuery(query)
        #cursor.execute(query)
        #db.commit()
        print("<script>alert('Account Created. Please login on next window.'); window.location='http://localhost/web/login.py';</script>")
    
    print("""
            </body>
            </html>
        """)
