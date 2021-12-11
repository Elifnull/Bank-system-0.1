class bankuser:
    def __init__(self, name, login):
        self.name = name
        self.login = login
        self.balance = 0

    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawl(self,amount):
        self.balance -= amount
        return self

    def user_balance(self):
        print(f'Account of {self.name}\nCurrent Balance: ${self.balance}')

    def transfer_money(self, user, amount):
        self.balance -= amount
        user.balance += amount
        print(f'User {self.name} current balance: ${self.balance}\nUser {user.name} current balance:$ {user.balance}')



levi = bankuser("Levi", "acer")
serge = bankuser("Serge", "Surge")
elisha = bankuser("Elisha", "Eli")

elisha.make_deposit(100)
elisha.make_deposit(75)
elisha.make_deposit(180)

elisha.make_withdrawl(65)
elisha.user_balance()

serge.make_deposit(1000).make_deposit(325).make_withdrawl(1100)
serge.user_balance()

levi.make_deposit(1975).make_withdrawl(975).make_withdrawl(85).make_withdrawl(15).user_balance()

levi.transfer_money(serge, 800)

serge.transfer_money(levi, 650)

