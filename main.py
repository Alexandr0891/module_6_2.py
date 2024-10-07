# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Vehicle:
    __COLOR_VARIANTS = ['white', 'black', 'blue', 'green', 'brown']
    def __init__(self,owner,__model,__color,__engine_power):
        self.owner = owner # владелец транспорта.(владелец может меняться)
        self.__model = __model     # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power # мощность двигателя.(мы не можем менять мощность двигателя самост.)
        self.__color = __color  # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def  get_model(self):
        return f"Модель{self.__model} "

    def  get_horsepower(self):
        return f"Мощность двигателя:{self.__engine_power}"

    def get_color(self):
        return f"Цвет:{self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')



    def set_color(self, new_color):
         self.new_color = new_color
         if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = self.new_color
         else:
            print(f'Нельзя сменить цвет на {self.new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # (в седан может поместиться только 5 пассажиров)


vehicle1 = Sedan('Ivan', ' Honda Acord ', 'red', 130)

vehicle1.print_info()

vehicle1.set_color('yellow')
vehicle1.set_color('white')
vehicle1.owner = 'Alex'

vehicle1.print_info()
