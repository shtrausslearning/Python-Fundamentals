## 6 | Class Inheritance 

### 1. Basic Syntax 

- Basic syntax of class inheritance 

```python

class ParentClass:
    # attributes of the parent class

class ChildClass(ParentClass):
    # attributes of the child class

```

### 2. Example Implementation

- Vehicle is the <code>parent</code> class
- Automobile is the <code>child</code> class

```python

# Parent class
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

# Child class 
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

### 3. Using SUPER with initialisers

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

### 4. Types of Inheritences

There are a couple of ways we can structure class inheritance:

- <code>single</code> 
- <code>Multi-level</code>
- <code>Hierarchical</code>
- <code>Multiple</code>
- <code>Hybrid</code>

#### SINGLE INHERITANCE

- <code>Vehicle</code> <- <code>Automobile</code> (sequential)
- Instantiate <code>child</code> class & access parent class <code>methods</code>

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


honda = Automobile()    # creating an object of the Car class
honda.setTopSpeed(4)    # accessing methods from the parent class
honda.openTrunk()       # accessing method from its own class

```

#### MULTI-LEVEL INHERITANCE

- <code>Vehicle</code> <- <code>Automobile</code> <- <code>Electric</code> (Sequential)
- Instantiate the <code>child</code> class and access method from the <code>two parent</code> classes before it

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


Tesla = Electric()        # creating an object of the Hybrid class
Tesla.setDoors(4)         # accessing methods from the parent class
Tesla.openTrunk()         # accessing method from the parent class
Tesla.turnOnBattery()     # accessing method from the child class

```

```
Number of Doors: 4
Trunk is now open
Battery has been turned on
```

#### HIERARCHICAL INHERITANCE

- <code>Vehicle</code> <- [<code>Automobile</code>,<code>Motocycle</code>]
- Two <code>child</code> classes inherit one <code>parent</code> class 

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

- Two <code>parent</code> classes, one <code>child</code> class inherits both <coed>parents</code>

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