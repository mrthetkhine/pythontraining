import random, string
str1 = 'hello'
str2 = 'how are you'
str3 = str1 + str2
print('Str3 ',str3)
str4 = 'hello'*4
print('Str4 ',str4)

password_size = 7
valid_password_text = string.ascii_letters+string.digits
print("String ",string.ascii_letters)

password = ''
for i in range(0,password_size):
    password = password + random.choice(valid_password_text)

print("random password ",password)
str3 = 'hello'+str(3)
print("Str3 len ",len(str3))