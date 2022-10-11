lst = [10,20,30,40,50,"False"]
print("list ",lst, ' type ',type(lst))
print("list [0]",lst[0])
print("last element list",lst[-1])

#print("total ",sum(lst))
print("lst[2:] ",lst[2:])

lst.append("Hello")
lst.remove(20)
for item in lst:
    print("Item ",item)