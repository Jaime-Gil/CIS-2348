"""
Jaime Gil
1788946
"""
datefile = input()
opened_f = open(datefile,'r')
month_dict = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
valid_dates = []
file_dates = []

for line in opened_f:
    file_dates.append(line.strip())
    for item in range(len(file_dates)):
        if (file_dates[item].find("/") == -1):
            valid_dates.append(file_dates[item])

print(file_dates)
print(valid_dates)
    
