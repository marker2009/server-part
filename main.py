buf = int(input())
ol = 0
while buf != 0:
    su = 0
    buf1 = buf
    while buf1 != 0:
        su += buf1 % 10
        buf1 = buf1 // 10
    if su % 6 == 0:
        ol += 1
    buf = int(input())
print(ol)
