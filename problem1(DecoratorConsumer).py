
def decor(func):
    def inner(*args):

     print("Welcome.....")
     func(*args)

     print("end......")
    return inner



class dwa:
    def __init__(self,function):
        self.function = function
    def __call__(self,*args):
        self.function(*args)




def dwia(name1,name2,name3):
    print(name1,name2,name3)
    def function(func):
        def inner(*args):
            print("Welcome.....")
            func(*args)
            print("End.....")

        return inner
    return function




class cdwia:

    def __init__(self,name4,name5,name6):

        self.name4 = name4

        self.name5 = name5

        self.name6 = name6

    def __init__(self,function):

        self.function = function
    def __call__(self,*args):
        self.function(*args)




@decor
def fun2(a,b):
    print(f"we will win the soccer WC {a} {b}")
    fun2(111, 222)




@decor
def fun3(x, y, z):
    print(f"Happy Sunday fun3 {x} {y} {z}")

fun3(10,20,30)




@dwia("Sachin","Sourav","Rahul")

def fun4(x, y):
    print(f"fun4 .. {x} {y}")



fun4(88,77)