name_ip = ('localhost','127.0.0.1')
dns = ('128.1.2.4','128.1.3.4')

another = name_ip + dns
print("another ",another)

t = (100,-2,3,49,22)
sorted_t = sorted(t)
print("T ",t)
print("Sorted t ",sorted_t)

my_list = list(t)
print("My_list ",my_list)
t = tuple(my_list)
print("T ",t)