Consider the following recursive function:

def my_fun(k):

    result = 0

    if(k>0):

        result = k+my_fun(k-2)

    return result

How many recursive calls does the function do on input 16?

The initial call should be counted in the answer.

Select one:
a. 15
b. 7
c. 8
d. 9
e. 16

What is a recursive function?
Select one:
a. A function that contains a call to itself
b. A function that raises an exception
c. A function that builds a linked list
d. A function that contains a while loop

    In
    a
    Python


    class , instance variables whose name begins with an underscore:
        Select
        one:


    a.Cannot
    be
    defined
    b.Are
    special
    methods
    c.Are
    part
    of
    the
    public
    interface
    of
    the


    class , by convention


    d.Are
    private
    members
    of
    the
    class , by convention


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

