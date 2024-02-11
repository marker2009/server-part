a = int(input())
ol = 0
m = []
for i in range(a):
    buf = int(input())
    if buf % 6 == 0 and buf % 10 == 4:
        ol += 1
        m.append(buf)
if ol == 0:
    print("НЕТ")
else:
    print(ol)
    for i in range(ol):
        print(m[i])
