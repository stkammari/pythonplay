def add(x,y) :
    return(x+y)

def subtract(x,y) :
    return(x-y)

def multiply(x,y) :
    return(x*y)

def division(x,y) :
    if x != 0 :
        return(x/y)
    else :
        return("Error : not devide by zero") 
    
print("Select an operation : " ) 
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. division") 

choice = input("Select choice for calculation (1/2/3/4) : ") 

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : ")) 

if choice == '1' :
    print ("Result : " , add(num1, num2)) 
elif choice == '2' :
    print ("Result : " , subtract(num1, num2))
elif choice == '3' :
    print ("Result : " , multiply(num1 , num2))
elif choice == '4' :
    print ("Result : " , division(num1, num2) ) 
else :
    print ("Invalid number")

