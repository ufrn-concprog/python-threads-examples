from threading import Thread 
from time import sleep

def doTask(id):
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