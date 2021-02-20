# Food price variable will be a float(whole number)
Food_price = float(input("Enter your meal amount: "))
# tip amount will be a int(decimal)
Tip = int(input("Enter tip %: "))
# split will input how much to divide total cost 
Split = float(input("Enter number of guests "))
Tax = .10

# calculations
# tip amount variable will be equal to food price multiplied by tip/100. 100 will represrent whole dollar
Tip_amt = Food_price * Tip/100
# tax amount is food multiplied by tax 
Tax_amt = Food_price * Tax
Total = Food_price + Tip_amt + Tax_amt 
Total_amt_owed = Total/Split

# F string outputs will give us the results based on calculations 
# Final output will show how much is owed per guest tax included
print(f"Your meal was {Food_price} and your tip was {Tip_amt}.")
print(f"Your total with tax is {Total} ")
print(f"Split between {Split} guests, you owe {Total_amt_owed}")
