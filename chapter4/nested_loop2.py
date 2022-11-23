count =0
for i in range(5):
    if( i==2):
        break
    for j in range(3):
        print("I ",i, " J ",j)
        count +=1
print("Count ",count)