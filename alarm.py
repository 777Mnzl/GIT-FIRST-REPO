from playsound import playsound
import time

CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'


def alarm(seconds):
    time_elapsed = 0
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        seconds_left = time_left % 60
        print(f'{CLEAR_AND_RETURN}{minute_left:02d}:{seconds_left:02d}')


minutes = int(input('how many minutes to wait: '))
secounds = int(input('how many seconds to wait: '))
total_seconds = minutes * 60 +secounds

alarm(total_seconds)

