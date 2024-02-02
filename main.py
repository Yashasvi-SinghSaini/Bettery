import psutil
from playsound import playsound
import time


while True:
    bt_char = psutil.sensors_battery().power_plugged            #Checks whether charging or not

    if bt_char==True:
        bt_perc = psutil.sensors_battery().percent              #Checks Battery level

        if bt_perc==100:
            playsound('bettery_baja.wav')
            continue

        else:
            time.sleep(15)
            continue

    else:
        time.sleep(15)
        continue