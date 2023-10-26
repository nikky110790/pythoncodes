# include the required libraries
import tkinter as tk
import tkinter.ttk as ttk

# creating a basic windows dialog
window = tk.Tk()

# creating the greetings
greeting = tk.Label(text="Hello, Tkinter", background="#34A2FE")

# creating the greetings
greeting1 = ttk.Label(text="Hello, Tkinter", background="red")

# calling the greetings pack
greeting.pack()

# calling the greetings pack
greeting1.pack()


button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)


button.pack()

# creating a loop to display the dialog
window.mainloop()