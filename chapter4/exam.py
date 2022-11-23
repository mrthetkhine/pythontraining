PASSED_MARK = 50
DISTINCTION_MARK = 75

sre_mark = (int)(input("Enter sre mark: "))

if(sre_mark >= PASSED_MARK):
    if(sre_mark >= DISTINCTION_MARK):
        print("You got distinction")
    else:
        print("You passed the exam")
else:
    print("Failed")
print("After if")