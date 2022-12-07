num = int(input("enter number "))
divisors = range(2,num) #2->6 [2,3,4,5,6,7]

for divisor in divisors:
    if(num % divisor == 0):
        print("It is not prime divisable by ",divisor)
        break
else:
    print("It is prime")
