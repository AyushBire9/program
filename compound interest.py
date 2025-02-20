principal=int(input("Enter the principal amount :"))
rate=int(input("Enter the Rate of Interest :"))
time=int(input("enter the time period :"))
A=principal*(1+rate/100)**time
CI=A-principal
print("the final amount is :",CI)