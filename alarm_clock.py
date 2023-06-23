from datetime import datetime
from music import music
alarm_time = input("ENTER THE TIME TO SET ALARM:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("SETTING UP ALARM...")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if (alarm_hour==current_hour):
            if (alarm_minute==current_minute):
                if (alarm_seconds==current_seconds):
                    print("WAKIE WAKIE BOOKIE DOO!!!")
                    music('audio.mp3')
                    break



