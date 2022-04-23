# Sets are an unordered collection of unique elements, 
# which means any duplicates are automatically removed. 
# Sets allow you to do operations:
# - union, 
# - intersection,
# - difference
# - symmetric difference

# dir
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'] 

my_set = set()
my_set.add(1)
my_set.update([2,1])
my_set.add(5.4)
my_set.add((5.2,6.3))
my_set.discard(5.4)
my_set.remove((5.2,6.3))
# Note that the set only contains a single 1 value
print(f'set1: {my_set}')
# set1: {1, 2}

my_set2 = set()
my_set2.add(1)
my_set2.add(2)
my_set2.add(3)
my_set2.add(4)
print(f'set2: {my_set2}')
# set2: {1, 2, 3, 4}

# Prints the overlap ( & operator )
print(my_set.intersection(my_set2))
# {1, 2}

# Prints the combination ( | operator )
print(my_set.union(my_set2))
# {1, 2, 3, 4}

# Prints the difference (those in my_set but not my_set2) ( - operator )
print(my_set.difference(my_set2))
# set() (empty set)

# define set w/ set(), as {} is an empty dictionary
# elements can be of different data types

# sets are immutable; string, int, tuple, floats
# can't contain lists & dictionaries

# > Multiple Operations

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

a.difference(b, c)
# {1, 2, 3}

a - b - c
# {1, 2, 3}

# > Symmetric Difference (no common elements)
# returns the set of all elements in either x1 or x2, but not both:

>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

x1.symmetric_difference(x2)
# {'foo', 'qux', 'quux', 'bar'}

x1 ^ x2
# {'foo', 'qux', 'quux', 'bar'}
