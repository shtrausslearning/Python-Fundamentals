### 4 | Class/Static Methods

#### 1. Class method

- Create a class <code>Employee</code>, which contains a class method @classmethod <code>getCompanyName</code>

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

#### 2. Static methods
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
