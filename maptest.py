seq = range(8)
seq1 = range(19)
def add(x,y):
    return x+y

print(list(map(add,seq,seq)))  #即效果是两个list对应每一位相加


print(list(map(add,seq,seq1))) #即列表长度不一致只显示到较短列表的长度