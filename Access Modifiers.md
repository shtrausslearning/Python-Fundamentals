### 5 | Access Modifiers

#### 1. Public attributes

- <code>Public attributes</code> are those that can be **accessed inside the class and outside the class**

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

#### 2. Private attributes

- <code>Private attributes</code> cannot be accessed directly from outside the class but can be accessed from inside the class

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

#### 3. Private methods

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

#### 4. Accessing private attributes

- If we absolutely needed to access the private attributes, python can't actually prevent us
- We simply write the instance <code>object name</code> + <code>_classname</code> + <code>private attribute</code>

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
