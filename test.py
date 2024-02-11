import random

def monthly_statement(manufactured, month_sold, month):
    print(f"{'─'*30}")
    print(f"*** STATEMENT FOR MONTH [{month}] ***")
    print("Items Manufactured:", manufactured)
    print("Units sold:", month_sold)
    print("Stock:", stock)
    if month >= 12:
        print(f"{'─'*30}")

# starting values
code = 1738242
name = "Example Product"
stock = 100
sale_price = 49.95
manufacture_cost = 20.17
monthly_units = 75

def generate_statement():
    global stock

    # these are all for the entire year
    total_manufactured = 0
    total_sold = 0
    total_cost = 0.0
    total_revenue = 0.0

    for i in range(1, 13):
        # do this 12 times

        # add x amount of units manufactured for this month to the total amount manufactured
        total_manufactured += monthly_units
        stock += monthly_units
        total_cost += (monthly_units*manufacture_cost)

        # sell some for the month
        sold = random.randint(60, 90)
        total_sold += sold
        total_revenue += (sold * sale_price)

        # subtract the amount sold from the total stock
        stock -= sold

        # display the stats
        monthly_statement(monthly_units, sold, i)
    # calculate and display total profit
    
    print("Total Sold:", total_sold)
    print("Total Cost:", total_cost)
    print("Total Revenue:", total_revenue)
    print("Total Items Manufactured:", total_manufactured)

    print(f"Profit = ${total_revenue - total_cost:.2f}")
    print(f"{'─'*30}")

generate_statement()