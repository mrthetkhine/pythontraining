lst = list(range(0,10))
for i in range(len(lst)):
    lst[i] = lst[i]*2
print("Lst ",lst)

lst = [x*x for x in range(0,10)]
print("Lst ",lst)

another = [x for x in lst if x % 2 ==0 ]
print("Another ",another)