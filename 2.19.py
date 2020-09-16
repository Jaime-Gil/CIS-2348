lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print("")
print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
print("")
numb_of_servings = float(input("How many servings would you like to make?\n"))
print("")
print("Lemonade ingredients - yields", '{:.2f}'.format(numb_of_servings), "servings")
ingredient_div = numb_of_servings / servings
lemon = lemon * ingredient_div
water = water * ingredient_div
agave = agave * ingredient_div

print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")
lemon = lemon / 16
water = water / 16
agave = agave / 16
print("")
print("Lemonade ingredients - yields", '{:.2f}'.format(numb_of_servings), "servings")
print('{:.2f}'.format(lemon), "gallon(s) lemon juice")
print('{:.2f}'.format(water), "gallon(s) water")
print('{:.2f}'.format(agave), "gallon(s) agave nectar")