import tkinter as tk

def click(event):
    global expression
    expression += str(event.widget["text"])
    entry_var.set(expression)

def clear():
    global expression
    expression = ""
    entry_var.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except:
        entry_var.set("Error")
        expression = ""

# GUI window setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x400")

expression = ""
entry_var = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge", justify="right")
entry.pack(pady=10)

# Button layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack()
    for char in row:
        if char == "C":
            btn = tk.Button(frame, text=char, font="Arial 18", padx=20, pady=20, command=clear)
        elif char == "=":
            btn = tk.Button(frame, text=char, font="Arial 18", padx=20, pady=20, command=equal)
        else:
            btn = tk.Button(frame, text=char, font="Arial 18", padx=20, pady=20)
            btn.bind("<Button-1>", click)
        btn.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
