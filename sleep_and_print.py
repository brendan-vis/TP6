import time

def count():
    for i in range (10):
        print(i)
        time.sleep(0.5)


for _ in range (2):
    task = count()
