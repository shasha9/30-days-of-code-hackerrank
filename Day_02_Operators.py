#Task
#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

mealCost =float(input())

tipPercent = int(input())

taxPercent = int(input())


tip_cost = (tipPercent/100.)* mealCost
tax_cost = (taxPercent/100.)* mealCost
totalCost = int(round(mealCost + tip_cost + tax_cost))

print (totalCost)
