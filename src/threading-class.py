from threading import Thread 
from time import sleep

class SleepyThread(Thread):
	def __init__(self, name, delay):
		Thread.__init__(self)
		self.name = name
		self.delay = delay

	def run(self):
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