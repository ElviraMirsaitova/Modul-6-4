import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=True):
        self.__color = __color
        self.__sides = list(__sides) if self.__is_valid_sides(*__sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self, *__color):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= int(self.r) <= 255 and 0 <= int(self.g) <= 255 and 0 <= int(self.b) <= 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self, *sides):
        are_positive_integers = True
        is_correct_count = len(sides) == self.sides_count
        for i in sides:
            if not isinstance(i, int) or i <= 0:
                are_positive_integers = False  # Если нет, меняем результат на False
                break
        return is_correct_count and are_positive_integers

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *__sides):
        super().__init__(color, *__sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)


    def get_square(self, __radius):
        Sc = math.pi * (self.__radius ** 2)
        return Sc


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides, filled)

    def get_square(self, __sides):
        self.__len__(__sides)
        p = self.summa * 0.5
        St = (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5
        return St


class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *__sides):
        if len(__sides) == 1:
            __sides = [__sides[0]] * self.sides_count
        super().__init__(__color, *__sides)


    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
