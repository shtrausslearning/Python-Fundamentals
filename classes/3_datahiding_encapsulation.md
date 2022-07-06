### Two Methods for Information Hiding

- Information hiding refers to the concept of hiding the inner workings of a class and simply providing an interface through which the outside world can interact with the class without knowing what’s going on inside, two types exist:
    - <code>Encapsulation</code>
    - <code>Abstraction</code>


### GET AND SETTER

With encapulation, we utilise private variables & utilise <code>get</code>, <codE>setter</code> methods

- A getter method allows reading a property’s value
- A setter method allows modifying a property’s value

```python
class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username      # private variable

    # set private variable with method
    def setUsername(self, x):
        self.__username = x

    # get private variable with method
    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
```

#### Data Hiding - Encapsulation

- <code>Encapsulation</code> in OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class.
- When encapsulating classes:
    - A good convention is to declare all variables of a class private. (This will restrict direct access by the code outside that class)
- If the methods and variables are encapsulated in a class, then how can they be used outside of that class?
    - One has to implement public methods to let the outside world communicate with this class. 
    - These methods are called getters and setters. We can also implement other custom methods.

#### ADVANTAGES

- Classes make the code easy to change and maintain.
- Properties to be hidden can be specified easily.
- We decide which outside classes or functions can access the class properties.

#### GET AND SET - Bad Example 

- Anyone can access, change, or print the <code>password</code> and <code>userName</code> fields directly from the main code.
- This is dangerous in the case of this User class because there is no <code>encapsulation</code> of the credentials of a user, 
- which means anyone can access their account by manipulating the stored data.

```python
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password
        
    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower())
                and (self.password == password)):
            print("Access Granted!")
        else:
            print("Invalid Credentials!")

Steve = User("tom", "123")
Steve.login("tom", "123")

Steve.login("tom", "345")
Steve.password = "345"     # access to variables is allowed
Steve.login("tom", "345")
```

```
Access Granted!
Invalid Credentials!
Access Granted!
```

#### GET AND SET - Good Example

- Instances use private variables, <code>get</code><code>set</code> compare method arguments to these private variables
- If there is no match, doesn't grant access to <code>login</code>

```python
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password

    def login(self, userName, password):
        if ((self.__userName.lower() == userName.lower())
                and (self.__password == password)):
            print(
                "Access Granted against username:",
                self.__userName.lower(),
                "and password:",
                self.__password)
        else:
            print("Invalid Credentials!")


Steve = User("tom", "234") # created a new User object and stored the password and username
Steve.login("tom", "234")  # Grants access because credentials are valid
Steve.login("tom", "6789") # does not grant access since the credentails are invalid
# Steve.__password           # compilation error will occur due to this line
```

```
Access Granted against username: steve and password: 12345
Invalid Credentials!
```
