atendance=75
atend=int(input("Enter the number class that atend: "))
total=int(input("Enter the total number of class: "))
percentage=(atend/total)*100
if percentage>=atendance:
    print("You are allowed to sit in exam")
else:
        print("You are not allowed to sit in exam")
