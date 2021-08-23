from interface_low.DroneController import DroneController



START_X = 250
START_Y = 250

SIZE_X = 500
SIZE_Y = 500

DEFAULT_MOVE_SIZE = 20

class patrouille:
    def __init__(self):
        self.actionList = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        self.DC = DroneController()
        """
        0 tout droit
        1 left
        2 bas
        3 right
        """

    def __init_map(self):
        self.map = [[False]*(SIZE_X / 20)]*(SIZE_Y / 20)
        self.map[self.map.len() / 2][self.map[self.map.len()].len() / 2] = True
        self.posx = self.map.len() / 2
        self.posy = self.map[self.map.len()].len() / 2
    
    def __move(self, actionId):
        if actionId == 0:
            self.DC.forwardcm(DEFAULT_MOVE_SIZE)
        elif actionId == 1:
            self.DC.leftcm(DEFAULT_MOVE_SIZE)
        elif actionId == 2: 
            self.DC.backwardcm(DEFAULT_MOVE_SIZE)
        elif actionId == 3:
            self.DC.rightcm(DEFAULT_MOVE_SIZE)

    def start(self):
        self.__init_map()
        self.DC = DroneController()
        self.upcm(100)
        for action in self.actionList:
            if (action == 0):
                self.DC.forwardcm(DEFAULT_MOVE_SIZE)
            else:
                break
        self.actionList = self.actionList[3:] 

    def destroy(self):
        self.DC.destroy()


    def featuresloop(self):
        index = 0

        while self.__running == True:
            if (index not in range(0, len(self.actionList))): index = 0
            self.__move(self.actionList[index])
            index += 1

    def activate(self):
        self.__running = True

    def desactivate(self):
        self.__running = False
