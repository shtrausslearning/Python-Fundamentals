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
