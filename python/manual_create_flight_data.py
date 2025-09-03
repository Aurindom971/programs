import pickle
import os
from datetime import datetime

# File path
file_path = "flight_details.dat"

# Function to add a new flight manually
def add_flight_manual():
    # Manually input flight details
    departure_airport = input("Enter departure airport: ").upper()
    arrival_airport = input("Enter arrival airport: ").upper()
    trip_type = input("Enter trip type (one-way/round): ").lower()
    flight_class = input("Enter class (economy/business/first): ").lower()
    airline = input("Enter airline: ")
    flight_number = input("Enter flight number: ").upper()

    # Input and validate dates
    departure_date = input("Enter departure date (YYYY-MM-DD): ")
    try:
        datetime.strptime(departure_date, "%Y-%m-%d")  # Verify date format
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD.")
        return
    
    # For round trips, ask for return date
    return_date = None
    if trip_type == "round":
        return_date = input("Enter return date (YYYY-MM-DD): ")
        try:
            datetime.strptime(return_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid return date format. Please enter in YYYY-MM-DD.")
            return
    
    # Input and validate times
    departure_time = input("Enter departure time (HH:MM): ")
    arrival_time = input("Enter arrival time (HH:MM): ")
    try:
        datetime.strptime(departure_time, "%H:%M")
        datetime.strptime(arrival_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please enter in HH:MM.")
        return
    
    # Set price based on class
    price = int(input("Enter ticket price: "))

    # Flight dictionary
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
        "airline": airline
    }

    # Load existing data, add new flight, and save
    flights = []
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            flights = pickle.load(file)
    
    flights.append(flight)  # Add the new flight to the list

    # Save updated data back to the file
    with open(file_path, "wb") as file:
        pickle.dump(flights, file)

    print("Flight added successfully.")

# Run the function
add_flight_manual()
