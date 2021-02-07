# A simple nanoseconds stopwatch implemented in Python.
# time.clock() gives wallclock seconds accurate to at least 1 millisecond
# it updates every millisecond, but only works with windows
# time.time() is more portable, but has quantization errors
# since it only updates updates 18.2 times per second
 
import time
 
print ("\nTiming a 1 million loop 'for loop' ...")
start = time.time()
for x in range(1000000):
  y = 100*x - 99  # do something
end = time.time()
print ("Time elapsed = ", end - start, "seconds")
 
"""
result -->
Timing a 1 million loop 'for loop' ...
Time elapsed =  0.471708415107 seconds
"""