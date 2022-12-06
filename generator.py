def gen(n):
    for i in range(n):
        yield i
print(gen(100000))
for i in gen(10000):
    print(i)