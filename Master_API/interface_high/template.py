from interface_low.DroneLibrary import DroneLibrary
from time import sleep
import requests


class template_interface:

    def __init__(self, x, y, minusX, minusY):
        """
        vous pouvez en ajouter au besoin
        """

        self.x = x
        self.y = y
        self.minusX = minusX
        self.minusY = minusY
        self.users = {"ThibaultJ": 1, "ThibaultD": 2, "Louis": 3, "Gustave": 4, "Leo": 5, "Simon": 6}
        self.coordinates = [self.x, self.y, self.minusX, self.minusY]

    def start(self):
        """
        permet de faire des initialisation de votre coté, test de connection ....
        """

        droneControl = DroneLibrary()
        droneControl.setSpeed(10)  # 10cm/s

        droneParams = droneControl.getAllowedData()
        droneBattery = droneParams[4]
        flightTime = droneParams[7]

        testResponse = droneControl.test()

        if testResponse == "test":
            print("The test has been successful the drone can fy !")

        print("The drone has been flying for " + flightTime + " min")

        if droneBattery < 20:
            print('The drone battery is too low to begin a flight')
        else:
            droneControl.takeOff()

    def destroy(self):
        """
        potentiellement vide, avec de la suppression d'infomation si vous créer des object le nécissitant. 
        """
        pass

    def featuresloop(self):
        """
        la boucle infinie de la features est ici
        """
        while self.__running == True:
            """
            logique de la fonction
            """
            self.createRoomPattern(200)

    def activate(self):
        """
        activer la features
        """
        self.__running = True

    def desactivate(self):
        """
        desacative la features
        """
        self.__running = False

    def resetCoordinates(self):
        self.x, self.y, self.minusY, self.minusX = 0

    def printCoordinates(self):
        for coordinate in self.coordinates:
            print("The X,Y drone coordinates are ", "x : ", self.coordinates[coordinate], " y : ",
                  self.coordinates[coordinate])
            print("The minusX, minusY drone coordinates are ", "minusX : ", self.coordinates[coordinate], " minusY : ",
                  self.coordinates[coordinate])

    def createRoomPattern(self, tailleCarre):
        droneControl = DroneLibrary()

        droneParams = droneControl.getAllowedData()
        droneBattery = droneParams[4]
        flightTime = droneParams[7]
        xSpeed = droneParams[19]
        ySpeed = droneParams[20]
        distance = 0

        for i in range(0, 5):
            distance = 60
            if xSpeed != 0:
                intervalT = distance / xSpeed
            elif ySpeed != 0:
                intervalT = distance / ySpeed

            droneControl.forwardCm(distance)
            self.y = distance
            print("The drone has been moving", distance, "forward in ", intervalT)
            self.printCoordinates()

            droneControl.leftCm(distance)
            self.minusX = distance
            print("The drone has been moving", distance, "left in ", intervalT)
            self.printCoordinates()

            droneControl.backwardCm(distance)
            self.y = 0
            print("The drone has been moving", distance, "backward in ", intervalT)
            self.printCoordinates()

            droneControl.rightCm(distance)  # point de départ
            self.resetCoordinates()
            print("The drone has been moving", distance, "right in ", intervalT)
            self.printCoordinates()

            droneControl.forwardCm(distance)
            self.y = distance
            print("The drone has been moving", distance, "forward in ", intervalT)
            self.printCoordinates()

            droneControl.backwardCm(distance)
            self.resetCoordinates()
            print("The drone has been moving", distance, "backward in ", intervalT)
            self.printCoordinates()

        print("The drone has finished his flight!! Landing :)")
        droneControl.land()
