num=int(input("Enter the number :"))
rev=0
num1=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10 
if num1==rev:
    print("The number",num1,"is palindrome")
else:
    print("The number",num1,"is not palindrome")