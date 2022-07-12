
### 7 | Polymorphism 

#### Simple case of polymorphism

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

```
Sides of a rectangle are 4
Area of rectangle is: 60
Sides of a circle are 0
Area of circle is: 153.9531
```

#### Polymorphism via inheritance

- The <code>getArea</code> method returns the area of the respective shape
- This is <code>Polymorphism</code>:
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
