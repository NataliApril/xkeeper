
from threading import *
import time
import random

def first():
	print ("First start")
	time.sleep(3)
	print("First end")
	
def second():
	print ("Second start")
	time.sleep(7)
	print("Second end")

def func(i):
	print(i,  "sub thread start")
	time.sleep(random.randint(1,5))
	print(i, "sub thread stop")
	
def third():
	print ("Third start")
	time.sleep(1)
	for i in range(0, 5):
		res = Thread(target = func, args = (i, ))
		res.deamon = True
		res.start()
		#res.join()
	#t5 = Thread(target = func)
	#t5.deamon = True
	#t5.start()
	#t5.join()
	time.sleep(1)
	print("Third end")
	
if __name__ == "__main__":
	t1 = Thread(target = first)
	t2 = Thread(target = second)
	t3 = Thread(target = third)
	t1.deamon = False    #main prcocess
	t2.deamon = True    #deamon process
	t3.deamon = True    #deamon process
	t1.start()
	t2.start()
	t3.start()
	#t1.join()
	#t2.join()
	#t3.join()
