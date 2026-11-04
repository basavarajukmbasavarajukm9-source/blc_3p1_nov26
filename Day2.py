   # check if a number is an even number


#
annual_gross_salary = float(input("Enter your annual gross salary:"))

if annual_gross_salary == 300000:
    print("you pay no tax.")
elif annual_gross_salary <= 500000:
    print("you pay 10% tax.")
elif annual_gross_salary<= 1000000:
    print("you pay 20% tax.")