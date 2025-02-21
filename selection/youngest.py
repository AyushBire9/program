person1=int(input("Enter the age of person1: "))
person2=int(input("Enter the age of person2: "))
person3=int(input("Enter the age of person3: "))
person4=int(input("Enter the age of person4: "))
person5=int(input("Enter the age of person5: "))
if person1<person2 and person1<person3 and person1<person4 and person1<person5:
    print("Person1 is the youngest")
elif person2<person1 and person2<person3 and person2<person4 and person2<person5:
    print("Person2 is the youngest")
elif person3<person1 and person3<person2 and person3<person4 and person3<person5:
    print("Person3 is the youngest")
elif person4<person1 and person4<person2 and person4<person3 and person4<person5:
    print("Person4 is the youngest")
elif person5<person1 and person5<person2 and person5<person3 and person5<person4:
    print("Person5 is the youngest")
else:
    print("write diffrent ages off all the persons")