### Object Oriented Programming Language or OOP
##Main Concepts of Object-Oriented Programming (OOPs) 
## Class Link :  https://www.youtube.com/watch?v=Mf2RdpEiXjU
##Class
##Objects
##Polymorphism
##Encapsulation
##Inheritance
##Abstraction

## Internally Python treats each attributes as "Object"
### We can create our own DataTypes
## --------------------------------------------------------------
## Here list is class n l1 is object
##""""l1 = [1, 2, 3]
##l1.uppper()"""" 

## Class Contains Two important things : 1.Data , 2.Functions
## Class Basic Structure
"""class Car:
    color = "blue" # data
    model = "sports" 
    def cal_avg_speed(km, time):
         #some code"""

## Class name always in Pascal Case
## eg. ThisIsPascalCase
## Data name always in snake case: eg.cal_avg_speed

"""Function Vs Methods
Function : Normal function
Methods : It's a function which are written inside a class"""

## New Class
class Atm:
    
    counter = 1
    
 #Constructor : __init__
    def __init__(self):
        
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1
        
        self.menu()
        
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if type(new_pin) == int:
            self.__pin = new_pin
            print('Pin Changed Successfully')
        else:
            print('Error : Enter Whole Number')
        
    def menu(self):
        user_input = input("""
                           Welcome
                           How Would you you like to Proceed?
                           1.Enter 1 to create pin
                           2.Enter 2 to Deposit  
                           3.Enter 3 to withdraw 
                           4.Enter 4 to Check Balance
                           5.Enter 5 to Exit
                           """) 
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print('Have a Lovely Day')

        
    def create_pin(self):
        self.__pin = input('Enter Your Pin : ')
        print('Pin Set Successfully')
        
    def deposit(self):
        temp = input('Enter Your Pin : ')
        if temp == self.__pin:
            amount = int(input('Enter the amount :'))
            self.__balance = self.__balance + amount
            print('Deposit Successfully')
        else:
            print('Invalid Pin')

    def withdraw(self):
        temp = input('Enter Your Pin : ')
        if temp == self.pin:
            amount = int(input('Enter the amount :'))
            if amount<=self.__balance:
                self.__balance=self.__balance-amount
                print('Sucessfully withdraw')
            else:
                print('Invalid Pin')
                
    def check_balance(self):
        temp = input('Enter Your Pin : ')
        if temp == self.pin:
            print(self.__balance)
        else:
            print('Invalid Pin')

## New Class
class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d
        
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
        
    def __add__(self, other):
        
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        
        return '{}/{}'.format(temp_num, temp_den)

    def __sub__(self, other):
        
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        
        return '{}/{}'.format(temp_num, temp_den)
    
    def __mul__(self, other):
        
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        
        return '{}/{}'.format(temp_num, temp_den)

    def __truediv__(self, other):
        
        temp_num = self.num * other.den 
        temp_den = self.den * other.num
        
        return '{}/{}'.format(temp_num, temp_den)

## New Class ::: Collection of Objects
class Customer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def intro(self):
        print('I am', self.name, 'and i am', self.age)
        
c1 = Customer('Ritwik', 22)
c2 = Customer('Ankit', 34)
c3 = Customer('Neha', 45)

L = [c1, c2, c3]

for i in L:
    i.intro()

## Object of each class are mutable like list, dict, sets
## Instance variable inside constructor but class/static variable outside the constructor

## New Class
class Customers:
    
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
        def edit_prifile(self, new_name, new_city, new_pin, new_state):
            self.name = new_name
            self.address.change_address(new_city, new_pin, new_state)
        
class Address:
    
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state
        
    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

##add = Address('siliguri', 734005, 'wb')
##cust = Customer('ritwik', 'male', add)

##cust.edit_prifile('rakesh', 'patna', 357434, 'bihar')

##print(cust.address.pincode)
##three concepts of polymorphism
## Method overridding, method overloading, operator overloading























