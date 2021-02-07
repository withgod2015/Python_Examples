# system clock with nanosecond
# import the time module 
import time
import datetime
import sys

'''
#  1 Start--- 
print(datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=2**53 / 1e9))
print(datetime.timedelta(seconds=2**53 / 1e9))

for i in range(10):
    sys.stdout.write("\r" + str(i) + " seconds passed")
    sys.stdout.flush()
    time.sleep(1)
#  1  ---End
'''

  
# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!') 
  
# input time in seconds 
t = input("Enter the time in seconds: ") 

# function call 
countdown(int(t)) 


'''
ns_time_int = time.time_base(units='ns', type=int)
ms_time_dec = time.time_base(units=1e-6, type='Decimal')
s_time_float= time.time_base(units=1, type=float)  # This is identical to the existing "time" functions
ns_time_int.clock()
ms_time_dec.clock()
Decimal('5174165.999999999')
s_time_float.clock()
ns_time_int.perf_counter()
ms_time_dec.perf_counter()
Decimal('243171477786.264')
s_time_float.perf_counter()

time.time_ns()
time.monotonic_ns()
time.perf_counter_ns()
time.clock_gettime_ns()
time.clock_settime_ns()
'''

