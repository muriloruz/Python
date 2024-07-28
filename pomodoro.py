import time

def contTime(sec):
    for i in range(1,sec+1):
        print(i)
        time.sleep(1)

contTime(9)