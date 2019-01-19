# Mess-Management

This website provides a complete system with both interfaces; one for mess admin and another for students. With this application mess admins are able to upload the daily menu. Students can see that menu and choose whther they want to eat or not. The admins analyse the feedback made by students and if the feedback is positive, the same menu is finalized for the day.

## Requirements:
XAMPP version 5.6.39

## Add Python in XAMPP:

**STEP-1:[Download Python]**
Download & install the latest version of python from www.python.org Download Python & click on the windows installer of any version [ex. python-3.6.2]

**STEP 2: [Install Python]** 
Install in any directory of your harddrive [ex. C:\python-3.6.2]

**STEP 3: [Configure Python]** 
Open the directory where xammp was installed Go to apache >> conf [ex. C:\xampp\apache\conf\httpd.conf] You'll see a file named httpd.conf Open it in any text editor & just add `.py` at the end of the below line

AddHandler cgi-script .cgi .pl .asp
