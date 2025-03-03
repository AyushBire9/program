num=int(input("Enter a number:"))
arm=0
temp=num
l=len(str(num))
while temp>0:
    digit=temp%10
    arm=arm+digit**l
    temp//=10
if num==arm:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")