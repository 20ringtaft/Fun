#calculates the amount an individual should pay for dinner, taking into account sales tax and tip

print("Welcome to the boy math calculator")
print("This calculator computes the share of a bill that an individual is responsible for based on their subtotal, tip percentage, and sales tax")

print("Please input the subtotal, total, tax percentage, and tip percentage separated by ',' characters")
print("Note that in this case 'subtotal' refers to the sum of cost of the items an individual orders, and total refers to the table's subtotal. Final price will be calculated with sales tax and tip")
print("For example: '60, 90, 15, 7.75' for a $60 share of a $90 subtotal, with a 15% tip and a 7.75% tax rate")

user_input = input("Input: ")
components = user_input.split(',')

subtotal = float(components[0])
total = float(components[1])
tip = float(components[2])
tax = float(components[3])

print("SUBTOTAL: $" + str(subtotal))
print("TOTAL: $" + str(total))
print("TIP: " + str(tip))
print("TAX: " + str(tax))

def alex_method(subtotal, tip, tax):
    tip_coefficient = tip * 0.01 
    tax_coefficient = tax * 0.01

 
    tip_amount = subtotal * tip_coefficient
    tax_amount = subtotal * tax_coefficient
    total = subtotal + tip_amount + tax_amount

    return total
    
def mason_method(subtotal, total, tip, tax):
    proportion = subtotal/total
    
    tip_coefficient = tip * 0.01 
    tax_coefficient = tax * 0.01
    
    final_price = total + (total * tip_coefficient) + (total * tax_coefficient)
    return proportion * final_price

print("According to Alex's boy math, this person should pay: " + str(alex_method(subtotal, tip, tax)))
print("According to Mason's boy math, this person should pay: " + str(mason_method(subtotal,total,tip,tax)))

    
    

    
    