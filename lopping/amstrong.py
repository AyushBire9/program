num=int(input("Enter a number:"))
arm=0
temp=num
while temp>0:
    digit=temp%10
    arm=arm+digit**3
    temp//=10
if num==arm:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")