"""
##### Description
Demonstrating the creation of Python threads using the 
[`threading`](https://docs.python.org/3/library/threading.html) module.	
This approach relies on implementing a custom class and creating objects
from it to run upon threads.

##### Author
[Everton Cavalcante](mailto:everton.cavalcante@ufrn.br)

##### Date
September 21, 2022
"""

from threading import Thread 
from time import sleep

class SleepyThread(Thread):
	"""
	This class represents a thread that suspends itself for a given number of seconds.	
	This class is a subclass of 
	[`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread) and 
	overrides its `run` method to code the statements to be executed by a thread object.
	"""
	def __init__(self, name, delay):
		"""
		Class constructor
		:param self: Self-reference
		:param name: Name to be assigned to the thread
		:param delay: Time (in seconds) for which the thread will be suspended
		"""
		Thread.__init__(self)
		self.name = name
		self.delay = delay

	def run(self):
		"""
		Makes the thread to be suspended for the given delay	
		This overrides the [`run`](https://docs.python.org/3/library/threading.html#threading.Thread.run) 
		method originally defined in the `Thread` class
		"""
		print("Thread", self.name, "suspending for", self.delay, "seconds")
		sleep(self.delay)
		print("Thread", self.name, "finished")

t1 = SleepyThread("T1", 3)
t2 = SleepyThread("T2", 1)

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished execution")