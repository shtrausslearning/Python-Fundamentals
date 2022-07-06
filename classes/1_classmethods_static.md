
### Defining a Class

```python
class Employee:
    
    # Constructor
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # class method; calcuate tax to be deduced from salary
    def tax(self):
        return (self.salary * 0.2)

    # class method; calculate daily salary
    def salaryPerDay(self):
        return (self.salary / 30)
    
# create an object of the Employee class
Tom = Employee(654, 100, "Engineering")
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

- Method <code>overloading</code> example

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
print("Demo 1")
Tom.overload(1, 2, 3)
print("\n")

print("Demo 2")
Tom.overload(1, 2, 3, 4)
print("\n")
```

# Class Methods

class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())

# Static Methods

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


