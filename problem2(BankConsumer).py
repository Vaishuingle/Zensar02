class Account :
    def __init__(self, balance, name):
        self.name = name
        self.balance = balance
        self.nominee =[]

    print("Your Account is crated.")

    def deposit(self, deposit):
        amount = int(input("Enter the amount to deposit: "))
        self.balance += amount
        print("Your New balance = %d" %self.balance)

    def withdraw(self, withdraw):
        amount = int(input("Enter The amount to withdraw: "))
        if(amount > self.balance):
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Your Remaining Balance is = %d" %self.balance)


    def __eq__(self, balance):
        self.balance == balance
        return self.balance == balance

    def __gt__(self, balance):
        self.balance > balance

    def __ge__(self, balance):
        self.balance >= balance

    def __lt__(self, balance):
        self.balance < balance

    def __le__(self, balance):
        self.balance <= balance

    def AddNominee(self, value):
        self.nominee.append(value)

    def __len__(self):
        return len(self.nominee)

    def __getitem__(self, index):
        return self.nominee[index]


acct1 = Account(5000, "Sachin")
acct1.deposit(1000)
acct1.withdraw(2000)
print(acct1)


acct2 = Account(3000, "Ali")
acct2.deposit(500)
acct2.withdraw(250)
print(acct2)

if(acct1 == acct2):
    print("They have equal balance")
else:
    print("They have different balance")


if(acct1 != acct2):
    print("Oops!!! they are not equal")
else:
    print("wow!!!  they are equal")


if(acct2 > acct1):
    print("acct2 should pay more tax")
else:
    print("acct1 should pay normal tax")

if(acct2 < acct1):
    print("Sponsor for two children")
else:
    print("Start an Orphanage")

if(acct2 >= acct1):
    print("Go On Europe Trip")
else:
    print("Go for an excursion")


if(acct2 <= acct1):
    print("We can have coffee")
else:
    print("We can have meals")


acct1.AddNominee("Ranjini")
acct1.AddNominee("Ragini")
acct1.AddNominee("Malini")
acct1.AddNominee("Rukmini")


print(len(acct1))  # number of nominees


for nom in acct1:  # should iterate nominees
    print(nom)

account = Account()
account.deposit()
account.withdraw()

