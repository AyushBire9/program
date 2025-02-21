comsume=int(input("Enter the unit consumed in KW: "))
if comsume<=50:
    cost=comsume*1
    print("Cost of electricity is: ",cost)
elif comsume<=150:
    cost=50+(comsume-50)*2.50
    print("Cost of electricity is: ",cost)
elif comsume<=250:
    cost=50+100+(comsume-150)*4
    print("Cost of electricity is: ",cost)
else:
    cost=50+100+400+(comsume-250)*6
    print("Cost of electricity is: ",cost)