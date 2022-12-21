my_str = "Mississippi"
print("my_str count ",my_str.count('s'))
my_list = list(my_str)
print("Count ",my_str.count('s'))
print("index ",my_str.index('s'))
print("find k",my_str.find('k'))

num_upto_30 = range(0,31,5)
my_list = []
for num in num_upto_30:
    #print("Item ",num)
    my_list.append(num)
print("my_list ",my_list)
print("my_list ",sum(my_list))