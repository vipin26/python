import thread

#defining a function for thread 
def display(threadName):
    print "Hello this is thread "
   
#creating thread
try:
   thread.start_new_thread(display, ("Thread-1",))
except:
   print "Error: unable to start thread"

