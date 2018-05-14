
for i in range(10000, 100000):
    s = 0
    for n in str(i):
        s += int(n)**5
    if s == i:
        list.append(s)
print(sum(list))
