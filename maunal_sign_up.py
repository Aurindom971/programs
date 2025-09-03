import pickle as p

def manual_signup():
    with open("customer.dat", "ab") as f:
        while True:
            # Gather information from the user
            try:
                national_id = int(input("Enter National Identification No (16 digits): "))
                if len(str(national_id)) != 16:
                    print("National ID must be 16 digits long. Please try again.")
                    continue
                
                passport_no = input("Enter Passport No (12 characters): ")
                if len(passport_no) != 12:
                    print("Passport No must be 12 characters long. Please try again.")
                    continue
                    
                name = input("Enter Name: ")
                dob = input("Enter Date of Birth in DD/MM/YYYY format: ")
                password1 = input("Create a password: ")
                password2 = input("Re-enter your password: ")
                if password1 != password2:
                    print("Passwords do not match. Please try again.")
                    continue
                
                gender = input("Enter Gender: ")
                email = input("Enter Email Address: ")
                phone = int(input("Enter Phone No (10 digits): "))
                if len(str(phone)) != 10:
                    print("Phone No must be 10 digits long. Please try again.")
                    continue
                
                residence = input("Enter Residence Address: ")
                emergency_contact = int(input("Enter an Emergency Contact No (10 digits): "))
                if len(str(emergency_contact)) != 10:
                    print("Emergency Contact No must be 10 digits long. Please try again.")
                    continue
                
                ticket = []  # Initialize an empty ticket list
                
                # Save the passenger information
                info = [national_id, passport_no, name, password1, dob, gender, email, phone, residence, emergency_contact, ticket]
                p.dump(info, f)
                
                # Ask if the user wants to add more passengers
                more_passengers = input("Do you want to add more passengers? (Y/N): ").strip().upper()
                if more_passengers == "N":
                    break
            except ValueError:
                print("Invalid input. Please try again.")

    print("Passenger details successfully saved ")

# Call the function to manually enter passenger details
manual_signup()
