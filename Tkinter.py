# importing the library Tkinter 
import tkinter as tk

# creating a new window to pop up we are using a variable as window to pop up
window = tk.Tk()

# after creating a window we can also add text to it by using a class called tk.Label in the variable. 
greeting = tk.Label(text="Hello, Tkinter")

# To add that created label widget to the window use ".pack()". 
greeting.pack()

# .mainloop() this tells python to run he tkinter event loop. This method listens for events like button, keywords and blocks any code that comes after.
window.mainloop() 