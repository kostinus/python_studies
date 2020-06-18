"""Python homework Planes
"""
import random
import math

class Plane(object):
  
  def __init__(self, number, company, x_position, y_position):
    """
    Описываем класс самолётов, который имеет такие атрибуты, как номер, авиакомпанию, координату по оси 0x и координату по оси 0y.
    """
    self.number = number
    self.company = company
    self.x_position = x_position
    self.y_position = y_position

  def __str__(self):
    return "самолёт авиакомпании {} номер {}, который находится в координатах x {}, y {}.".format(self.company,self.number,self.x_position,self.y_position)

  def distance(self,other):
    """
    Эта функция производит следующие вычисления:
    1. выясняем разницу между x-координатами двух самолётов, берём значение по модулю и возводим в квадрат
    2. выясняем разницу между y-координатами двух самолётов, берём значение по модулю и возводим в квадрат
    3. складываем полученные значения
    4. извлекаем их полученного значения квадратный корень
    >>>some_plane = Plane(1,"smth",1,2)
    >>>other_plane = Plane(2,"smth",3,4)
    >>>some_plane.distance(other_plane)
    8.61577310586391
    """
    dist = math.sqrt(abs(self.x_position - other.x_position)**2 + abs(self.y_position - other.y_position)**2)
    return dist

comp = "Aeroflot","Air France","KLM","Lufthansa","British Airways"

# Создаём 50 самолётов со случайными значениями. 
planes = list()
for i in range (0,50):
  onemore_plane = Plane(str(i),random.choice(comp), random.randrange(1,360,1), random.randrange(1,360,1))
  planes.append(onemore_plane)

#Выбираем случайный самолёт.
some_plane = random.choice(planes)
planes.remove(some_plane)


minimum = math.sqrt(360**2+360**2)
for i in planes:
  if some_plane.distance(i) < minimum:
    minimum = some_plane.distance(i)
    winner = i

#Выводим результаты
print("Абсолютно случайно был выбран", some_plane)
print("Ближайшим к нему является", winner)
print("Расстояние между двумя самолётами составило", int(minimum), "каких-то единиц (это мы округлили до целых).")