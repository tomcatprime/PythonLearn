# Tkinter

import tkinter

def button_clicked():
    print("Clicked")
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack()

#Buttob
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=10)
print(input.get())
input.pack()














# has to be at very end of the program
window.mainloop()