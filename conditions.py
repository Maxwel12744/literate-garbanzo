Name = input("Enter your First name: ")
Age = int(input("Enter your age: "))
Nationality = input("Enter your nationality: ")
if Age >= 18 and Nationality.lower() == "kenyan":
    print(f"Hello {Name}, you are eligible to vote.")
elif Age < 18 and Nationality.lower() == "kenyan":
    print(f"Hello {Name}, you are not eligible to vote \n Because you are not 18 years old.")
elif Age >= 18 and Nationality.lower() != "kenyan":
    print(f"Hello {Name}, you are not eligible to vote \n Because you are not a Kenyan citizen.")
else:   
    print(f"Hello {Name}, you are not eligible to vote.")