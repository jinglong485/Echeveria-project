import time
while True:
    print(time.strftime('%H%M%S',time.localtime()))
    print(time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime()))
    time.sleep(1)