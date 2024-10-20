price = int(input("Enter your price : "))
def vatCal(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
print(vatCal(price))