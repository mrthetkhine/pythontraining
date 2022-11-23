a = 1
while a <= 5:
    print("A is ",a)
    a += 1
print("end of while ",a)
lst = [10,20,-5,200,37,22] 

item_to_find = 200
index = 0
found = False
while (not found) and (index <= len(lst)-1) :
    if lst[index] == item_to_find:
        print("Found at index ",index)
        found = True
        break
    index += 1
print("Found ",found , " Index ",index)