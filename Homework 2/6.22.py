a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

first_equation = (c-(a*f/d))/(b-(e*a/d))
second_equation = ((c/a)-(b*first_equation/a))
if a+b == d+e:
    print(round(second_equation), end=' ')
    print(round(first_equation))
else:
    print("No solution")
