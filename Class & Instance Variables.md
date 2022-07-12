### 2 | Class & Instance Variables 

#### 1. Create class instances with class variables

- <code>company</code> class variable
- <code>name</code> instance variable 

```python
class Employee:
    
    company = 'Microsoft'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Employee('Tim')
p2 = Employee('Tom')

print("Name:", p1.name)
print("Team Name:", p1.company)
print("Name:", p2.name)
print("Team Name:", p2.company)
```

#### 2. Wrong use of class variables 

- Class variables are shared **between all instances/objects** created with <code>Employee</code>

```python
class Employee:
    
    formerEmployer = []  # class variables
    companyName = 'Microsoft'
    
    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Employee('Tim')
p2 = Employee('Tom')

p1 = Employee('Tim')
p1.formerEmployer.append('Apple') # wrong use of class variable
p2 = Employee('Tom')
p2.formerEmployer.append('IBM') # wrong use of class variable

print("Name:", p1.name)
print("Employer Name:", p1.companyName)
print(p1.formerEmployer)
print("Name:", p2.name)
print("Team Name:", p2.companyName)
print(p2.formerEmployer)

```

```
Name: Tim
Employer Name: Microsoft
['Apple', 'IBM']
Name: Tom
Team Name: Microsoft
['Apple', 'IBM']
```

#### 3. Right uses of class variables 

```python

class Employee:
    
    companyName = 'Microsoft'
    
    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerEmployer = []


p1 = Employee('Tim')
p2 = Employee('Tom')

p1 = Employee('Tim')
p1.formerEmployer.append('Apple') # wrong use of class variable
p2 = Employee('Tom')
p2.formerEmployer.append('IBM') # wrong use of class variable

print("Name:", p1.name)
print("Employer Name:", p1.companyName)
print(p1.formerEmployer)
print("Name:", p2.name)
print("Team Name:", p2.companyName)
print(p2.formerEmployer)

```

```
Name: Tim
Employer Name: Microsoft
['Apple']
Name: Tom
Team Name: Microsoft
['IBM']
```

```python

class Employee:
    
    companyName = 'Microsoft'
    coworkers = []
    
    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerEmployer = []
        self.coworkers.append(self.name)

p1 = Employee('Tim')
p2 = Employee('Tom')

print("Name:", p1.name)
print("Employer Name:", p1.companyName)
print(p1.coworkers)
print("Name:", p2.name)
print("Team Name:", p2.companyName)
print(p2.coworkers)

```

```
Name: Tim
Employer Name: Microsoft
['Tim', 'Tom']
Name: Tom
Team Name: Microsoft
['Tim', 'Tom']
```

- Printing <code>properties</code> of class instance <code>Tom</code>

```python
# Printing properties of instance Tom
print("ID =", Tom.ID)
print("Salary", Tom.salary)
print("Department:", Tom.department)
print("Tax paid by Steve:", Tom.tax())
print("Salary per day of Steve", Tom.salaryPerDay())
```