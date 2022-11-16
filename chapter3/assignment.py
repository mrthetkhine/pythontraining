a = 3
b = 4
print("A ",a)
print("b ",b)

a = b # value semantics
a +=1
print("A ",a)
print("B ",b)

lst = [1,2,3,4]
lst2 = lst #reference semantics
lst2.append(5)
print("Lst ",lst)
print("Lst2 ",lst2)

lst2 = [10,20]
lst2.append(30)
print("Lst ",lst)
print("Lst2 ",lst2)