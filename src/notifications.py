import launches
import time
import datetime

def send_cloud_message(mission_name, minutes):
    # TODO: Send cloud message here
    print('The mission ' + mission_name + ' will launch in ' + str(minutes) + ' minutes')

def send_next_launch_message():
    launch = launches.get_next_launch()

    if launch == 0:
        print('Unable to fetch launch')
        return

    try:
        mission_name = launch['mission_name']
        launch_date_unix = launch['launch_date_unix']
        now = int(time.time())
        seconds_left = launch_date_unix - now

        # The notification should trigger when less than 1 hour is left until takeoff
        if seconds_left > 0 and seconds_left < 3600:
            minutes = int(seconds_left / 60)
            send_cloud_message(mission_name, minutes)
        # The following section can be enabled for debugging - no need to print the same stuff every time the script is executed on the server
        # else:
        #     launch_date = datetime.datetime.fromtimestamp(launch_date_unix).strftime('%d.%m.%Y %H:%M:%S')
        #     print('The mission ' + mission_name + ' will launch on ' + launch_date)
    except:
        print('An error occured')
