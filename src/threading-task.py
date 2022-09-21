"""
##### Description
Demonstrating the creation of Python threads using the 
[`threading`](https://docs.python.org/3/library/threading.html) module.	
This approach relies on creating objects as instances of the 
[`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread)
class as threads to run a callback function.

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 21, 2022
"""

from threading import Thread 
from time import sleep

def doTask(id):
	"""
	Simulates the execution of a task.	
	This is a callback function to run upon a thread.

	:param id: Task ID
	"""
	print("Starting task", id)
	sleep(1)
	print("Task", id, "is done")

threads = []
for i in range(1, 11):
	t = Thread(target=doTask, args=(i, ))
	threads.append(t)
	t.start()

for t in threads:
	t.join()

print("All threads finished execution")