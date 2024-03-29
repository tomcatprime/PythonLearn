import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label.pack()

window.mainloop()

def add(*args): #*args - unlimited arguments
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 5, 6, 7, 8, 431))

#**kwargs - unlimited key word arguments
def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_Car = Car(make="Nissan", model="almera")
print(my_Car.model)