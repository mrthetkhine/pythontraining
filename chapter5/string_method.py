str1 = 'hello good morning good'
print('str1.find("good") ',str1.find("good"))
print('str1.find("good1") ',str1.find("good1"))
print('str1.rfind("good") ',str1.rfind("good"))
print('str1.find("good",10) ',str1.find("good",10))

index = str1.find("good")
str_start_from_good = str1[index:]
print("string after good =>",str_start_from_good)
#print('str1.index("good1") ',str1.index("good1"))
print("At the end of program")