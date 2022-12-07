counter =0
total = 0
while( counter <=100):
    total += counter
    print("Counter ",counter)
    counter += 10
print("Total ",total)

lst = range(0,101,10)
print("Total ",sum(lst))