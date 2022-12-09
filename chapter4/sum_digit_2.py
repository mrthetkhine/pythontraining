num = int(input("enter number "))

if(num <0 ):
    num *= -1

num = str(num)
sum = 0
for ch in num:
    sum+=int(ch)
print("Total of num ",sum)