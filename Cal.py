import tkinter as tk

def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y)

def multiply(x,y) :
    print(x*y)
    
def divide(x,y) :
    if x != 0:
        return (x/y)
    else:
        print("zero is not dividable") 
    
print("Select an operation : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an operation 1/2/3/4 : ")


num_1 = float(int(input("Enter the first number : ")))
num_2 = float(int(input("Enter the second number : ")))

if choice == "1":
    print(add(num_1,num_2))
elif choice == "2":
    print(subtract(num_1,num_2))
elif choice == "3":
    print(multiply(num_1,num_2))
elif choice == "4":
    print(divide(num_1,num_2))
else :
    print("Choose the correct operation!")