class clock_hand():
    # Нахождение угла между часовой и минутной стрелками
    # Принимает часы и минуты
    # Возвращает угол в градусах или -1, если значения не валидны
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def angle(self):
        # Метод возвращает наименьший положительный угол между стрелками часов
        if (self.minutes < 0 or self.minutes > 60) \
                or (self.hours < 0 or self.hours > 24):
            return -1
        ang_min = (self.minutes * 6) % 360
        ang_hr = (self.minutes / 2 + (self.hours * 30)) % 360
        return round(abs(ang_hr - ang_min) if abs(ang_hr - ang_min) <= 180
                     else (360 - abs(ang_hr - ang_min)), 2)

# Возможный вариант использования
# p = clock_hand(round(float(input("Enter a hours: ")), 2),
#                round(float(input("Enter a minutes: ")), 1))
# ans_tmp = p.angle()
# if ans_tmp == -1:
#     print("\033[1;33mHey, valid format is [0, 24] "
#           "for hours and [0, 60] for minutes!\033[1;37m")
# else:
#     print("The angle between clock hands "
#           "is: ", ans_tmp, "°", sep="")
