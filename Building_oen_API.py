from flask import Flask, jsonify, request
from Flights_data import flights
from utils import search_flight, get_index

app = Flask(__name__)


# Main host address: IP address - when this machine is your machine - 127.0.0.1,
# Usually translates to local host
# Machines can await for payloads/requests on different ports,
# So they can run multiple applications at a time
# (e.g. one machine can be running an HTTP sever and database server)

# Protocol HTTP for communication - http://
# http://localhost:5000 - base URL
# endpoint - which is the path that comes after your base url
@app.route("/")  # http://localhost:5000
def hello():
    return {"hello": "Universe"}


@app.route("/flights")
def get_flights():
    return jsonify(flights)


@app.route("/flights/<int:id>")
def get_flight_by_id(id):
    return search_flight(id, flights)


@app.route("/flights", methods=["POST"])
def add_flight():
    flight = request.get_json()
    flight.append(flight)
    return flight

@app.route("/flights/<int:id>", methods=["PUT"])
def update_flight(id):
    flight_to_update = request.get_json()
    index = get_index(id, flights)
    flights[index] = flight_to_update
    return jsonify(flights[index])


@app.route("/flights/<int:id>", methods=["DELETE"])
def delete_flight(id):
    index = get_index(id, flights)
    deleted = flights.pop(index)
    return jsonify(deleted)


if __name__ == "__main__":
    app.run(debug=True)
