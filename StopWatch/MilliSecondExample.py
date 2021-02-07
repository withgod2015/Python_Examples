#
# url : https://cnpnote.tistory.com/entry/PYTHON-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%ED%98%84%EC%9E%AC-%EC%8B%9C%EA%B0%84%EC%9D%84-%EB%B0%80%EB%A6%AC-%EC%B4%88-%EB%8B%A8%EC%9C%84%EB%A1%9C-%EA%B0%80%EC%A0%B8-%EC%98%B5%EB%8B%88%EA%B9%8C

import time
from datetime import datetime

millis = int(round(time.time() * 1000))
print(millis)
current_milli_time = lambda: int(round(time.time() * 1000))
print(current_milli_time())

dt = datetime.now()
dt.microsecond
print(dt.microsecond)

def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 

#TimestampMillisec64()

def millis():
    return int(round(time.time() * 1000))


print(millis())


start_time = datetime.now()

# returns the elapsed milliseconds since the start of the program
def millis2():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

print(millis2())

timestamp = int(time.time()*1000.0)
print(timestamp)

def get_epochtime_ms():
    return round(datetime.datetime.utcnow().timestamp() * 1000)

#get_epochtime_ms()

d = datetime.now()
print(d.microsecond/1000 + d.second*1000)