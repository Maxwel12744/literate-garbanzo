try:
  Name = input("Enter your First name: ")
  Age = int(input("Enter your age: "))
except ValueError:
  print("Please enter a valid age.")
  exit()
except TypeError:
  print("Please enter a valid name.")
  exit()
else:
  print(f"Hello {Name}, you are {Age} years old.")
Nationality = input("Enter your nationality: ")
if Age >= 18 and Nationality.lower() == "kenyan":
    print(f"Hello {Name}, you are eligible to vote.")
elif Age < 18 and Nationality.lower() == "kenyan":
    print(f"Hello {Name}, you are not eligible to vote \n Because you are not 18 years old \n but you are a kenyan citizen.")
elif Age >= 18 and Nationality.lower() != "kenyan":
    print(f"Hello {Name}, you are not eligible to vote \n Because you are not a Kenyan citizen.")
else:   
    print(f"Hello {Name}, you are not eligible to vote.")
print("Thank you for using the voting eligibility checker.")    