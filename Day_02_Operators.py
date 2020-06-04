mealCost = float(input())

tipPercent = int(input())

taxPercent = int(input())


tip_cost = (tipPercent/100.)* mealCost
tax_cost = (taxPercent/100.)* mealCost
totalCost = int(round(mealCost + tip_cost + tax_cost))

print (totalCost)
