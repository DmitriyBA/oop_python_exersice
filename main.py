class Soda:

  def __init__(self, add_limon=""):
    self.add_limon = add_limon

  def show_my_drink(self):
    if str(self.add_limon) != "":
      print(f"Газировка и {self.add_limon}")
    else:
      print("Обычная газировка")


class TriangleChecker:

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def is_triangle(self):

    if type(self.a) != int or type(self.b) != int or type(self.c) != int:
      print("Нужно вводить только числа!")
    else:
      if self.a < 0 or self.b < 0 or self.c < 0:
        print("Вводить нужно только положительные числа")
      else:
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
          print("Ура можно построить треугольник")
        else:
          if (self.a + self.b <= self.c) or (self.b + self.c <= self.a) or (self.a + self.c <= self.b):
            print("Жаль, но из этого треугольник не сделать!")