import launches
import time
import storage

def send_cloud_message(mission_name, minutes):
    # TODO: Send cloud message here
    print('The mission ' + mission_name + ' will launch in ' + str(minutes) + ' minutes')
    return True

# Returns True when the message was sent, False otherwise
def send_next_launch_message():
    launch = launches.get_next_launch()

    if launch == 0:
        return False

    try:
        mission_name = launch['mission_name']
        launch_date_unix = launch['launch_date_unix']
        flight_number = launch['flight_number']
        now = int(time.time())
        seconds_left = launch_date_unix - now

        # The notification should only trigger when less than 1 hour is left until takeoff
        if seconds_left <= 0 or seconds_left > 3600:
            return False

        # Check whether the notification for this flight has already been sent
        latest_flight_sent = storage.get_latest_flight_sent()
        if latest_flight_sent == flight_number:
            return False

        minutes = int(seconds_left / 60)
        message_sent = send_cloud_message(mission_name, minutes)

        if message_sent:
            storage.set_latest_flight_sent(flight_number)
    except:
        return False
