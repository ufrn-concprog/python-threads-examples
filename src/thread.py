"""
##### Description
Demonstrating the creation of Python threads using the 
[`thread`](https://python.readthedocs.io/en/v2.7.2/library/thread.html) module.		
This approach treats a thread as a function, i.e., it relies on callback functions.

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 21, 2022
"""

from _thread import start_new_thread

def thread_getName(threadName):
	"""
	Prints a name given to a thread in the standard output.	
	This is a callback function to run upon a thread.

	:param threadName: Name to assign to the thread
	"""
	print("I am thread", threadName)

start_new_thread(thread_getName, ('T1', ))
start_new_thread(thread_getName, ('T2', ))

print("All threads finished execution")