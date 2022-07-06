
### Initialising Objects

#### Defining an initialiser with preset parameters

- Aside from setting instance arguments by themselves (self,ID,salary,department)
- We can set a preset value, which will be used if the objects are created without them

```python

class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

# Creating an object of the Employee class
Tom = Employee()                           # uses default parameters
Tim = Employee("001", 100, "Engineering")  # uses input parameters
```

```python
print("Tom")
print("ID :", Tom.ID)
print("Salary :", Tom.salary)
print("Department :", Tom.department)

print("Tim")
print("ID :", Tim.ID)
print("Salary :", Tim.salary)
print("Department :", Tim.department)

```

```

Tom
ID : None
Salary : 0
Department : None

Time
ID : 3789
Salary : 2500
Department : Human Resources

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

### Class & Instance Variables 

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

#### WRONG USE OF CLASS VARIABLES

- Class variables are shared between all instances/objects created with <code>Employee</code>

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

#### RIGHT USE OF CLASS VARIABLES

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

### Method Overloading

- Overloaded methods are compiled faster compared to different methods,
- especially if the list of methods is long.
- Allows to implement polymorphism
- Cleaner code

```python
class Employee:
    
    # Constructor
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading example
    def overload(self, a, b, c, d=10, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    # class method; calcuate tax to be deduced from salary
    def tax(self, title=None):
        return (self.salary * 0.2)

    # class method; calculate daily salary
    def salaryPerDay(self):
        return (self.salary / 30)


# cerating an object of the Employee class
Tom = Employee()

# Printing properties of Steve
Tom.overload(1, 2, 3)
print("\n")

Tom.overload(1, 2, 3, 4)
print("\n")
```

```
a = 1
b = 2
c = 3
d = 10
e = None


a = 1
b = 2
c = 3
d = 4
e = None
```

### Class Methods

```python
class Employee:
    
    companyName = 'Microsoft'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getCompanyName(cls):
        return cls.companyName
  
print(Employee.getCompanyName())
```

```
Microsoft
```

### Static Methods

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")

p1 = Player('lol')
p1.demo()
Player.demo()


