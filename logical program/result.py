pas=45
obtain=int(input("Enter the marks obtained: "))
total=int(input("Enter the total marks: "))
percentage=(obtain/total)*100
if percentage>=pas:
    print("you obtain",percentage,"%")
    print("You are pass")
else:
    print("you obtain",percentage,"%")
    print("you are not pass")