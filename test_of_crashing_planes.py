from numpy import arange
import random
from tkinter import *
from math import cos, sin, pi
from time import sleep
from sympy import Point, Line, Segment

number_of_planes = int(input("Сколько самолётов запустим?"))

class Plane(object):# Описываем самолёт как класс.
    def __init__ (self, number, x_position, y_position, old_x, old_y, speed, direction):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position
        self.old_x = old_x
        self.old_y = old_y
        self.speed = speed
        self.direction = direction

    def __str__ (self):
        return "cамолёт №{}, старое положение {}, {}, новое положение {},{}".format(self.number,self.old_x, self.old_y, self.x_position, self.y_position)

    def fly(self): # Функция, описывающая перемещение самолёта на каждом ходе.
        # Задаём случайную скорость.
        self.speed = random.randrange(300,1000)
        # Случайно изменение направления. Чтобы не накручивать слишком большое количество градусов, контролируем, чтобы итоговое значение осталось в пределах 360.
        if self.direction >=15 or self.direction <= 345:
            self.direction = self.direction + random.randrange(-15,16)
        elif self.direction < 15:
            self.direction = self.direction + random.randrange (0,16)
        else:
            self.direction = self.direction - random.randrange (0,16)
        # Перед изменением позиции запоминаем предыдущее положение.
        self.old_x = self.x_position
        self.old_y = self.y_position
        # Вычисляем новое положение.
        self.x_position = round (self.x_position + self.speed * cos(self.direction*pi/180),2)
        self.y_position = round(self.y_position + self.speed * sin(self.direction*pi/180),2)

    def out(self): # Функция для определения вылета за пределы поля.
        if self.x_position > 5000 or self.y_position > 5000 or self.x_position < 0 or self.y_position < 0: 
            return 1
        else:
            return 0

    def crash(self,other): # Функция для определения столкновения двух самолётов. Мы создаём для каждого самолёта по отрезку от старого положения до нового. Функция возвращает список точек пересечения двух отрезков. Если длина списка нулевая, пересечения нет. Если больше 0, значит пересечение есть и самолёты столкнулись.
        seg1_1 = Point(self.old_x,self.old_y)
        seg1_2 = Point(self.x_position,self.y_position)
        seg2_1 = Point(other.old_x,other.old_y)
        seg2_2 = Point(other.x_position,other.y_position)
        seg1 = Segment(seg1_1,seg1_2)
        seg2 = Segment(seg2_1,seg2_2)
        return len(seg1.intersection(seg2))

pos_random = arange(1,5000,0.1)
dir_random = range(1,360,1)
planes = list()

for i in range(1,number_of_planes+1): # Создаём самолёты в том количестве, которое получили от пользователя.
    a = Plane(i,round (random.choice(pos_random),2),round(random.choice(pos_random),2),0,0,0,random.choice(dir_random))
    planes.append(a)

count = 1 # Номер хода.

for f in planes: #Первый полёт.
    f.fly()

while True:
    print("Ход №{}".format(count))

    for cr in planes:
        # Берём каждый самолёт в списке и проверяем на столкновение с каждым последующим из списка.
        current_plane = cr
        current_plane_index = planes.index(cr)
        for an in planes[current_plane_index+1:number_of_planes]:
            if current_plane.crash(an)>0:
                another_plane = an
                another_plane_index = planes.index(another_plane)
                print("Cтолкнулись самолёты {} и {}.".format(current_plane,another_plane))
                del planes[another_plane_index]
                del planes[current_plane_index]
        
    for off in planes:
        if off.out()==1:
            planes.remove(off)
            print("{} покинул поле.".format(off))

    for n in planes:
        n.fly()

    count = count + 1

    # Если список самолётов опустел, то и мы завершаем.
    if len(planes) == 0:
        break

print("самолётов больше не осталось")
