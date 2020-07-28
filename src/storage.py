import pickle

filename = 'latest_flight_sent.data'

# Returns the latest flight number a message has been sent for
# This prevents the server to trigger a message every time the script is called when less than 1 hour remains
def get_latest_flight_sent():
    try:
        stream = open(filename, 'rb')
        flight_number = pickle.load(stream)
        return flight_number
    except:
        return -1

def set_latest_flight_sent(flight_number):
    stream = open(filename, 'wb')
    pickle.dump(flight_number, stream)
    stream.close()