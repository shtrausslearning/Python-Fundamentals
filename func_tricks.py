# MAP FUNCTION

# map(func, iter)
list(map(lambda x: x[0], ['red', 'green', 'blue'])) 
# Result: ['r', 'g', 'b']

# map(func, i1, ..., ik)
list(map(lambda x, y: str(x) + ' ' + y + 's' , [0, 2, 2], ['apple', 'orange', 'banana']))
# Result: ['0 apples', '2 oranges', '2 bananas']

# STRING FUNCTIONS 

# string.join(iter)
' marries '.join (list(['Alice', 'Bob']))
# Result: 'Alice marries Bob'

# string.strip()
print("\n \t 42 \t ".strip()) # Result: 42

# SORTING FUNCTIONS 

# sorted(iter)
sorted([8, 3, 2, 42, 5]) # Result: [2, 3, 5, 8, 42]

# sorted(iter, key=key)
sorted([8, 3, 2, 42, 5], key=lambda x: 0 if x==42 else x) 
# [42, 2, 3, 5 ,8]

# FILTER 

list(filter(lambda x: True if x>17 else False, [1, 15, 17, 18])) # Result: [18]

# HELP FUNCTION

help(str.upper) # Result: '... to upercase.'

# ZIP FUNCTION (zip & unzip)

list(zip(['Alice', 'Anna'], ['Bob', 'Jon', 'Frank'])) # Result: [('Alice', 'Bob'), ('Anna'), 'Jon)]
list(zip(*[('Alice', 'Bob'), ('Anna', 'Jon')])) # Result: [('Alice', 'Anna'), ('Bob', 'Jon')]

# ENUMERATE 

list(enumerate(['Alice', 'Bob', 'Jon']))
#Result: [(0, 'Alice), (1, 'Bob'), (2, 'Jon')]

# SWAPPING VARIABLES

a, b = 'Jane', 'Alice'
a, b = b, a
#Result: a = 'Alice', b = 'Jane'

# UNPACKING ARGUMENTS

def f(x, y, z):
  return x + y * z

f(*[1, 3, 4]) # 13
f(**{'z' : 4, 'x' : 1, 'y' : 3}) # 13

list(enumerate(['Alice', 'Bob', 'Jon']))
#Result: [(0, 'Alice), (1, 'Bob'), (2, 'Jon')]

# EXTENDED UNPACKING 

a, *b = [1, 2, 3, 4, 5]
#Result: a = 1, b = [2, 3, 4, 5]

# MERGING DICTIONARIES

x={'Alice' :18}
y={'Bob' : 27, 'Ann' : 22}
z = {**x,**y}
# Result: z = {'Alice': 18, 'Bob': 27, 'Ann': 22}
