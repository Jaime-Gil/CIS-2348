'''
Jaime Gil
1788946
'''


serv_price = ['Oil change', '35', 'Tire rotation', '19', 'Car wash', '7', 'Car wax', '12']
serv = "0"
price = "0"
service = "0"
cost = "0"
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")

serv1 = input("Select first service:\n")
if serv1 == "Oil change":
    serv = serv_price[0]
    price = serv_price[1]
elif serv1 == "Tire rotation":
    serv = serv_price[2]
    price = serv_price[3]
elif serv1 == "Car wash":
    serv = serv_price[4]
    price = serv_price[5]
elif serv1 == "Car wax":
    serv = serv_price[6]
    price = serv_price[7]


serv2 = input("Select second service:\n")
if serv2 == "Oil change":
    service = serv_price[0]
    cost = serv_price[1]
elif serv2 == "Tire rotation":
    service = serv_price[2]
    cost = serv_price[3]
elif serv2 == "Car wash":
    service = serv_price[4]
    cost = serv_price[5]
elif serv2 == "Car wax":
    service = serv_price[6]
    cost = serv_price[7]
print("")

total_cost = int(price) + int(cost)
print("Davy's auto shop invoice\n")
if serv1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: " + serv + ", $" + price)
if serv2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: " + service + ", $" + cost)
print("")
print("Total: $" + str(total_cost) )