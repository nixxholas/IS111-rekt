#Q2
def get_day_of_week(n):
    # We use a tuple to record all the days of week.
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    
    # Uncomment the code below to understand how the variable days_of_week looks like.
    # print(type(days_of_week))
    # print(days_of_week)
    
    return days_of_week[n]
    
n = int(input('Enter a number indicating the day of the week [0 to 6]: '))
if n <= 0:
    print('Your number should be at least 0.')
elif n >= 7:
    print('Your number should be at most 6.')
else:
    print(get_day_of_week(n))

#Q3
def calculate_income_tax(income):
    if income <= 20000:
        tax = 0
    elif income <= 30000:
        tax = 0 + (income - 20000) * 0.02
    elif income <= 40000:
        tax = 200 + (income - 30000) * 0.035
    elif income <= 80000:
        tax = 550 + (income - 40000) * 0.07
    elif income <= 120000:
        tax = 3350 + (income - 80000) * 0.115
    elif income <= 160000:
        tax = 7950 + (income - 120000) * 0.15
    elif income <= 200000:
        tax = 13950 + (income - 160000) * 0.18
    elif income <= 240000:
        tax = 21150 + (income - 200000) * 0.19
    elif income <= 280000:
        tax = 28750 + (income - 240000) * 0.195
    elif income <= 320000:
        tax = 36550 + (income - 280000) * 0.20
    else:
        tax = 44550 + (income - 320000) * 0.20
    return tax

revenue = float(input('Enter your annual taxable income : '))
print('Your total tax is $' + str(calculate_income_tax(revenue)))

#Q4
def get_discount_rate(num_boxes):
    discount = 0
    if num_boxes >= 5:
        discount = 0.2
    elif 2 <= num_boxes:
        discount = 0.1
    return discount    

def calculate_total_amount(brand, num_boxes):
    BRAND_1 = "Tung Lok"
    BRAND_2 = "Man Fu Yuan"
    PRICE_1 = 55.40
    PRICE_2 = 59.60
    
    if brand == BRAND_1:
        return PRICE_1 * num_boxes * (1 - get_discount_rate(num_boxes))
    else:
        return PRICE_2 * num_boxes * (1 - get_discount_rate(num_boxes))

brand = input("Which brand do you want to buy? ")
num_boxes = int(input("How many boxes do you want to buy? "))

print("You need to pay $" + str(calculate_total_amount(brand, num_boxes)) )

#Q5
# retail_utility.py
def calculate_max_quantity_and_change(unit_price, amount):
    qty = int(amount // unit_price)
    price_to_pay = unit_price * qty
    change = amount - price_to_pay
    return (qty, change)

# purchase_honey.py
import retail_utility

PRICE_1kg = 98.50
PRICE_500gr = 58.50
amount = float(input('How much money do you want to spend? '))

result_tuple = retail_utility.calculate_max_quantity_and_change(PRICE_1kg, amount)
qty_1kg = result_tuple[0]
change = result_tuple[1]

result_tuple = retail_utility.calculate_max_quantity_and_change(PRICE_500gr, change)
qty_500gr = result_tuple[0]
change = result_tuple[1]

num_grams_can_buy = qty_1kg * 1000 + qty_500gr * 500

print('You can buy '+ str(num_grams_can_buy) + ' grams of honey. You have $' + str(change) + ' left as your change.')
