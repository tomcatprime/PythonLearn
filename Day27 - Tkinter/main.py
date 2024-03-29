import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()

#Entry componenet - input

input = tkinter.Entry(width=10)
input.pack()
input.get()

window.mainloop()

