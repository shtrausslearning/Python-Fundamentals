## Arithmetic Operations
x, y = 3, 2
print(x + y) # = 5
print(x - y) # = 1
print(x * y) # = 6
print(x / y) # = 1.5

print(x // y) # = 1
print(x % y) # = 1
print(-x) # = -3
print(abs(-x)) # = 3
print(int(3.9)) # = 3
print(float(3)) # = 3.0
print(x ** y) # = 9

## Key String Methods
y = " This is lazy\t\n"
print(y.strip()) # 'This is lazy'
print("DrDre".lower()) # 'drdre
print("stop".upper()) # 'STOP'
s = "smartphone"
print(s.startswith("smart")) # True
print(s.endswith("phone")) # True
print("another".find("other")) # 2
print("cheat".replace("ch", "m")) # 'meat'
print(','.join(["F", "B", "I"])) # 'F,B,I'
print(len("Rumpelstiltskin")) # 15
print("ear" in "earth") # True

# Evaluated as False 
if (None or 0 or 0.0 or '' or [] or {} or set()):
  print("Dead code")

# Evaluated as True
if (1 < 2 and 3 > 2 and 2 >= 2 and 1 == 1 and 1 != 0):
  print("True")
  
## Index & Slicing 
  
s = "The youngest pope was 11 years old"
print(s[0]) # 'T
print(s[1:3]) # 'he'
print(s[-3:-1]) # 'ol'
print(s[-3:]) # 'old'
x = s.split() # string array
print(x[-3] + " " + x[-1] + " "+ x[2] + "s") # '11 old popes'
