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

#while True . keeps it running completely so you should atleast exit or break
while True:
    student = input("Name of the student? ")

#This part handles if someone types something that is not a number
    try:
        score = int(input("Score of the student? "))
    except ValueError:
        print("Please enter a valid number for the score.")
        continue

#This means go back to the top of the loop and ask again.(continue)
    while True:  # This only controls the "again" question its inner loop until the writter inputs the correct
        again = input("Do you want to view the student's grade? [yes or no]: ")

        if again.lower() == "yes":
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
            break  # Breaks out of inner loop and continues to next student

        elif again.lower() == "no":
            print("Goodbye!")
            exit()  # Ends the program

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


