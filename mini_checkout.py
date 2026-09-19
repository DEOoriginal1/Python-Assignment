#Psuedocode
#--> Prompt user for their name in the terminal and enter an input.
#--> Collect the input and save it in a reference called customer_name.
#--> Prompt user for the product name in the terminal.
#--> Collect the input and save it in a reference called product_name.
#--> Prompt the user for quantity in the terminal.
#--> Collect the input and save it in a reference called quantity.
#--> Display the price of the goods on the terminal.
#--> Ask the user if he will buy again.
#--> If there is no more purchase, display the total bill on the terminal.


customer_name: input("Enter your name: ")
another_purchase = "yes"
quantity = 0
price = 0.0
total_bill = 0.0

while another_purchase != "no":
    product_name = input("Enter product Name: ")
    quantity = int(input(f"Enter the quantity of {product_name} : "))
    price = float(input(f"Enter the price of {product_name} :"))
    another_purchase = input("Do you want to buy another thing. Yes/No: ").lower()
        
    bill= quantity * price 
    total_bill += bill
    
if (another_purchase == "no"):
    print (f"Your total bill is ${total_bill:.2f}")
      
    
