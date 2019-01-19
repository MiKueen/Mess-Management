import mysql.connector as mysql

def loadFile(filename):
	fl = open(filename,"r")	
	return fl.read()

def runQuery(query):	
	try:
		cnn = mysql.connect(host="localhost",user="root",password="",database="mess")
		cr = cnn.cursor()
		cr.execute(query)	
		cnn.commit()		
		return True
	except Exception as ex:		
		return False
	finally:
		cnn.close()			
		