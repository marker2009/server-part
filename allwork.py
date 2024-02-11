import time
f_nam = ["tim.txt"]
ol = 0
while True:
    for i in f_nam:
        try:
            f = open(i, "r")
            if time.time() - float(f.read()) > 60:
                print("rr in " +  i)
        except Exception as p:
            print("rr in xpt", p)
    time.sleep(2)
    ol += 1
    if ol % 10 == 0:
        print("20 ok")

