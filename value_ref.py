import sys
import gc

name = "Steve"


lst = [1,2,3,4]
another = lst
another.append(30)
lst.append(20)

print("Reference another count", sys.getrefcount(another))
#lst = None
del lst
del name
another = None
n = gc.collect()
print("Number of unreachable objects collected by GC: ",n)
#print("Lst ",lst)
print("Another ",another)
print("Reference another count after none", sys.getrefcount(another))
#print("sys.getrefcount(name) ",sys.getrefcount(name))
#name = None
#print("sys.getrefcount(name) ",sys.getrefcount(name))
i = 20
j = i
j = j+1
print("J ",j, " i ",i)