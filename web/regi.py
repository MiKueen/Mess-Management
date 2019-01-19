#!C:\Python36\python

import cgi, cgitb, mysql.connector
cgitb.enable()
obj=cgi.FieldStorage()
login_id=obj.getvalue("login_id")

print("Content-type:text/html")
print("Set-Cookie: session="+login_id+";")
print("")

submit=obj.getvalue("submit")
role=""
if submit!=None:
    xpass=obj.getvalue("login_pass")
    db=mysql.connector.connect(host="localhost",user="root",password="",database="mess")
    cursor=db.cursor()
    query="select * from login where id='%s'"%login_id
    cursor.execute(query)
    result=cursor.fetchall()
    db.commit()
    if result==[]:
        print("<script>alert('Wrong credentials, Redirect to login page?'); window.location='http://localhost/web/login.py'</script>")
    resultfine=result[0]
    passw=resultfine[1]
    role=resultfine[2]
    if passw==xpass:
        print("Login successful")
    else:
        print("Login not successful") 
        print("""
            <script>
                var cookies = document.cookie.split(";");
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i];
                    var eqPos = cookie.indexOf("=");
                    var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                    document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
                }
                document.location.reload()
                alert("Redirecting.........")
            </script>
            """)

print("<h2 id='test11'>"+role+"</h2>")
print("<h2 id='test12'>"+login_id+"</h2>")

print("""
    <script>
        var role= document.getElementById('test11').textContent;
        var id= document.getElementById('test12').textContent;
        var url1="http://localhost/web/admin.py?id="+id;
        var url2="http://localhost/web/student.py?id="+id;
        if (role=="admin")
            window.location=url1;
        else if(role=="student")
            window.location=url2;
        else
            document.write("role not matched");
    </script>
    """)