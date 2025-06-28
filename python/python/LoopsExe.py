students = ["Alice", "Bob", "Kwanzu", "Zara"]

for student in students:
    again = input("Do you want to view another student's grade? [yes or no]: ")
    
    if again.lower() == "yes": 
      score = int(input(f"The score of {student} ?")) 

      if score >= 90:
            print(f"{student} got an A")
      elif score >= 80:
            print(f"{student} got a B")
      elif score >= 70:
            print(f"{student} got a C")
      elif score >= 60:
            print(f"{student} got a D")
      else:
            print(f"{student} got an F")

    elif again.lower() == "no":
        print("Goodbye!")
        break

    else:
        print("Please type yes or no.")

