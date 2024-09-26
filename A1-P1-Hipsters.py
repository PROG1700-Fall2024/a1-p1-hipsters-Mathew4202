#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.
"""
Student Name:    Mathew Akunyili
Program Title:  Hipster's Local Vinyl Records
Description:    calculate total cost of records of a customer
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Declare variables
    #In this section i declare my variables for the delivery fee and sales tax
    deliveryFee = 15
    salesTax = 0.14
    # Ask for customers name
    #in this section we prompt user to input the customer they want to calculate for
    customersName = input("Enter the customer's name:")

    # Ask user for the distance in kilometers driven to deliver
    #In this section we ask the user to input the distance taken to deliver the record to the customer and then we use the float to switch it from a string to a float
    distance = float(input("Enter the distance in kilometers for delivery:"))

    # Ask user to input the cost of any records purchased by the customer
     #In this section we ask the user to input the cost of records of the customer and then we use the float to switch it from a string to a float
    costofRecords = float(input("Enter the cost of records purchased:"))

    # Perform calculations
    # since all values inputed by the user has been changed to floate we then do the neccessary calculations
    deliveryCost = distance * deliveryFee
    purchaseCost = (salesTax * costofRecords) + costofRecords 
    totalCost = purchaseCost + deliveryCost

    # Print customers name
    print("Purchase summary for", customersName)

    # Print selivery, purchase and total cost
    # make sure to change is to print in 2 decimal places as thats the required formad for currency
    print(f"Delivery Cost: ${deliveryCost:.2f}")
    print(f"Purchase Cost: ${purchaseCost:.2f}")
    print(f"Total Cost: ${totalCost:.2f}")





    # YOUR CODE ENDS HERE

main()
