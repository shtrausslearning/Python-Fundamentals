### 3 | Class Method Implementation

- Create a class <code>Employee</code> & create an instance object <code>Tim</code>
- Then print the <code>properties</code> of class <code>Tim</code>

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

#### 1. Method overloading

- Overloaded methods are compiled faster compared to different methods,
- Allows to implement <code>polymorphism</code>
- We have a cleaner OOP style code

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