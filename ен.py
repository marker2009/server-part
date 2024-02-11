import dill
mas1 = []
ans1 =[ ]
for i in range(1,42):
    dill.load_session(str(i)+".pkl")
    mas1.append(buf)
    ans1.append(buf1)
    print(buf, buf1)
print(mas1)
print(ans1)
