my_list = [100,-2,3,4,5,1]
another = my_list

print("Id my_list",id(my_list))
print("Id another ",id(another))

another[0] = 200
print("My_list ",my_list)
print("another ",another)

#another = my_list[:]
another = my_list.copy()
print("Id my_list",id(my_list))
print("Id another ",id(another))

another[0] = 400
print("My_list ",my_list)
print("another ",another)

thrid = my_list+ another
print("third ",thrid)

print("My_list ",my_list)
print("another ",another)

fourth = my_list*3
print("fourth ",fourth)
print("My_list ",my_list)