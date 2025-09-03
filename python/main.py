import pickle as p
from datetime import datetime


def signup():
    with open("customer.dat", "ab") as f:
        while True:
            try:
                national_id = int(
                    input("Enter National Identification No (16 digits): ")
                )
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
                emergency_contact = int(
                    input("Enter an Emergency Contact No (10 digits): ")
                )
                if len(str(emergency_contact)) != 10:
                    print(
                        "Emergency Contact No must be 10 digits long. Please try again."
                    )
                    continue
                ticket = []
                # save the passenger information
                info = [
                    national_id,
                    passport_no,
                    name,
                    password1,
                    dob,
                    gender,
                    email,
                    phone,
                    residence,
                    emergency_contact,
                    ticket,
                ]
                p.dump(info, f)
                more_passengers = (
                    input("Do you want to add more passengers? (Y/N): ").strip().upper()
                )
                if more_passengers == "N":
                    break
            except ValueError:
                print("Invalid input. Please try again.")
    print("Passenger details successfully saved ")


def book_tickets(ticket):
    print("Please enter your travel details:")
    departure_airport = input("Enter your departure airport: ").strip()
    arrival_airport = input("Enter your arrival airport: ").strip()
    trip_type = input(
        "Is this a one-way trip or round trip? (Enter 'one-way' or 'round'): "
    ).lower()
    departure_date = input("Enter your departure date (YYYY-MM-DD): ").strip()

    # if round trip, ask for return date
    return_date = None
    if trip_type == "round":
        return_date = input("Enter your return date (YYYY-MM-DD): ").strip()

    travel_class = input("Choose your class (First/Business/Economy): ").strip().lower()

    # flight details from flight_details.dat
    try:
        with open("flight_details.dat", "rb") as file:
            flights = p.load(file)
    except FileNotFoundError:
        print("Error: Flight details file not found.")
        return
    except EOFError:
        print("Error: Flight details file is empty.")
        return

    # filter flights based on user's input
    available_flights = []
    for flight in flights:
        if (
            flight["departure_airport"].lower() == departure_airport.lower()
            and flight["arrival_airport"].lower() == arrival_airport.lower()
            and flight["class"].lower() == travel_class
            and flight["departure_date"] == departure_date
        ):

            # for round trip, check if return date matches
            if trip_type == "round" and "return_date" in flight:
                if flight["return_date"] == return_date:
                    available_flights.append(flight)
            elif trip_type == "one-way":
                available_flights.append(flight)

    # display available flights
    if available_flights:
        print("\nAvailable Flights:")
        for i, flight in enumerate(available_flights, start=1):
            print(f"\nFlight {i}:")
            print(f"  Flight Number: {flight['flight_number']}")
            print(
                f"  Departure: {flight['departure_airport']} at {flight['departure_time']}"
            )
            print(f"  Arrival: {flight['arrival_airport']} at {flight['arrival_time']}")
            print(f"  Class: {flight['class']}")
            print(f"  Price: ₹{flight['price']}")
            print(f"  Airline: {flight['airline']}")
            if trip_type == "round":
                print(f"  Return Date: {return_date}")

        # user to enter the flight number for booking
        selected_flight_number = input(
            "\nEnter the flight number you want to book: "
        ).strip()

        # find and confirm selected flight
        selected_flight = next(
            (
                flight
                for flight in available_flights
                if flight["flight_number"] == selected_flight_number
            ),
            None,
        )

        if selected_flight:

            print("\nBooking successful!")

            # append booking details to the ticket list
            booking = {
                "flight_number": selected_flight["flight_number"],
                "departure_airport": selected_flight["departure_airport"],
                "arrival_airport": selected_flight["arrival_airport"],
                "departure_date": selected_flight["departure_date"],
                "return_date": return_date,
                "departure_time": selected_flight["departure_time"],
                "arrival_time": selected_flight["arrival_time"],
                "class": selected_flight["class"],
                "price": selected_flight["price"],
                "airline": selected_flight["airline"],
            }
            ticket.append(booking)

            # save booking details to cus_booking_detail.dat
            with open("cus_booking_detail.dat", "ab") as booking_file:
                p.dump(booking, booking_file)

            # print ticket details
            print("\nTicket Details:")
            for key, value in booking.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Invalid flight number. No booking made.")
    else:
        print("No flights available matching your criteria.")


# baggage rates by weight
baggage_rates = {
    5: 500,  # ₹500 for up to 5 kg
    10: 900,  # ₹900 for up to 10 kg
    15: 1300,  # ₹1300 for up to 15 kg
    20: 1700,  # ₹1700 for up to 20 kg
}


def check_flight_status_and_baggage():
    try:
        # load booking details
        with open("cus_booking_detail.dat", "rb") as booking_file:
            bookings = []
            while True:
                try:
                    booking = p.load(booking_file)
                    bookings.append(booking)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No booking details found.")
        return

    # check if there are any bookings and print them
    if not bookings:
        print("No Booking Done")
    else:
        print("Booking Details:")
        for booking in bookings:
            print("--------------------------------------------------")
            for key, value in booking.items():
                print(f"{key.capitalize()}: {value}")
            print("--------------------------------------------------")

            # ask if the user wants to add extra baggage
            add_baggage = (
                input("Would you like to prepay for extra baggage? (Y/N): ")
                .strip()
                .upper()
            )
            if add_baggage == "Y":
                # display baggage rates
                print("\nExtra Baggage Rates (per additional kg):")
                for weight, rate in baggage_rates.items():
                    print(f"{weight} kg - ₹{rate}")

                # get the baggage weight from the user
                extra_weight = int(
                    input("Enter the additional baggage weight (in kg): ").strip()
                )
                while extra_weight not in baggage_rates:
                    print(
                        "Invalid weight selected. Please choose from the available options."
                    )
                    extra_weight = int(
                        input("Enter the additional baggage weight (in kg): ").strip()
                    )

                # additional baggage cost
                extra_cost = baggage_rates[extra_weight]
                print(f"Extra baggage cost: ₹{extra_cost}")

                # confirm and add extra baggage price to the ticket total
                confirm_baggage = (
                    input("Confirm extra baggage? (Y/N): ").strip().upper()
                )
                if confirm_baggage == "Y":
                    booking["price"] += extra_cost
                    print(f"Total price with extra baggage: ₹{booking['price']}")

                    # update the booking with the new price
                    with open("cus_booking_detail.dat", "wb") as booking_file:
                        for b in bookings:
                            p.dump(b, booking_file)
                    print("Baggage added and booking updated successfully.")
                else:
                    print("Extra baggage not added.")
            else:
                print("No extra baggage added.")
            print("--------------------------------------------------")


def dashboard(
    national_id, passport_no, nm, password2, dob, gen, em, ph, res, em_contact, ticket
):
    while True:
        welcome_message = f"""
        ===============================================================================
                                Welcome Back, {nm}!                          
        ===============================================================================
                    We’re excited to assist you with your travel needs.                
                        Check your flight status, book new tickets.                                     
                            Have a pleasant journey ahead!                           
        ===============================================================================
        """
        print(welcome_message)
        ch = int(input(" 1.Book New Tickets \n 2.Check Flight status \n 3.Exit\n"))
        if ch == 1:
            book_tickets(ticket)
        elif ch == 2:
            check_flight_status_and_baggage()
        elif ch == 3:
            break


def login_cus():
    f = open("customer.dat", "rb")
    ni = int(input("Enter National Identification code: "))
    ps = input("Enter Passport No.: ")
    password = input("Enter your Password: ")
    status = False
    try:
        while True:
            pb = p.load(f)
            if pb[0] == ni and pb[1] == ps and pb[3] == password:
                dashboard(
                    pb[0],
                    pb[1],
                    pb[2],
                    pb[3],
                    pb[4],
                    pb[5],
                    pb[6],
                    pb[7],
                    pb[8],
                    pb[9],
                    pb[10],
                )
                status = True
                break
        if status == False:
            print("Login failed")
    except EOFError:
        pass
    f.close()


def customer_portal():
    ch = int(input("    1.Login \n    2.Sign Up \n"))
    if ch == 1:
        login_cus()
    elif ch == 2:
        signup()
    else:
        print("Invalid Input")


def flight_monitoring():
    f = open("flight_details.dat", "rb")

    try:
        print(
            "FLT NO.",
            "\t",
            "DEP AIRPORT",
            "\t",
            "ARR AIRPORT",
            "\t",
            "DEPT DATE",
            "\t",
            "DEPT TIME",
            "\t",
            "ARR TIME",
            "\t",
            "CLASS",
            "\t\t\t",
            "PRICE",
            "\t\t",
            "AIRLINE",
        )
        while True:
            flight = p.load(f)
            for i in flight:
                print(
                    i["flight_number"],
                    "\t\t",
                    i["departure_airport"],
                    "\t\t",
                    i["arrival_airport"],
                    "\t\t",
                    i["departure_date"],
                    "\t",
                    i["departure_time"],
                    "\t\t",
                    i["arrival_time"],
                    "\t\t",
                    i["class"],
                    "\t\t",
                    i["price"],
                    "\t\t",
                    i["airline"],
                )

    except EOFError:
        pass
    f.close()


def gate_management():
    try:
        with open("flight_details.dat", "rb") as f:
            flights = []
            while True:
                try:
                    flight = p.load(f)
                    flights.extend(flight)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No flight details found.")
        return

    flight_no = input("Enter Flight Number to assign a gate: ").strip()
    gate = input("Enter Gate Number: ").strip()

    for flight in flights:
        if flight["flight_number"] == flight_no:
            flight["gate"] = gate  # assign the gate to the flight
            print(f"Gate {gate} assigned to Flight {flight_no}.")

            # update flights back to the file
            with open("flight_details.dat", "wb") as f:
                p.dump(flights, f)
            return

    print("Flight not found.")


def dashboard_staff(emp_id, nm, gen, dob, password, b_no):
    print(f"\nWelcome to the Staff Dashboard, {nm}!")
    while True:
        print("\nDashboard Options:")
        print("1. Flight Monitoring")
        print("2. Gate Management")
        print("3. Add Flight Data")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_monitoring()
        elif choice == 2:
            gate_management()
        elif choice == 3:
            add_flight_manual()
        elif choice == 4:
            print("Exiting dashboard")
            break
        else:
            print("Invalid choice. Please try again.")


def add_flight_manual():
    departure_airport = input("Enter departure airport: ").upper()
    arrival_airport = input("Enter arrival airport: ").upper()
    trip_type = input("Enter trip type (one-way/round): ").lower()
    flight_class = input("Enter class (economy/business/first): ").lower()
    airline = input("Enter airline: ")
    flight_number = input("Enter flight number: ").upper()

    # validate dates
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    try:
        datetime.strptime(departure_date, "%Y-%m-%d")  # verify date format
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD.")
        return

    # for round trips, ask for return date
    return_date = None
    if trip_type == "round":
        return_date = input("Enter return date (YYYY-MM-DD): ")
        try:
            datetime.strptime(return_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid return date format. Please enter in YYYY-MM-DD.")
            return

    # validate times
    departure_time = input("Enter departure time (HH:MM): ")
    arrival_time = input("Enter arrival time (HH:MM): ")
    try:
        datetime.strptime(departure_time, "%H:%M")
        datetime.strptime(arrival_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please enter in HH:MM.")
        return

    # set price based on class
    price = int(input("Enter ticket price: "))

    # flight dictionary
    flight = {
        "flight_number": flight_number,
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
        "departure_date": departure_date,
        "return_date": return_date,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "class": flight_class,
        "price": price,
        "airline": airline,
    }

    # load existing data, add new flight, and save
    flights = []
    with open("flight_details.dat", "rb") as file:
        flights = p.load(file)
    flights.append(flight)  # add the new flight to the list
    # save updated data back to the file
    with open("flight_details.dat", "wb") as file:
        p.dump(flights, file)
    print("Flight added successfully.")


def staff_portal():
    f = open("staff.dat", "rb")
    emp_id = input("Enter Employee ID: ")
    password = input("Enter password: ")
    b_no = input("Enter Badge No: ")
    status = False
    try:
        while True:
            pb = p.load(f)
            if pb[0] == emp_id and pb[4] == password and pb[5] == b_no:
                dashboard_staff(pb[0], pb[1], pb[2], pb[3], pb[4], pb[5])
                status = True
                break
        if status == False:
            print("Login Failed")
    except EOFError:
        pass
    f.close()


def report():
    while True:
        choice = int(
            input(
                "    1.Total Revenue\n    2.Revenue by Month\n    3.Revenue by Class\n    4.Total People Travelled\n    5.Exit\n"
            )
        )

        if choice == 1:
            f = open("cus_booking_detail.dat", "rb")
            total_revenue = 0
            try:
                while True:
                    pb = p.load(f)
                    total_revenue += pb["price"]
            except EOFError:
                print(f"Total Revenue: {total_revenue:.1f}")
                f.close()

        elif choice == 2:
            f = open("cus_booking_detail.dat", "rb")

            # dictionary to store revenue by month (as strings in "YYYY-MM" format)
            monthly_revenue = {}

            try:
                while True:
                    pb = p.load(f)
                    departure_date = pb["departure_date"]  # example: '2024-12-25'
                    departure_month = departure_date[:7]  # extract "YYYY-MM"
                    # add price to the corresponding month's revenue
                    if departure_month in monthly_revenue:
                        monthly_revenue[departure_month] += pb["price"]
                    else:
                        monthly_revenue[departure_month] = pb["price"]

            except EOFError:
                pass
            f.close()

            user_month = input("Enter the month (YYYY-MM) to see the revenue: ")

            if user_month in monthly_revenue:
                print(f"Revenue for {user_month}: {monthly_revenue[user_month]:.1f}")
            else:
                print(f"No revenue data available for {user_month}.")

        elif choice == 3:
            f = open("cus_booking_detail.dat", "rb")

            # store revenue by class
            class_revenue = {"first": 0, "business": 0, "economy": 0}
            try:
                while True:
                    pb = p.load(f)
                    flight_class = pb["class"].lower()
                    price = pb["price"]
                    # add price of the class revenue
                    if flight_class in class_revenue:
                        class_revenue[flight_class] += price
                    else:
                        class_revenue[flight_class] = price
            except EOFError:
                pass
            f.close()

            print("Revenue by Class:")
            for flight_class, revenue in class_revenue.items():
                print(f"{flight_class.capitalize()}: {revenue:.1f}")

        elif choice == 4:
            f = open("cus_booking_detail.dat", "rb")
            cnt = 0
            try:
                while True:
                    pb = p.load(f)
                    cnt += 1
            except EOFError:
                print("Total no people travelled till now: ", cnt)
        elif choice == 5:
            break


def main():
    while True:
        welcome_text = """
        ===============================================================================
                          WELCOME TO THE AIRPORT MANAGEMENT PORTAL                                         
        ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈  ✈ 
            Experience a smoother, faster way to manage airport operations!           
        ===============================================================================
        """

        sub_message = """
        For Airport Staff and Customers, managing flights has never been easier!
        Please login to continue...
        --------------------------------------------------------------------------------
        """
        print(welcome_text)
        print(sub_message)
        por = int(
            input(
                "    1.Customer Portal \n    2.Airport Staff Portal \n    3.Report\n    4.Exit\n"
            )
        )
        if por == 1:
            customer_portal()
        elif por == 2:
            staff_portal()
        elif por == 3:
            report()
        elif por == 4:
            break
        else:
            print("Invalid Input")


main()
