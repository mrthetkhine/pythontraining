num = int(input("enter number "))

sum = 0
while (num != 0):
    n = (num %10)
    print("Add ",n)
    sum += n
    num = int(num / 10)
print("Total of num ",sum)