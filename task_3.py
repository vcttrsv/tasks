#Напишите класс BaseConverter для конвертации из градусов по Цельсию в
#Кельвины​, ​Фаренгейты​, и так далее. У метода должен быть метод convert, который
#и делает конвертацию.
#При запуске кода должна быть возможность ввести градусы Цельсия и выбора конвертации в Кельвины​ или ​Фаренгейты

class BaseConverter:
    def convert(self, unit, new_unit):
        if new_unit == "K":
            return unit + 273.15
        elif new_unit == "F":
            return unit * 9/5 + 32
        else:
            raise ValueError("Неверный ввод")

converter = BaseConverter()

unit = float(input("Введите градусы Цельсия: "))
temp = input("Выберите единицы измерения(K - Кельвин, F - Фаренгейт): ")

try:
    result = converter.convert(unit, temp)
    print(f"Температура в {temp} : {result} ")
except ValueError as err:
    print(err)
