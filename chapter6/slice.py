lst = [10,20,30,40,50,60]
print("Lst [1:] ",lst[1:])
print("Lst [1:3]",lst[1:3])
print("Lst [1::2]",lst[1::2]) #1,3,5
print("Lst [::2]",lst[::2]) 
print("Lst [::-1]",lst[::-1]) 
print("Lst [-1::-1]",lst[-1::]) 

lst[1]= 50
print("Lst ",lst)

my_str = "Hello"
#my_str[0] ='h'

for item in lst:
    print("Item ",item)