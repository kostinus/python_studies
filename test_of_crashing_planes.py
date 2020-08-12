from numpy import arange # использовать системную переменную __name__
import random
import tkinter as tk
from math import cos, sin, pi
from time import sleep
from sympy import Point, Line, Segment

if __name__ == "__main__":
    while True:
        try:
            user_value = input("Сколько самолётов запустим?")
            if int(user_value) > 0:
                number_of_planes = int(user_value)
                break
            elif int(user_value) <= 0:
                print ("Надо ввести положительное число.")
        except ValueError:
                print ("Надо ввести положительное число.")

root = tk.Tk()
root.title("Полетаем?")
root.attributes("-topmost", True)
#root.attributes("-fullscreen", True)
canvas = tk.Canvas(width = 500, height = 500,bg="white") # Поскольку мне надо, чтобы всё поместилось на экране, отображение будет в масштабе 1 к 10. 
canvas.pack()

class Plane(object):# Описываем самолёт как класс.
    def __init__ (self, number, x_position, y_position, new_x_position, new_y_position, speed, direction, colour):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position
        self.new_x_position = new_x_position
        self.new_y_position = new_y_position
        self.speed = speed
        self.direction = direction
        self.colour = colour

    def __str__ (self):
        return "cамолёт №{}, старое положение {}, {}, новое положение {},{}, скорость {}, направление {}".format(self.number,self.x_position, self.y_position, self.new_x_position, self.new_y_position,self.speed,self.direction)

    def fly(self): # Функция, описывающая перемещение самолёта на каждом ходе.
        # Вычисляем новое положение.
        self.x_position = self.new_x_position
        self.y_position = self.new_y_position
        self.new_x_position = round (self.x_position + self.speed * cos(self.direction*pi/180),2)
        self.new_y_position = round(self.y_position + self.speed * sin(self.direction*pi/180),2)
        # Случайно изменение направления. Чтобы не накручивать слишком большое количество градусов, контролируем, чтобы итоговое значение осталось в пределах 360.
        if self.direction >=15 or self.direction <= 345:
            self.direction = self.direction + random.randrange(-15,16)
        elif self.direction < 15:
            self.direction = self.direction + random.randrange (0,16)
        else:
            self.direction = self.direction - random.randrange (0,16)
        self.speed = random.choice(speed_random)

    def out(self): # Функция для определения вылета за пределы поля.
        if self.new_x_position > 5000 or self.new_y_position > 5000 or self.new_x_position < 0 or self.new_y_position < 0: 
            return 1
        else:
            return 0

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

    def crash(self,other): # Функция для определения столкновения двух самолётов. Мы создаём для каждого самолёта по отрезку от старого положения до нового. Функция возвращает список точек пересечения двух отрезков. Если длина списка нулевая, пересечения нет. Если больше 0, значит пересечение есть и самолёты столкнулись.
        seg1_1 = Point(self.x_position,self.y_position)
        seg1_2 = Point(self.new_x_position,self.new_y_position)
        seg2_1 = Point(other.x_position,other.y_position)
        seg2_2 = Point(other.new_x_position,other.new_y_position)
        seg1 = Segment(seg1_1,seg1_2)
        seg2 = Segment(seg2_1,seg2_2)
        return len(seg1.intersection(seg2))

def plane_colour(): # Это функция для случайного выбора цвета самолёта.
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    digit_array = []
    for m in range(6):
        digit_array.append(hex_digits[random.randint(0,15)])
    joined_digits = ''.join(digit_array)
    colour = '#' + joined_digits
    return colour

pos_random = arange(1,5000,0.1)
dir_random = range(1,360,1)
speed_random = range(300,1001,100)
planes = list()

for i in range(1,number_of_planes+1): # Создаём самолёты в том количестве, которое получили на входе.
    a = Plane(i,round (random.choice(pos_random),2),round(random.choice(pos_random),2),0,0,random.choice(speed_random),random.choice(dir_random),plane_colour())
    a.new_x_position = a.x_position
    a.new_y_position = a.y_position
    print(a)
    planes.append(a)
# Рисуем сетку.
for g in range(0,500,50):
    canvas.create_line(0,g,1000,g,fill="#A0A0A0")
    canvas.create_line(g,0,g,1000,fill="#A0A0A0")
    canvas.create_text(g+15,10,text = g*10,fill="#A0A0A0",justify="left")
    if g > 0:
        canvas.create_text(15,g+10,text = g*10, fill="#A0A0A0",justify="left")

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

for i in range(1,number_of_planes+1): # Создаём самолёты в том количестве, которое получили от пользователя.
    a = Plane(i,round (random.choice(pos_random),2),round(random.choice(pos_random),2),0,0,speed_random,random.choice(dir_random), plane_colour)
    a.new_x_position = a.x_position
    a.new_y_position = a.y_position
    planes.append(a)

count = 1 # Номер хода.

while True:
    print("Ход №{}".format(count))
    for f in planes:
        f.fly()
        #print(f)

    for off in planes:
        #print(off, off.out)
        if off.out()==1:
            planes.remove(off)
            print("{} покинул поле.".format(off))

    for cr in planes:
        # Берём каждый самолёт в списке и проверяем на столкновение с каждым последующим из списка.
        current_plane = cr
        current_plane_index = planes.index(cr)
        for an in planes[current_plane_index+1:number_of_planes]:
            if current_plane.crash(an) > 0:
                another_plane = an
                another_plane_index = planes.index(an)
                print("Cтолкнулись самолёты {} и {}.".format(current_plane,another_plane))
                del planes[another_plane_index]
                del planes[current_plane_index]
                break

    count = count + 1

    # Если список самолётов опустел, то и мы завершаем.
    if len(planes) == 0:
        break

print("самолётов больше не осталось")
