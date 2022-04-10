# Various Python Functions (Advanced)
# Разные Питоновские операции 

# MAP FUNCTION

# map(func, iter)
list(map(lambda x: x[1], ['red', 'green', 'blue'])) 
#Result: ['e', 'r', 'l']

# map(func, i1, ..., ik)
list(map(lambda x,y: str(x) + ' ' + y + 's' , [0, 2, 2], ['blue', 'red', 'green']))
#Result: ['0 blue', '2 red', '2 green']

# STRING FUNCTIONS 

# string.join(iter)
' and '.join (list(['Ally', 'Emma']))
#Result: 'Alice and Bob'

# string.strip()
print("\n \t 10 \t ".strip()) 
#Result: 10

# SORTING FUNCTION

# sorted(iter)
sorted([8, 3, 2, 42, 5]) 
#Result: [2, 3, 5, 8, 42]

# sorted(iter, key=key)
sorted([8, 3, 2, 42, 5], 
		key=lambda x: 0 if x==42 else x) 
#Result: [42, 2, 3, 5 ,8]

# FILTER FUNCTION

list(filter(lambda x: True if x>17 else False,
			 [1, 15, 17, 18])) 
#Result: [18]

# ZIP FUNCTION (zip & unzip)

list(zip(['Alice', 'Anna'],
		 ['Emma', 'Laura', 'Annie'])) 
#Result: [('Alice', 'Emma'), ('Anna', 'Laura')]

list(zip(*[('Alice', 'Emma'), ('Anna', 'Laura')])) 
#Result: [('Alice', 'Anna'), ('Emma', 'Laura')]

# ENUMERATE FUNCTION

list(enumerate(['Alice', 'Laura', 'Emma']))
#Result: [(0, 'Alice), (1, 'Laura'), (2, 'Emma')]

# SWAPPING VARIABLES

a, b = 'Emma', 'Alice'
a, b = b, a
#Result: a = 'Alice', b = 'Emma'

# UNPACKING ARGUMENTS

def f(x,y,z):
  return x+y*z

# from list
f(*[1, 3, 4]) 
#Result: 13

# from dictionary
f(**{'z' : 4, 'x' : 1, 'y' : 3}) 
#Result: 13

# ENUMERATE

list(enumerate(['Alice', 'Emma', 'Laura']))
#Result: [(0, 'Alice), (1, 'Emma'), (2, 'Laura')]

# EXTENDED UNPACKING 

a,*b = [1, 2, 3, 4, 5]
#Result: a = 1, b = [2, 3, 4, 5]

# MERGING DICTIONARIES

x={'Anna' :18}
y={'Emma' : 27, 'Laura' : 22}
z = {**x,**y}
#Result: z = {'Anna': 18, 'Emma': 27, 'Laura': 22}
