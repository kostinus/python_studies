#from numpy import arange 
import random

class Plane(object):
    def __init__(self,number,x_position,y_position,speed,direction):
        self.number=number
        self.x_position=x_position
        self.y_position=y_position
        self.speed=speed
        self.direction=direction

    def __str__(self):
        return "Cамолёт {} c направлением {} и скоростью {} километров в час находится по координатам {}/{}".format(self.number,self.direction,self.speed,self.x_position,self.y_position)

    def start(self):
        if self.direction == 'up':
            self.y_position = self.y_position - self.speed/10
        elif self.direction == 'right':
            self.x_position = self.x_position + self.speed/10
        return self.x_position, self.y_position

    def fly(self):
        if self.direction == 'up':
            self.y_position = self.y_position - self.speed/10
        elif self.direction == 'right':
            self.x_position = self.x_position + self.speed/10
        return self.x_position, self.y_position

    def crash(self,other):
        if self.x_position == other.x_position and self.y_position == other.y_position:
            return 1
        else:
            return 0

direction = ['up','right']
speed = range(200,1100,100)


    def __str__(self):
        return "Аэропорт {}, находящийся по координатам {}/{}".format(self.name,self.x_position,self.y_position)

aeroports = []
a = Aeroport('LED',100,100)
b = Aeroport('BSN',300,300)
c = Aeroport('CDG',700,900)
aeroports.append(a)
aeroports.append(b)
aeroports.append(c)

planes=[]
test_plane = Plane(0,1000,100,0,'right')
planes.append(test_plane)
k = 1

for i in aeroports:
    d = Plane(k,float(i.x_position),float(i.y_position),random.choice(speed),random.choice(direction))
    d.start()
    planes.append(d)
    print(d)
    k = k + 1

for x in planes:
    x.fly()
    print(x)

for x in planes:
    x.fly()
    print(x)