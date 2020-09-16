'''
Jaime Gil
1788946
'''


paint_coverage = 350
color_price = ['red', '35', 'blue', '25', 'green', '23']
color = ""
price = ""

height = float(input("Enter wall height (feet):\n"))
width = float(input("Enter wall width (feet):\n"))
area = height * width
print("Wall area:", '{:.0f}'.format(area), "square feet")
print("Paint needed:", '{:.2f}'.format(area / paint_coverage), "gallons")
cans = int(area / paint_coverage + 0.9999)
print("Cans needed:", cans, "can(s)\n")
user_color = input("Choose a color to paint the wall:\n")
if user_color == "red":
    color = color_price[0]
    price = color_price[1]
elif user_color == "blue":
    color = color_price[2]
    price = color_price[3]
elif user_color == "green":
    color = color_price[4]
    price = color_price[5]

print("Cost of purchasing " + color + " paint: $" + str(cans * int(price)))
