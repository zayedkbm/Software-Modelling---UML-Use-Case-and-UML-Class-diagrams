from datetime import datetime


class Passenger:
    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email
        self.__boarding_passes = []

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_boarding_passes(self):
        return self.__boarding_passes

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def add_boarding_pass(self, boarding_pass):
        self.__boarding_passes.append(boarding_pass)


class Flight:
    def __init__(
        self,
        flight_number: str,
        departure_time: datetime,
        arrival_time: datetime,
        origin: str,
        destination: str,
    ):
        self.__flight_number = flight_number
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__origin = origin
        self.__destination = destination
        self.__seats = []

    def get_flight_number(self):
        return self.__flight_number

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_seats(self):
        return self.__seats

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def set_origin(self, origin):
        self.__origin = origin

    def set_destination(self, destination):
        self.__destination = destination

    def add_seat(self, seat):
        self.__seats.append(seat)


class BoardingPass:
    def __init__(
        self,
        flight: Flight,
        passenger: Passenger,
        seat: "Seat",
        gate: str,
        boarding_time: datetime,
    ):
        self.__flight = flight
        self.__passenger = passenger
        self.__seat = seat
        self.__gate = gate
        self.__boarding_time = boarding_time

    def get_flight(self):
        return self.__flight

    def get_passenger(self):
        return self.__passenger

    def get_seat(self):
        return self.__seat

    def get_gate(self):
        return self.__gate

    def get_boarding_time(self):
        return self.__boarding_time

    def set_flight(self, flight):
        self.__flight = flight

    def set_passenger(self, passenger):
        self.__passenger = passenger

    def set_seat(self, seat):
        self.__seat = seat

    def set_gate(self, gate):
        self.__gate = gate

    def set_boarding_time(self, boarding_time):
        self.__boarding_time = boarding_time

    def display_details(self):
        print(f"Passenger: {self.get_passenger().get_name()}")
        print(f"Flight: {self.get_flight().get_flight_number()}")
        print(f"Seat: {self.get_seat().get_seat_number()}")
        print(f"Gate: {self.get_gate()}")
        print(f"Boarding Time: {self.get_boarding_time().strftime('%Y-%m-%d %H:%M')}")


class Seat:
    def __init__(self, seat_number: str, class_type: str):
        self.__seat_number = seat_number
        self.__class_type = class_type
        self.__is_available = True

    def get_seat_number(self):
        return self.__seat_number

    def get_class_type(self):
        return self.__class_type

    def get_is_available(self):
        return self.__is_available

    def set_seat_number(self, seat_number):
        self.__seat_number = seat_number

    def set_class_type(self, class_type):
        self.__class_type = class_type

    def set_is_available(self, is_available):
        self.__is_available = is_available

    def reserve(self):
        self.__is_available = False

    def release(self):
        self.__is_available = True


passenger = Passenger("ZAYED KHALID", "zkhalid@email.com")
flight = Flight(
    "NA4321",
    datetime(2023, 12, 10, 11, 40),
    datetime(2023, 12, 10, 13, 30),
    "ABU DHABI AUH",
    "DUBAI DXB",
)
seat = Seat("09A", "First")
boarding_pass = BoardingPass(
    flight, passenger, seat, "03", datetime(2023, 12, 10, 11, 20)
)

# Add seat
flight.add_seat(seat)

# Add boarding pass
passenger.add_boarding_pass(boarding_pass)

# Display boarding pass details
boarding_pass.display_details()
