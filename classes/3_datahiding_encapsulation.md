Data Hiding - Encapsulation

- Encapsulation in OOP refers to binding data and the methods
- To manipulate that data together in a single unit, that is, class.
- When encapsulating classes, a good convention is to declare all
- variables of a class private. This will restrict direct access by the code outside that class.
- At this point, a question can be raised: 
- If the methods and variables are encapsulated in a class, then how can they be used outside of that class?
    - The answer to this is simple. One has to implement public methods to let the outside world communicate with this class. 
    - These methods are called getters and setters. We can also implement other custom methods.

#### ADVANTAGES

- Classes make the code easy to change and maintain.
- Properties to be hidden can be specified easily.
- We decide which outside classes or functions can access the class properties.

#### GET AND SET - Bad Example 

- Anyone can access, change, or print the password and userName
- fields directly from the main code.
- This is dangerous in the case of this User class because 
- there is no encapsulation of the credentials of a user, 
- which means anyone can access their account by manipulating 
- the stored data.

```python
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
```

#### GET AND SET - Good Example

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


# created a new User object and stored the password and username
Steve = User("Steve", "12345")
Steve.login("steve", "12345")  # Grants access because credentials are valid

# does not grant access since the credentails are invalid
Steve.login("steve", "6789")
Steve.__password  # compilation error will occur due to this line
```
