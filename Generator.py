def f_gen(m):
    s = 1
    for n in range(1,m):
        yield n**2 + s
        s += 1
a = f_gen(5)


for i in a:
    print(i)