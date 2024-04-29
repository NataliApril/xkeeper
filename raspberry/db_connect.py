import psycopg2
from psycopg2 import Error
import time


class DB_actions():
	def connect_DB(self, data):
		
		try:
			#connection to data base
			conn = psycopg2.connect(dbname="tester", user="tester", password="postgres", host= "77.238.255.81", port="5432")
			cur = conn.cursor()
			data_to_insert = (data, 'test')
			cur.execute("INSERT INTO devices VALUES (%s, %s)", data_to_insert)
			conn.commit()
			
		except (Exception, Error) as error:
			print ("Error working table")
		finally:
			if conn:
				cur.close()
				conn.close()
				print ("stop connection DB")
		
		
		
	'''cur = conn.cursor()

	#cur.execute('select * from devices')
	#results = cur.fetchall()

	for result in results:
		print (result)'''
