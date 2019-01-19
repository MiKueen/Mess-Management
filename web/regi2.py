#!C:\Python36\python
print("Content-type:text/html")
print("")

import cgi, cgitb, mysql.connector
import datetime

print("""
        <html>
        <head>
            <title>Mess management</title>
        </head>
        <body>
    """)

now = datetime.datetime.now()
print ("Current date: "+now.strftime("%Y-%m-%d"))
date=now.strftime("%Y-%m-%d")

cgitb.enable()
obj2=cgi.FieldStorage()
submit=obj2.getvalue("submit")
id2=""

if submit!=None:
    id2=obj2.getvalue("id")
    choice=obj2.getvalue("choice")  
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="insert into feedback values('"+id2+"','"+choice+"','"+date+"')"
    cursor.execute(query)
    db.commit()

print("""   
        <script>
            window.location='http://localhost/web/student.py?id="""+id2+"""'
        </script>
    </body>
    </html>
    """)
