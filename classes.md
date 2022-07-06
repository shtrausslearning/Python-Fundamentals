## Python Class Operations

What the notebook covers:
- Initialsing Objects
- Class & Instance Variables 
- Class Method Implementation
- Class/Static Methods
- Access Modifiers
- Class Inheritance
- Polymorphism

### 1 | Initialising Objects

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

### 2 | Class & Instance Variables 

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

- Printing <code>properties</code> of class instance <code>Tom</code>

```python
# Printing properties of instance Tom
print("ID =", Tom.ID)
print("Salary", Tom.salary)
print("Department:", Tom.department)
print("Tax paid by Steve:", Tom.tax())
print("Salary per day of Steve", Tom.salaryPerDay())
```

### 3 | Class Method Implementation

```python

class Employee:
    
    # constructor
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # calcuate the tax portion of the salary
    def tax(self):
        return (self.salary * 0.2)

    # calcualte salary per day
    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Tim = Employee(213, 100, "data science")

# Printing properties of Steve
print("ID =", Tim.ID)
print("Salary", Tim.salary)
print("Department:", Tim.department)
print("Tax paid by Steve:", Tim.tax())
print("Salary per day of Steve", Tim.salaryPerDay())

```

```

ID = 213
Salary 100
Department: data science
Tax paid by Steve: 20.0
Salary per day of Steve 3.3333333333333335

```

#### METHOD OVERLOADING

- Overloaded methods are compiled faster compared to different methods,
- Allows to implement <code>polymorphism</code>
- We have a cleaner code

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

### 4 | Class/Static Methods

#### CLASS METHODS

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

#### STATIC METHODS
- <code>static</code> methods do not know anything about the state of the class

```python
class Employee:
    
    companyName = 'Microsoft'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def Entered():
        print("Entered the building")

p1 = Employee('Tim')
p1.Entered()
Employee.Entered()
```

```
Entered the building
Entered the building
```

### 5 | Access Modifiers

#### PUBLIC ATTRIBUTES

- Public attributes are those that can be accessed inside the class and outside the class

```python
class Employee:
    
    # all properties are public
    def __init__(self, ID, salary):
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Tim = Employee(2342, 1000)
Tim.displayID()
print(Tim.salary)

```

```
ID: 2342
1000
```

#### PRIVATE ATTRIBUTES

- Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class

```python
class Employee:

    def __init__(self, ID, salary):
        self.ID = I'D # public property
        self.__salary = salary  # salary is a private property/attribute

Tim = Employee(3789, 2500)
print("ID:", Tim.ID)
print("Salary:", Tim.__salary)  # error
```

```
 File "/tmp/ipykernel_33/910573642.py", line 4
    self.ID = I'D # public property
                                   ^
SyntaxError: EOL while scanning string literal
```

#### PRIVATE METHODS

- Like <code>attributes</code>, <code>methods</code> can also be private

```python

class Employee:
    
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    # showSalary is a public method
    def showSalary(self): 
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(2131,1000)
Steve.showSalary()
Steve.__displayID()  # this will generate an error

```

```
1000
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/tmp/ipykernel_33/2274506191.py in <module>
     15 Steve = Employee(2131,1000)
     16 Steve.showSalary()
---> 17 Steve.__displayID()  # this will generate an error

AttributeError: 'Employee' object has no attribute '__displayID'

```

#### ACCESSING PRIVATE ATTRIBUTES

- If we absolutely needed to access the private attributes, python can't actually prevent us

```python
class Employee:
    def __init__(self, ID, salary):
    
        self.ID = ID
        self.__salary = salary  # salary is a private property/attribute


Tim = Employee(123, 1000)
print(Tim._Employee__salary)  # accessing a private property/attribute
```

```
1000
```

### 6 | Class Inheritance 

#### SYNTAX

```python

class ParentClass:
    # attributes of the parent class

class ChildClass(ParentClass):
    # attributes of the child class

```

#### EXAMPLE IMPLEMENTATION

- Vehicle is the <code>parent</code> class
- Automobile is the <code>child</code> class

```python

class Vehicle:

    # Parent Class Constructor
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    # Parent Class Method
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Automobile(Vehicle):
    
    # Automobile Constructor
    def __init__(self,make,color,model,doors):
        
        # Call the parent class constructor
        Vehicle.__init__(self,make,color,model)
        self.doors = doors

    # Child Class Method
    def printAutomobileDetails(self):
        self.printDetails()
        print("Doors:", self.doors)

obj = Automobile("Honda", "Red", "2000", 5)
obj.printAutomobileDetails()

```

#### SUPER FUNCTION

```python

# Parent Class
class Automobile:  
    
    doors = 2  # parent class variable

# Child class
class Sedan(Vehicle):  
    
    doors = 5 # child class variable

    def display(self):
        
        # accessing fuelCap from the Vehicle class using super()
        print("Doors from the Automobile Class:", Automobile.doors)

        # accessing fuelCap from the Car class using self
        print("Doors from the Sedan Class:", self.doors)


obj1 = Sedan()  # creating a car object
obj1.display()  # calling the Car class method display()


```

```
Doors from the Automobile Class: 2
Fuel cap from the Sedan Class: 5
```

- Calling the <code>parent</code> class method from the <code>child</code> class via <code>super</code>

```python

# Parent Class
class Vehicle:  
    
    def display(self):  # defining display method in the parent class
        print("Vehicle Class Method")

# Child Class
class Automobile(Vehicle):  # defining the child class 
    
    # child class method
    def display(self):
        super().display()  
        print("Automotive Class Method")

obj1 = Automobile()    # creating a automobile object
# obj1.display()       # calling the automobile class method

```

#### USING SUPER WITH INITIALISERS

```python

class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Automobile(Vehicle):
    
    # Constructor, calls parent constructor as well
    def __init__(self, make, color, model, doors):
#         super().__init__(make, color, model)         # can use super()
        Vehicle.__init__(self,make, color, model)      # or just parent class name 
        self.doors = doors

    # Child class method calls parent class method
    def printAutomobileDetails(self):
        self.printDetails()
        print("Door:", self.doors)


obj1 = Automobile("Honda", "Red", "2000", 5)
obj1.printAutomobileDetails()

```

#### TYPES OF INHERITANCES

There are a couple of ways we can structure class inheritance:
- <code>single</code> 
- <code>Multi-level</code>
- <code>Hierarchical</code>
- <code>Multiple</code>
- <code>Hybrid</code>

#### SINGLE INHERITANCE

```python

# Parent Class
class Vehicle: 
    
    def setTopSpeed(self, speed): 
        self.doors = speed
        print("Number of Doors:", self.doors)

# Child Class
class Automobile(Vehicle): 
    
    def openTrunk(self):
        print("Trunk is now open")


honda = Automobile()           # creating an object of the Car class
honda.setTopSpeed(4)         # accessing methods from the parent class
honda.openTrunk()             # accessing method from its own class

```

#### MULTI-LEVEL INHERITANCE

```python

# Parent Class 
class Vehicle: 
    
    def setDoors(self, doors): 
        self.doors = doors
        print("Number of Doors:", self.doors)

# Child Class of Class Vehicle 
class Automobile(Vehicle): 
    
    def openTrunk(self):
        print("Trunk is now open")


# Child Class of Class Automobile
class Electric(Automobile):  # child class of Car
    
    # Class method 
    def turnOnBattery(self):
        print("Battery has been turned on")


Tesla = Electric()       # creating an object of the Hybrid class
Tesla.setDoors(4)         # accessing methods from the parent class
Tesla.openTrunk()      # accessing method from the parent class
Tesla.turnOnBattery()  # accessing method from the child class

```

```
Number of Doors: 4
Trunk is now open
Battery has been turned on
```

#### HIERARCHICAL INHERITANCE

```python

# Parent Class
class Vehicle: 
    
    # Class method of Parent Class
    def setTopSpeed(self, speed):  
        self.topSpeed = speed
        print("Top Speed ", self.topSpeed)


# Child Class of Vehicle
class Automobile(Vehicle):  
    pass

# Child Class of Vehicle
class Motocycle(Vehicle): 
    pass

Tesla = Automobile()  # creating an object of the Car class
Tesla.setTopSpeed(150)  # accessing methods from the parent class

Honda = Motocycle()  # creating an object of the Truck class
Honda.setTopSpeed(100)  # accessing methods from the parent class

```

#### MULTIPLE INHERITANCE

```python

# Parent Class #1 for class HybridEngine
class CombustionEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

# Parent Class #2 for Class HybridEngine
class ElectricEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child Class inherits from both CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()

```

```
Tank Capacity: 20 Litres
Charge Capacity: 250 W
```

#### HYBRID INHERITANCE

- Type of inheritance which is a combination of <code>Multiple</code> and <code>multi-level</code> inheritance 

```python

# Parent Class
class Engine:  # Parent class
    def setPower(self, power):
        self.power = power

# Child Class of Class Engine
# Parent Class for class Hybrid Engine
class CombustionEngine(Engine):  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

# Child Class of Class Engine
# Parent Class for class HybridEngine
class ElectricEngine(Engine):  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setChargeCapacity("100 W")
car.setTankCapacity("10 Litres")
car.printDetails()
```

```
Tank Capacity: 10 Litres
Charge Capacity: 100 W
```

#### EXAMPLE 

```python

# parent class 
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


# child class 
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)  # instantiate parent class; get access
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate)/100

# create savings account
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object

```

### 7 | Polymorphism 

#### SIMPLE CASE OF POLYMORPHISM

- Say we have two classes <code>Rectangle</code> & <code>Circle</code>
- They both look like they have the same method <code>getArea</code>, but different methods are called. 
- Thus, we have achieved polymorphism.

```python

# Class Rectangle
class Rectangle():

    # Constructor
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)

# Class Circle
class Circle():
    
    # Constructor
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.1419)


shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))

```

#### POLYMORPHISM VIA INHERITANCE

- The getArea() method returns the area of the respective shape. 
- This is Polymorphism: 
    - Having unique implementations of the same methods for each class

```python

# Parent Class
class Shape:
    
    # Parent class constructor
    def __init__(self): 
        self.sides = 0

    def getArea(self):
        pass

# Child class of parent class Shape
class Rectangle(Shape):  
    
    # constructor
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)

# Child class of parent class Shape
class Circle(Shape):  
    
    # constructor
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(3, 5), Circle(3)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))

```

```
Area of rectangle is: 15
Area of circle is: 28.278
```
