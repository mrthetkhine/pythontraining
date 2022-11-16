a = 10
b = 5
a += b # a= a + b
print("A ",a) #a 15, b = 5
temp = a
a = b
b = temp

print("A ",a, " B ",b)
a,b = b,a
print("A ",a, " B ",b)