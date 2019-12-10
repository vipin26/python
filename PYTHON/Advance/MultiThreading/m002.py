#threading using oops

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
      display(self.name)

def display(threadName):
    print "Starting " + threadName + " Multi Threading Example "+ threadName +"\n"
    
# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()

