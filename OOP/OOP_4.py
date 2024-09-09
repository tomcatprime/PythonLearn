#private attributes

class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

#create some tests
john = Athlete("John", "boy")
Maria = Athlete("Maria", "girl")
Maria.running()
john.running()


print("###############################################")

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1._Customer__wallet_balance = 10000000000
c1.show_balance()

