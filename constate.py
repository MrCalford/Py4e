# Conditional Statements
# Hours w/ ACA
hrs=input('Enter Hours: ')
if float(hrs) >= 30 :
    print("ACA Full-Time", float(hrs))
else:
    print("Part-Time", float(hrs))
# Pay Rate Hourly vs Salary
pay=input('Enter Pay:')
if float(pay) < 50000 :
    print("Hourly")
elif float(pay) >= 50000 :
    print("Salary")
# Try Except For Union and Non-Union
Salary = 'Union'
Hourly = 'Non_Union'
try:
    be = int(Hourly)
except:
    be = float(pay)
if float(be) < 50000 :
    print("Benefits Eligible", Hourly)
try:
    ie = int(Salary)
except:
    ie = float(pay)
if float(ie) >= 50000 :
    print("Benefits Ineligible", Salary)
