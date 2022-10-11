num = 10
print("Bin(10)  ",bin(num))
print("Oct(10)  ",oct(num))
print("Hexa(10)  ",hex(num))

my_str = "50"
result = my_str * 2
print("result ",result)
total = int(my_str) * 2
print("Total ",total , " type total ",type(total))

my_str = "50.12"
result = float(my_str)
print("Result ",result)

print("5/2 ", int(5/2))
print("int(False )",int(False ))
print("int(True )",int(True ))

print("Bool(100 )",bool(100 ))
print("Bool(0 )",bool(0 ))
print("Bool(-2 )",bool(-2 ))
print("Bool('hello' )",bool('hello'))
print("Bool('' )",bool(''))
print("Bool('False' )",bool('False'))
print("Bool(' ' )",bool(' '))

print('str(100)*5 ',str(100)*5)

arr = [10,20,30]
b = bytes(arr)
print("Bytes ",b)
print("BytesArray ",bytearray(arr))