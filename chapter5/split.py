str1 = '127.0.0.124,127.0.0.2'
addresss = str1.split(',')
print("Type ",type(addresss))
for add in addresss:
    print("Add ",add)
    print("Last no ", add.split(".")[3])