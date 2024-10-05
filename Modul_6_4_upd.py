import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=True):
        self.color = __color
        self.sides = list(__sides) if self.__is_valid_sides(__sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self, *__color):
        return self.color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= int(self.r) <= 255 and 0 <= int(self.g) <= 255 and 0 <= int(self.b) <= 255:
            return r, g, b
        else:
            return self.color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.color = list(new_color)
        return self.color

    def __is_valid_sides(self, new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if side <= 0:
                return False
        return True

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *__sides):
        super().__init__(color, *__sides)
        self.radius = self.get_sides()[0] / (2 * math.pi)


    def get_square(self, __radius):
        Sc = math.pi * (self.radius ** 2)
        return Sc


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides, filled=True):
        super().__init__(__color, *__sides, filled)
        self.sides = __sides

    def get_square(self):
        p = sum(self.sides) * 0.5
        St = (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
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
triangle1 = Triangle((200, 200, 100), 5, 8, 12)

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

# Проверка площади (треугольника):
#print(len(triangle1))
#print(triangle1.get_square())
