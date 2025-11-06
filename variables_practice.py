# Creating a variables to show the number of cups sold and profit earned per coffee 
profit_per_cup = 0.75
num_of_coffees = 0

# creating a user input and calculating the number cups they are buying
order_1 = int(input(("Enter how many coffees? : ")))
num_of_coffees = num_of_coffees + order_1 

order_2 = int(input(("Enter how many coffees? : ")))
num_of_coffees = num_of_coffees + order_2

# calculating profits per cups sold 
total_profits = profit_per_cup * num_of_coffees

# printing the number of cups sold and profits earned
print ("Total coffees sold : " + str(num_of_coffees))
print ("Total profits earned : " + str(total_profits) )