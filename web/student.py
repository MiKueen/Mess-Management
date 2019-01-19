#!C:\Python36\python
print("Content-type:text/html")
print("")

import cgi, cgitb, mysql.connector,os
import datetime

now = datetime.datetime.now()
print ("<h3>Current date: </h3>"+now.strftime("%Y-%m-%d"))
date1=now.strftime("%Y-%m-%d")
cgitb.enable()

obj=cgi.FieldStorage()
id=obj.getvalue('id')

print("""
        <html>
        <head>
            <title>Mess Manager</title>
            <style type="text/css" >
                body {
                    background: linear-gradient(to right, #0F292F, #14A098);
                    background-repeat: no-repeat;
                    background-size: 100%;
                    text-align: center;
                    font-family: Lucida Console;
                    color: black;
                    text-shadow: 3px 3px 3px TEAL;
                    margin-top: 50px;
                }
            </style>
        </head>
    <body><enter><br/>
    """)

if "HTTP_COOKIE" in os.environ:
    if id!=os.environ["HTTP_COOKIE"]:
        print("""   <script>window.location='http://localhost/web/login.py</script>  """)

else:
    print("HTTP_COOKIE not set!")
    print(""" <script>window.location='http://localhost/web/login.py';</script> """)

print("""
        <h1>Hello """+id+"""</h2>  &nbsp;&nbsp;&nbsp;&nbsp; <a href="./login.py" onclick="delcookie()">logout</a>
        <br/><br/>
        <h2>Today's Menus:</h3>
    """)
db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
cursor=db.cursor()
query="select menuname,menu1 from menu where date='"+date1+"'"

cursor.execute(query)
result=cursor.fetchall()
db.commit()

for row in result:
    print("<h3>Menu Contents:</h3><br/>")
    for elem in row:
        print(elem+"<br/>")
print("""
        <form method="POST" action='regi2.py?id="""+id+"""'>
            <h2>Do you like the menu?(yes/no):&nbsp;<input type="text" name="choice" id="choice"></h2><br/>
            <input type="submit" style="margin-top:1%;" value="SUBMIT FEEDBACK" name="submit" id="submit"/>
        </form>
        <script>
            function delcookie(){
                var cookies = document.cookie.split(";");
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i];
                    var eqPos = cookie.indexOf("=");
                    var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
                }
            document.location.reload()
            alert("Redirecting.........")
            }
        </script>
    </body>
    </html>
    """)