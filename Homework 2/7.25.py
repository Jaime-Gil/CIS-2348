dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1
def exact_change(user_total):
    num_dollars = user_total // dollar
    user_total = user_total % dollar

    num_quarters = user_total // quarter
    user_total = user_total % quarter

    num_dimes = user_total // dime
    user_total = user_total % dime

    num_nickels = user_total // nickel
    user_total = user_total % nickel

    num_pennies = user_total // penny
    user_total = user_total % penny

    return num_dollars,num_quarters,num_dimes,num_nickels,num_pennies

def main():
    user_total = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)
    if user_total <= 0:
        print("no change")
    else:
        if num_dollars > 1:
            print(num_dollars, "dollars")
        elif num_dollars == 1:
            print(num_dollars, "dollar")
        if num_quarters == 1:
            print(num_quarters, "quarter")
        elif num_quarters > 1:
            print(num_quarters, "quarters")   
        if num_dimes == 1:
            print(num_dimes, 'dime' )
        elif num_dimes > 1:
            print(num_dimes, "dimes")
        if num_nickels == 1:
            print(num_nickels, "nickel")
        elif num_nickels > 1:
            print(num_nickels, "nickels")
        if num_pennies == 1:
            print(num_pennies, "penny")
        elif num_pennies > 1:
            print(num_pennies, "pennies")
main()
