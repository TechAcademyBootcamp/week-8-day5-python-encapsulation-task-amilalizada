class Vehicle():
    positionX = 1
    positionY = 1 
    speed = 100 
    isOn = False
    def __init__(self, color_, engine_, numofWheels_):
        self.color = color_
        self.engine = engine_
        self.numofWheels = numofWheels_

    def accelerate(self):
        self.isOn = True
        if self.isOn==True:
            self.speed+=1
        else:
            print('ise sal')
    
    def moveForward(self,x,y):
        self.positionX+=x
        self.positionY+=y

    def moveBackwards(self, x, y):
        self.positionX -= x
        self.positionY -= y
    
    def ignition(self):
        if self.isOn==True:
            self.isOn=False
        else:
            self.isOn=True
    
    def getNumofWheels(self):
        return self.numofWheels

    def setNumofWheels(self, num):
        self.numofWheels = num

    def getColor(self):
        return self.color 

    def setColor(self,colorr):
        self.color= colorr 

    def __str__(self):
        return f'{self.color},{self.engine},{self.numofWheels}'

class Motocycle(Vehicle):
    brandd = 'bmw'
    numofSeats=2
    color='red'
    engine=3
    wheels=2
    
    def __init__ (self,color, engine, wheels, brand, seats):
        self.color=color
        self.engine=engine
        self.wheels=wheels
        self.brand=brand
        self.seats=seats
    
    def getBrand(self):
        return self.brand
    def getnumofSeats(self):
        return self.seats
    def setBrand(self,brand):
        self.brand=brand
    def setnumofSeats(self,numofSeats):
        self.seats=numofSeats
    def accelerate(self):
        self.speed+=1
    def decelerate(self):
        self.speed-=1

vehicle = Vehicle('RED',3,4)
vehicle.accelerate()

vehicle.moveForward(2,2)
vehicle.moveBackwards(2,2)
vehicle.ignition()
vehicle.getNumofWheels()
vehicle.setNumofWheels(5)
vehicle.getColor()
vehicle.setColor('black')

moto = Motocycle('yellow',2,4,5,6)
moto.getBrand()
moto.getnumofSeats()
moto.setBrand('merc')
moto.accelerate()
moto.decelerate()
moto.setnumofSeats(3)

print(vehicle)
