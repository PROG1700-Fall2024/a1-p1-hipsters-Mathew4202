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
    deliveryFee = 15
    salesTax = 0.14
    # Ask for customers name
    customersName = input("Enter the customer's name:")

    # Ask user for the distance in kilometers driven to deliver
    distance = float(input("Enter the distance in kilometers for delivery:"))

    # Ask user to input the cost of any records purchased by the customer
    costofRecords = float(input("Enter the cost of records purchased:"))

    # Perform calculations
    deliveryCost = distance * deliveryFee
    purchaseCost = (salesTax * costofRecords) + costofRecords 
    totalCost = purchaseCost + deliveryCost

    # Print customers name
    print("Purchase summary for", customersName)

    # Print selivery, purchase and total cost
    print(f"Delivery Cost: ${deliveryCost:.2f}")
    print(f"Purchase Cost: ${purchaseCost:.2f}")
    print(f"Total Cost: ${totalCost:.2f}")





    # YOUR CODE ENDS HERE

main()