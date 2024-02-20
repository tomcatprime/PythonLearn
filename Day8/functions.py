# functions parameters & Caesar Cipher



def my_func(name, location): # name is parameter - passed variable is called argument
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

name = input("Type name:\n")
location = input("Type Location:\n")
my_func(name, location)