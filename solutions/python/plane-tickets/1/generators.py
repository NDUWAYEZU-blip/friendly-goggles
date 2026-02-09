"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    number_of_seats_supplementary = number - 4 
    seats_in_row = ["A","B","C","D"] 
    seats = [] 
    if number_of_seats_supplementary<0: 
        for seat in seats_in_row[:number]: 
            seats.append(seat) 
        for letter in seats: 
            yield letter 
    else: 
        for seat in seats_in_row: 
            yield seat 
            if number_of_seats_supplementary > 0: 
                seats_in_row.append(seat) 
                number_of_seats_supplementary-= 1 
            continue
        
def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = ["A", "B", "C", "D"]
    seat_count = 0
    row = 1

    while seat_count < number:
        if row == 13:
            row += 1
            continue

        for letter in seat_letters:
            if seat_count >= number:
                return
            yield f"{row}{letter}"
            seat_count += 1

        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    number_of_passengers = len(passengers)
    passengers_seat = generate_seats(number_of_passengers)
    each_passengers_seat = {}
    for passenger in passengers:
        each_passengers_seat[passenger] = passengers_seat.__next__()
    return each_passengers_seat

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        code = seat+flight_id
        additional_num = 12 - len(code)
        additional_zero = ""
        for zero in range(additional_num):
            zero = "0"
            additional_zero+= zero
        yield f"{seat}{flight_id}{additional_zero}"
    
