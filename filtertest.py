def f(x):
    return x % 3 == 0 or x %5 == 0

print(list(filter(f,range(3,25)))) #filter是一个interator(迭代器)，无法直接打印，需要转换成list


