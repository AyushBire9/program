num=int(input("Enter the number: "))
sum=0
for i in range(0,num+1):
    if i%2!=0:
        sum=sum+i
print("The sum of all odd number is: ",sum)