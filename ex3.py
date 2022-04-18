import math


class BaseConverter:
    # Конвертация из заданных градусов в градусы Цельсия, Кельвина, Фаренгейта
    # На вход принимает значения в градусах и размерность("C", "K" или "F")
    # Возвращает два значения в вышеописанном порядке
    def __init__(self, degree, name):
        self.degree = degree
        self.name = name

    def convert(self):
        if self.name == "C":
            return [self.degree, round(self.degree + 273.15, 2),
                    round(self.degree*9/5 + 32, 2)]
        elif self.name == "K":
            return [round(self.degree - 273.15, 2), self.degree,
                    round((self.degree - 273.15)*9/5 + 32, 2)]
        elif self.name == "F":
            return [round((self.degree - 32)*5/9, 2),
                    round((self.degree - 32)*5/9 + 273.15, 2), self.degree]
        else:
            return

# Возможный вариант использования класса
# p = BaseConverter(float(input("Enter a temperature: ")),
#                   str(input("Enter a dimension(\"C\", \"K\" or \"F\"): ")))
# tmp_arr = p.convert()
# if not tmp_arr:
#     print("\033[1;33mPls, enter a valid dimension!\033[1;37m")
# else:
#     print("{}°C {}°K {}°F".format(tmp_arr[0], tmp_arr[1], tmp_arr[2]))
