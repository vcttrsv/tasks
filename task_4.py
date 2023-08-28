def hour_minutes_angle(hours, minutes):
    
    one_hour_angle = 360 / 12
    one_minute_angle = 360 / 60

    hour_angle = (hours % 12 + minutes / 60) * one_hour_angle
    minute_angle = minutes * one_minute_angle

    s_angle = abs(hour_angle - minute_angle)
    
    return min(s_angle, 360 - s_angle)

hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))
angle = hour_minutes_angle(hours, minutes)
print(f"Угол между стрелками: {angle} градусов")
