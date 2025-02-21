year=int(input("enter youe experience in year :"))
if year>=5:
    bonus=10000
    print("Your bonus is: ",bonus)
elif year>=3:
    bonus=5000
    print("Your bonus is: ",bonus)
elif year>=1:
    bonus=2000
    print("Your bonus is: ",bonus)
else:
    print("You have no bonus")