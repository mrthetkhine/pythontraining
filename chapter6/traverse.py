lst = [10,20,30,40,50,60]
for item in lst: # item = lst[index]
    print("Item ",item)
    item = item * 2
print("Lst ",lst)

for index in range(len(lst)): 
    print("Item ",lst[index])
    lst[index] = lst[index] * 2
print("Lst ",lst)