#!!! Poluchih OK

class Wallet:
    def __init__(self):
        self.credit = 0

    def load(self, amount):
        self.credit = self.credit + amount
    
    def get_credit(self):
        return self.credit
    
    def purchase(self, price):
        if price > self.credit:
            return False
        else:
            self.credit = self.credit - price
            return True
        
w = Wallet()
# Let's load some money
w.load(10.00)
# We buy an item
success = w.purchase(6.00)
print(success)
another_success = w.purchase(5)
print(another_success)
print(w.get_credit())