# InventWithPython Exercise number 11

"""
Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. 
The argument for this parameter will be the number of seconds to be translated 
into the number of hours, minutes, and seconds. If the amount for the hours, minutes, 
or seconds is zero, don't show it: the function should return '10m' rather than '0h 10m 0s'. 
The only exception is that getHoursMinutesSeconds(0) should return '0s'
"""

def getHoursMinutesSeconds(seconds):
    if seconds == 0:
        return "0s"

    timestamp = ""
    if int(seconds / 3600) > 0:
        hours = int(seconds / 3600) 
        timestamp += str(hours) + "h "
        seconds = seconds % 3600

    if int(seconds / 60) > 0:
        minutes = int(seconds / 60)
        timestamp += str(minutes) + "m "
        seconds = seconds % 60

    if seconds != 0:
        timestamp += str(seconds) + "s"
    
    timestamp = timestamp.strip()
    return timestamp


assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'

print("Ex11 Done")