class Vehicle():
    positionX = 1
    positionY = 1 
    speed = 100 
    isOn = False
    def __init__(self, color_, engine_, numofWheels_):
        self.__color = color_
        self.__engine = engine_
        self.__numofWheels = numofWheels_

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

    @property
    def NumofWheels(self):
        return self.__numofWheels

    @NumofWheels.setter
    def NumofWheels(self, num):
        self.__numofWheels = num

    @property
    def Color(self):
        return self.__color 

    @Color.setter
    def Color(self,colorr):
        self.__color=colorr 

    def __str__(self):
        return f'{self.__color},{self.__engine},{self.__numofWheels}'

vehicle = Vehicle('red',1,2)
print(vehicle.Color)
vehicle.Color='green'
print(vehicle.Color)
vehicle.numofWheels=8
