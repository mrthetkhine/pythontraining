
str = "Hello World"
print(str*4)
print("Char at 0 ",str[0])
print("Char at 10 ",str[10])

print("Char at -1 ",str[-1])
print("Char at -2 ",str[-2])

print("Char [1:3] ",str[1:3])
print("Char [:3] ",str[:3])
print("Char [2:] ",str[2:])

authorization_header = "Barer ee9e99e"
print("String len ",len("Barer "))
token  = authorization_header[len("Barer "):]
print("JWT ",token)

print("5/2 ", (5/2))