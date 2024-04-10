
#Return the flight from the given flights which has the given flight ID
def search_flight(fid, flights):
    return [element for element in flights if element['flight_id'] == fid]

#Return the position (index) of the flight from the given flights which has the given flight ID
def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1