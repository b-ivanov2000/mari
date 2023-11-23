### Exercises that will be similar to those in the exam
# and their solutions
# there will be classes

Create a Python class called BankAccount that represents a bank account. The class should have the following attributes and methods:
Attributes:
account_number (string): The account number associated with the bank account.
balance (float): The current balance of the bank account.

Methods:

deposit(amount): Accepts a float amount and adds it to the account's balance.
withdraw(amount): Accepts a float amount and subtracts it from the account's balance, if the balance is sufficient.
get_balance(): Returns the current balance of the account as a float.
get_account_number(): Returns the account number as a string.
For example:

Test	Result
account = BankAccount("12345678", 100.0)
account.deposit(50.0)
print(account.get_balance())
150.0


##### solution

class BankAccount:     # a model of a bank account
    # self - specific people (Marina Kancheva)
    # self.something - my own attribute
    def __init__(self, account_number, balance):
        # we include account_number and balance because they are already there, we pass externally or there is a default value (0)
        self.account_number = account_number   # can also do = x
        self.balance = balance

# getter method: get me a a value
# setter method: updating, adding, doing something

    def deposit(self, amount):     # start with self, referring to other parameters
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    def get_balance(self):           # always include self
        return self.balance
    def get_account_number(self):
        return self.account_number

account = BankAccount("12345678", 100.0)
account.deposit(50.0)
print(account.get_balance())



##########################################
Define a class Scale to represent a traditional scale (balance) with two plates: a left and a right plate. The user will be able to incrementally load each plate, adding weight, and test whether the scale is in equilibrium or it tilts to the left or to the right.
The class shall provide the following methods:

Constructor: does not take any parameter: it initialises a scale with empty plates.
load(weight, plate): when called, the weight weight shall be added to plate plate. plate is a string that may be 'L' (left plate) or 'R' (right plate)
measure(): returns the current measurement outcome. The method returns a string that may be 'E' (equilibrium), 'L' (left plate is heavier) or 'R' (right plate is heavier).
For example:

Test	Result
s = Scale()
m = s.measure()
print(m)
E
# solution

class Scale:
    def __init__(self):   # this is the constructor
        self.right_plate = 0
        self.left_plate = 0
    def load(self, weight, plate):
        if plate == "L":
            self.left_plate += weight
        elif plate == "R":
            self.right_plate += weight
    def measure(self):
        if self.right_plate == self.left_plate:
            return "E"
        elif self.right_plate > self.left_plate:
            return "R"
        else:
            return "L"

s = Scale()
m = s.measure()
print(m)



##########################
Define a class Car to simulate the behavior of a car. The user will be able to refuel the car, and then to drive, consuming fuel (if there is enough fuel). The class shall provide the following methods:

Constructor: takes one float parameter fuel_consumption, expressed in liters per kilometer. The fuel tank is initially empty.
refuel(quantity): when called, quantity liters of fuels are stored in the tank.
drive(distance): ask to drive for distance kilometers, while consuming fuel. The method shall return the number of kilometers actually traveled: if there is not enough fuel, the car travels as much as possible, stopping as soon as tank becomes empty.
For example:

Test	Result
c = Car(0.1)    # Our car consumes 0.1 liters per kilometer
# Let’s refuel 20 liters
c.refuel(20)
# Try to drive for 150 km
traveled = c.drive(150)
print(int(traveled))        # Expected: 150 - ok
150

# solution
class Car:
    def __init__(self, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.tank = 0
    def refuel(self, quantity):
        self.tank += quantity
    def drive(self, distance):
        if self.fuel_consumption*distance >= self.tank: # we consume more than tank
            actual_distance = self.tank/self.fuel_consumption
            self.tank = 0   # important to update the tank!!
            return actual_distance
        else:
            self.tank -= self.fuel_consumption*distance   # updating the tank
            return distance


############################

Define a class Wallet to represent a personal digital wallet. The user will be able to load money in the wallet, and then to spend money to purchase items. The class shall provide the following methods:

Constructor: does not take any parameter: it initialises an empty wallet (i.e., starting credit is 0)
load(amount): when called, the amount of money amount shall be added to the wallet credit
get_credit(): returns the current balance of the wallet
purchase(price): purchases an item whose price is price. Returns True on success, i.e., if there is enough credit in the wallet the transaction is completed. Returns False if there is not enough credit, and the transaction is aborted (i.e., item is not purchased).
For example:

Test	Result
w = Wallet()
# Let's load some money
w.load(10.00)
# We buy an item
success = w.purchase(6.00)
print(success)
True



# solution

class Wallet:
    def __init__(self):
        self.wallet = 0
    def load(self, amount):
        self.wallet += amount
    def get_credit(self):
        return self.wallet
    def purchase(self, price):
        if price <= self.wallet:
            self.wallet -= price
            return True
        else:
            return False

w = Wallet()
# Let's load some money
w.load(10.00)
# We buy an item
success = w.purchase(6.00)
print(success)

####################

Define a class TelephoneAccount to keep track of the phone calls of a subscriber of a telephone line.

The class shall provide the following methods.

Constructor: takes two float parameters (call_setup_fee, per_minute_fee).
add_call(duration): called when a phone call is performed. If duration is 0, the call is unsuccessful and nothing is charged. Otherwise, duration is the length of the call, in minutes. The subscriber is charged the call setup fee, plus a variable cost, depending on the call duration.
get_bill(): returns the total price to be paid for all the calls that have been performed so far.
For example:

Test	Result
a = TelephoneAccount(0.1, 0.2)
a.add_call(2)
a.add_call(0)
a.add_call(1.5)
b = a.get_bill()
print(float(b))
0.9


#### solution


class TelephoneAccount:
    def __init__(self, call_setup_fee, per_minute_fee):
        self.call_setup_fee = call_setup_fee
        self.per_minute_fee = per_minute_fee
        self.phone_calls = 0
        self.price = 0
    def add_call(self, duration):
        if duration == 0:
            self.phone_calls = self.phone_calls
        else:
            self.price += self.call_setup_fee + self.per_minute_fee*duration
    def get_bill(self):
        return self.price

a = TelephoneAccount(0.1, 0.2)
a.add_call(2)
a.add_call(0)
a.add_call(1.5)
b = a.get_bill()
print(float(b))