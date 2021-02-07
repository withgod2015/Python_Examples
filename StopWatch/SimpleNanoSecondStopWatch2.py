import time

i = 0
lastTime = time.time_ns()
timer = 0

for i in sample_iteration:
    now = time.time_ns()
    timer += (now - lastTime)
    lastTime = now

    if timer >= 1000000000:
        i+=1
        timer = 0
        print(i)