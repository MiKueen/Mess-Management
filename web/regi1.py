#!C:\Python36\python
print("Content-type:text/html")
print("")

print("""
        <html>
        <head>
            <title>Mess management</title>
        </head>
        <body>
    """)

import cgi, cgitb, mysql.connector
cgitb.enable()

obj1=cgi.FieldStorage()
submit=obj1.getvalue("submit")
id1=obj1.getvalue("id")

if submit!=None:
    menuname=obj1.getvalue("menuname")
    menu=obj1.getvalue("tarea")
    date=obj1.getvalue("date")
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="insert into menu values('"+id1+"','"+menuname+"','"+menu+"','"+date+"')"
    cursor.execute(query)
    db.commit()

print("""   
        <script>
            window.location='http://localhost/web/admin.py?id="""+id1+"""'
        </script>
    </body>
    </html>
    """)
