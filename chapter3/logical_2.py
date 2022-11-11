def getTrue():
    print("Get true")
    return True

def getFalse():
    print("Get False")
    return False

print("getFalse and getTrue ", getFalse() and getTrue())
print("getTrue and getFalse ", getTrue() and getFalse())
print("'hello' and getFalse ", 'hello' and getFalse())

print("getFalse or getTrue ", getFalse() or getTrue())
print("getTrue or getFalse ", getTrue() or getFalse())
print("'hello' or getFalse ", 'hello' or getFalse())