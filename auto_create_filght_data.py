import pickle
import random
from datetime import datetime, timedelta

# Expanded sample data for random generation
airports = [
    "JFK", "LAX", "SFO", "ORD", "ATL", "DFW", "DEN", "SEA", "MIA", "BOS",  # USA
    "LHR", "LGW", "MAN", "CDG", "FRA", "AMS", "MAD", "BCN",  # Europe
    "HKG", "SIN", "NRT", "KIX", "SYD", "MEL", "BKK",  # Asia/Pacific
    "DEL", "BOM", "BLR", "CCU", "MAA", "HYD", "COK", "TRV",  # India
    "YYZ", "YVR", "YUL",  # Canada
    "DXB", "AUH", "DOH", "JED",  # Middle East
]

airlines = [
    "IndiGo", "Air India", "SpiceJet",  # Indian Airlines
    "Emirates",  # International
    "Singapore Airlines",  # Asia
    "Delta Airlines"  # USA
]

# Function to generate a random valid date in the format YYYY-MM-DD
def generate_random_date(start_year=2024, end_year=2026):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    # Use the month to determine the maximum valid day
    if month in [1, 3, 5, 7, 8, 10, 12]:  # 31 days
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:  # 30 days
        day = random.randint(1, 30)
    else:  # February, check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day = random.randint(1, 29)  # Leap year
        else:
            day = random.randint(1, 28)  # Non-leap year
    return f"{year:04}-{month:02}-{day:02}"

# Generate 1000 sample flights
sample_flights = []
for i in range(100000):
    # Randomly select departure and arrival airports, ensuring they are different
    departure_airport = random.choice(airports)
    arrival_airport = random.choice([airport for airport in airports if airport != departure_airport])
    
    # Randomly select an airline, class, and generate flight number
    airline = random.choice(airlines)
    flight_class = random.choice(["economy", "business", "first"])
    flight_number = f"{airline.split()[-1][0]}{random.randint(100, 999)}"
    
    # Generate random dates for departure and return (if round trip)
    departure_date = generate_random_date()
    return_date = generate_random_date() if flight_class in ["business", "first"] else None
    
    # Generate random times for departure and arrival
    departure_time = f"{random.randint(1, 23):02}:{random.randint(0, 59):02}"
    arrival_time = f"{(int(departure_time.split(':')[0]) + random.randint(6, 10)) % 24:02}:{random.randint(0, 59):02}"
    
    # Set random price based on class
    if flight_class == "economy":
        price = random.randint(50000, 100000)
    elif flight_class == "business":
        price = random.randint(120000, 340000)
    else:  # first class
        price = random.randint(400000, 700000)
    
    # Create a dictionary representing a flight
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
    
    # Append the flight to the list of sample flights
    sample_flights.append(flight)

# Save the sample flights to a binary file using pickle
with open("flight_details.dat", "ab") as file:
    pickle.dump(sample_flights, file)

print("Sample flight data successfully saved to flight_details.dat.")
