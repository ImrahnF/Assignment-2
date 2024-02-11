'''
App.py
'''
import random
##############################################################################################################################################
class Product:

    # initialize everything. will be starting as zeros and blank strings and populated afterwards through another function
    def __init__(self, code, name, stock, sale_price, manufacture_cost, monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock
        self.monthly_units = monthly_units

    # this is called once the user inputs the desired values for whatever item they are creating
    def update_info(self, code, name, stock, sale_price, manufacture_cost, monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock
        self.monthly_units = monthly_units
    
    # this is more for debugging purposes to display the values of the product
    def __str__(self):
        return f"Product Code: {self.code}\n" \
               f"Product Name: {self.name}\n" \
               f"Stock Level: {self.stock_level}\n" \
               f"Product Sale Price: {self.sale_price}\n" \
               f"Product Manufacture Cost: {self.manufacture_cost}\n" \
               f"Estimated Monthly Units Manufactured: {self.monthly_units}"

    # this takes whatever values it has and runs a monthly simulation, keeping track of everything
    def generate_statement(self):
        total_manufactured = 0
        total_cost = 0.0
        total_sold = 0
        
        total_revenue = 0.0

        for i in range(1, 13):
            # do this 12 times

            # add x amount of units manufactured for this month to the total amount manufactured
            total_manufactured += self.monthly_units
            self.stock_level += self.monthly_units
            total_cost += (self.monthly_units*self.manufacture_cost)

            # sell some for the month
            sold = random.randint(self.monthly_units-15, self.monthly_units+15)
            total_sold += sold
            total_revenue += (sold * self.sale_price)

            # subtract the amount sold from the total stock
            self.stock_level -= sold

            # display the stats
            monthly_statement(self.monthly_units, sold, i, self.stock_level)

        # calculate and display total profit
        print("Total Sold:", total_sold)
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Total Cost: ${total_cost:.2f}\n")
        print(f"Profit = ${total_revenue - total_cost:.2f}")
        print(f"{'─'*30}")

##############################################################################################################################################
# simply displays the month's progress. this is made solely for a cleaner program
def monthly_statement(manufactured, month_sold, month, stock):
    print(f"{'─'*30}")
    print(f"*** STATEMENT FOR MONTH [{month}] ***")
    print("Items Manufactured:", manufactured)
    print("Units sold:", month_sold)
    print("Stock:", stock)
    if month >= 12:
        print(f"{'─'*30}")

# check if the item is an int, string, float, etc..
def get_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            number_input = float(user_input)
            return number_input  # Return the input as a float to perserve any decimal values if added
        except ValueError:
            # If conversion to float fails try again
            print("Invalid input. Try again")

# use get_input() for the numbers, input() for strings
def get_inputs():
    code = int(get_input("Please enter the Product Code: "))
    name = input("Please enter the Product Name: ")
    stock = int(get_input("Please enter the Current Stock: "))
    sale_price = get_input("Please enter the Product Sale Price: ")
    manufacture_cost = get_input("Please enter the Product Manufacture Cost: ")
    monthly_units = int(get_input("Please enter Estimated Monthly Production: "))

    return code, name, stock, sale_price, manufacture_cost, monthly_units

##############################################################################################################################################
# MAIN
print(f"{'─'*30}")
print("Welcome")
print(f"{'─'*30}")

# Initialize new product
product = Product(0, "", 0, 0.0, 0.0, 0)
# product = Product(1234, "Product", 100, 150, 45.42, 75) # this is used for testing purposes

# Get information for the product
code, name, stock, sale_price, manufacture_cost, monthly_units = get_inputs()

# Call update_info with inputted values
product.update_info(code, name, stock, sale_price, manufacture_cost, monthly_units)

# Everything is set up so display the monthly statement to see the yearly statistic for the given product
product.generate_statement()