from _thread import start_new_thread

def thread_getName(threadName):
	print("I am thread", threadName)

start_new_thread(thread_getName, ('T1', ))
start_new_thread(thread_getName, ('T2', ))

print("All threads finished execution")