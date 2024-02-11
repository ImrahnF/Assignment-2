'''
App.py
'''
import random

class Prodcut:
    def __init__(self, code, name, stock, sale_price, manufacture_cost, monthly_units):
        # initialize everything. will be starting as zeros and blank strings and populated afterwards through another function
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock
        self.monthly_units = monthly_units

    def update_info(self, code, name, stock, sale_price, manufacture_cost, monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock
        self.monthly_units = monthly_units
    
    def __str__(self):
        return f"Product Code: {self.code}\n" \
               f"Product Name: {self.name}\n" \
               f"Stock Level: {self.stock_level}\n" \
               f"Product Sale Price: {self.sale_price}\n" \
               f"Product Manufacture Cost: {self.manufacture_cost}\n" \
               f"Estimated Monthly Units Manufactured: {self.monthly_units}"

    def generate_statement(self):
        pass


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

def get_inputs():
    # use get_input() for the numbers, input() for strings
    code = int(get_input("Please enter the Product Code: "))
    name = input("Please enter the Product Name: ")
    stock = int(get_input("Please enter the Current Stock: "))
    sale_price = get_input("Please enter the Product Sale Price: ")
    manufacture_cost = get_input("Please enter the Product Manufacture Cost: ")
    monthly_units = int(get_input("Please enter Estimated Monthly Production: "))

    return code, name, stock, sale_price, manufacture_cost, monthly_units

# MAIN
print(f"{'─'*30}")
print("Welcome")
print(f"{'─'*30}")

# Initialize new product
product = Prodcut(0, "", 0.0, 0.0, 0, 0)

# Get information for the product
code, name, stock, sale_price, manufacture_cost, monthly_units = get_inputs()

# Call update_info with inputted values
product.update_info(code, name, stock, sale_price, manufacture_cost, monthly_units)

# print those values back
# print(product)

# 