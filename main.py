import psutil

def convertime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d"%(hours, minutes, seconds)

battery = psutil.sensors_battery()
print("バッテリ残量: ", battery.percent,"%")
print("充電中: ", battery.power_plugged)
print("バッテリ時間: ", convertime(battery.secsleft))
