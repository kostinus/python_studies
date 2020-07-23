from numpy import arange
import random
from tkinter import *
from math import cos, sin, pi
from time import sleep
from sympy import Point, Line, Segment

number_of_planes = int(input("Сколько самолётов запустим?"))

root = Tk()
root.title("Полетаем?")
root.attributes("-topmost", True)
#root.attributes("-fullscreen", True)
canvas = Canvas(width = 500, height = 500,bg="white") # Поскольку мне надо, чтобы всё поместилось на экране, отображение будет в масштабе 1 к 10. 
canvas.pack()

class Plane(object):
    def __init__ (self, number, x_position, y_position, old_x, old_y, speed, direction,colour):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position
        self.old_x = old_x
        self.old_y = old_y
        self.speed = speed
        self.direction = direction
        self.colour = colour

    def __str__ (self):
        return "cамолёт №{}, координаты {},{}, скорость {}, направление {}.".format(self.number,self.x_position,self.y_position,self.speed,self.direction)


    def fly(self): # Функция, описывающая перемещение самолёта на каждом ходе.
        # Если поле 5000 на 5000, а скорость до 1000, то всё закончится слишком быстро, поэтому считаем, что десять единиц скорости покрывают одну единицу поля. Скорость назначается при каждом ходе в диапазоне между условными 300 и 1000 единицами за один ход.
        self.speed = random.randrange(30,100)
        # Тут, чтобы не накручивать слишком большое количество градусов, контролируем, чтобы итоговое значение осталось в пределах 360.
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

    def crash(self,other):
        seg1_1 = Point(self.old_x,self.old_y)
        seg1_2 = Point(self.x_position,self.y_position)
        seg2_1 = Point(other.old_x,other.old_y)
        seg2_2 = Point(other.x_position,other.y_position)
        seg1 = Segment(seg1_1,seg1_2)
        seg2 = Segment(seg2_1,seg2_2)
        if len(seg1.intersection(seg2)) > 0:
            return 1
        else:
            return 0
            pass

    def visual(self): # Визуализация полёта самолёта. Поскольку мне надо, чтобы всё поместилось на экране, рисуем в масштабе 1 к 10. Все значения для визуализации делим на 10.
         # Рисуем вектор, где начальная точка – это предыдущее положение, а конечная точка – новое положение.
        canvas.create_line(self.old_x/10,self.old_y/10,self.x_position/10,self.y_position/10, fill = self.colour, arrow=LAST, tag = "visual_plane")
        # Создаём текстовую метку с номером самолёта, которая будет отображаться рядом с ним.
        if self.x_position < 50:
            text_x = self.x_position/10 + 10
        else:
            text_x = self.x_position/10
        if self.y_position/10 < 450:
            text_y = (self.y_position + 100)/10 + 5
        else:
            text_y = self.y_position/10 - 15
        canvas.create_text(text_x, text_y, text = self.number,fill = self.colour, tag = "visual_plane")

pos_random = arange(1,5000,0.1)
speed_random = range(30,100,1)
dir_random = range(1,360,1)
planes = list()
planes_for_compare = list()

def plane_colour(): # Это функция для случайного выбора цвета самолёта.
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    digit_array = []

    for m in range(6):
        digit_array.append(hex_digits[random.randint(0,15)])
    joined_digits = ''.join(digit_array)

    colour = '#' + joined_digits
    return colour

for i in range(1,number_of_planes+1): # Создаём самолёты в том количестве, которое получили на входе.
    a = Plane(i,round(random.choice(pos_random),2),round(random.choice(pos_random),2),0,0,0,random.choice(dir_random),plane_colour())
    planes.append(a)
# Рисуем сетку.
for g in range(0,500,50):
    canvas.create_line(0,g,1000,g,fill="#A0A0A0")
    canvas.create_line(g,0,g,1000,fill="#A0A0A0")
    canvas.create_text(g+15,10,text = g*10,fill="#A0A0A0",justify=LEFT)
    if g > 0:
        canvas.create_text(15,g+10,text = g*10, fill="#A0A0A0",justify=LEFT)

# Рисуем обратный отсчёт.
for c in range(3,0,-1):
    countdown = canvas.create_text(250,250,text=c,fill="red",font=50)
    canvas.update()
    sleep(1)
    canvas.delete(countdown)
countdown = canvas.create_text(250, 250, text="полетели!", fill="red",font=50)
canvas.update()
sleep(1)
canvas.delete(countdown)

count = 1 # Номер хода.

while True:
    canvas.delete("visual_plane")
    sleep(0.5)
    for j in planes:
        # Проверяем, не покинул ли самолёт поле.
        if j.out()==1:
            canvas.delete("message")
            planes.remove(j)
            canvas.create_text(250,30,text="на ходу №{} самолёт №{} покинул поле".format(count,j.number),fill="red",tag = "message")
            canvas.update()
            print("Ход {}: {} покинул поле.".format(count, j))
        j.fly()
        j.visual()
    canvas.update()
    count = count + 1

    # Если список самолётов опустел, то и мы завершаем.
    if len(planes) == 0:
        canvas.delete("visual_plane")
        break
sleep(1)    
canvas.delete("message")
canvas.create_text (250,250,text="самолётов больше не осталось", font = "50", fill="red")
canvas.update()
root.mainloop()