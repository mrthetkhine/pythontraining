my_list = [1,2,3,4,5]
my_list.insert(-2,100)
print("my_list ",my_list)

another_list = [200,300]
my_list.extend(another_list)
print("my_list ",my_list)
print("another ",another_list)

my_list.remove(5)
print("my_list ",my_list)

#my_list.remove(-5)
print("my_list ",my_list)