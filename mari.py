### Exercises that will be similar to those in the exam
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


### solution

