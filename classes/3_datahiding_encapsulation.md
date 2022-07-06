Data Hiding - Encapsulation

- Encapsulation in OOP refers to binding data and the methods
- To manipulate that data together in a single unit, that is, class.
- When encapsulating classes, a good convention is to declare all
- variables of a class private. This will restrict direct access by the code outside that class.

- At this point, a question can be raised: 
- If the methods and variables are encapsulated in a class, then how can they be used outside of that class?

- The answer to this is simple. 
- One has to implement public methods to let the outside world communicate with this class. These methods are called getters and setters. We can also implement other custom methods.

#### ADVANTAGES

- Classes make the code easy to change and maintain.
- Properties to be hidden can be specified easily.
- We decide which outside classes or functions can access the class properties.

#### GET AND SET

class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)

Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())



