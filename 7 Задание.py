def fibo_gen():
    pr = 1
    for el in range(1, 16):
        pr = pr*el
        yield pr
for el in fibo_gen():
    print(el, end= ' ')