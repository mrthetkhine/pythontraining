lst = [1,20,10,2,1,20]
my_set = {1,1,2,3,2,4}
my_set.add(10)
my_set.add(20)
my_set.remove(1)
print("Set ",my_set)

my_set = set(lst)
print("Set ",my_set)
lst = list(my_set)
print("Non duplicate ",lst)


my_frozen_set = frozenset({1,2,3})
#my_frozen_set.add(4)
print("My_frozen set ",my_frozen_set)

lst = []
empty_set = set(lst)
print("Empty set ",empty_set)