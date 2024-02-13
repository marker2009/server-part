def f(x):
    return 300 - (300 / x + 1 ) * (x - 10)
mi = [1000000, 0]
for i in range(1, 1000000):
    buf = i / 10000
    mi = min(mi, [abs(f(buf)), buf])

    if f(buf) == 0:
        print(buf)
print(mi)
print(f(60))
