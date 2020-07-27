import launches
import time
import datetime

try:
    launch = launches.get_next_launch()
    mission_name = launch['mission_name']
    launch_date_unix = launch['launch_date_unix']
    now = int(time.time())
    seconds_left = launch_date_unix - now

    # The notification should trigger when less than 1 hour is left
    if seconds_left < 3600:
        minutes = int(seconds_left / 60)
        print('The mission ' + mission_name + ' will launch in ' + str(minutes) + ' minutes')
        # TODO: Send cloud message here
    else:
        launch_date = datetime.datetime.fromtimestamp(launch_date_unix).strftime('%d.%m.%Y %H:%M:%S')
        print('The mission ' + mission_name + ' will launch on ' + launch_date)
except:
    print('An error occured')
