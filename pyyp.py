import time
f = ["tim.txt"]
while True:
    for i in f:
        f = open(i, "w")
        f.write(str(time.time()))
        f.close()
    time.sleep(20)
