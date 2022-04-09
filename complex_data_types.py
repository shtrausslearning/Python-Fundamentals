# Lists

#List comprehension
[('Hi ' + x) for x in ['Alice', 'Bob', 'Pete']] #['Hi Alice', 'Hi Bob', 'Hi Pete']
[x * y for x in range(3) for y in range(3) if x>y] #[0, 0, 2]

[1, 2, 2].append(4) # [1, 2, 2, 4] 
[2, 4].insert(2,2) # [1, 2, 2, 4] 
[1, 2, 2] + [4] # [1, 2, 2, 4]
[1, 2, 2, 4].remove(1) # [2, 2, 4]
[1, 2, 3].reverse() # [3, 2, 1]
[2, 4, 2].sort() # [2, 2, 4]
[2, 2, 4].index(2) # 0
[2 , 2, 4].index(2,1) #1

# Lists as Stacks

stack = [3]
stack.append(42) # [3, 42]
stack.pop() # 42 (stack: [3])
stack.pop() # 3 (stack: [])

# Sets

# A set is an unordered collection of unique elements (at-most-once)

basket = {'apple' , 'eggs', 'banana', 'orange'}
same = set(['apple', 'eggs', 'banana', 'orange'])
print(basket == same) # True

# Set comprehension
squares = { x**2 for x in [0,2,4] if x < 4} # {0, 4}

# Dictionary

# A useful data structure for storing (key, value) pairs

calories = {'apple' : 52,
            'banana' :89,
            'choco' : 546}
c = calories

print(c['apple'] < c['choco']) # True
c['cappu'] = 74
print(c['banana'] < c['cappu']) #False
print('apple' in c.keys()) # True
print(52 in c.values()) # True

calories = {'apple' : 52,
            'banana' :89,
            'choco' : 546}

# Looping Over Dictionary
for k, v in calories.items():
  print(k) if v > 500 else None # 'choco'
  
# Classes
  
class Dog:
  """ Blueprint of a dog """

  # class variable for all instances
  species = ["canis lupus"]

  # Attributes upon class instantiation
  def __init__(self, n, c):
    self.name = 
    self.state = "sleeping"
    self.color = c

  def command(self, x):
    if x == self.name:
      self.bark(2)
    elif x == "sit":
      self.state = "sit"
    else:
      self.state = "wag tail"

  def bark(self, freq):
    for i in range(freq):
      print(self.name + ": Woof!")

bello = Dog("bello", "black")
alice = Dog("alice", "white")

print(bello.color) # black
print(alice.color) # white

bello.bark(1) # bello: Woof!

alice.command("sit")
print("alice: " + alice.state) # alice: sit

bello.command("no")
print("bello: " + bello.state) # bello: wag tail

alice.command("alice") # alice: Woof! 
                       # alice: Woof!

bello.species += ["wulf"]
print(len(bello.species) == len(alice.species)) # True (!)
