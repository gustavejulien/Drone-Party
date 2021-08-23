import math as math


def calcCircle(self, velocite, divisions, radio):
    points = []

    # On divise le cercle à differents points avec la meme separation
    gradAn = 360 / divisions # angle en degrès 
    radAn = (gradAn * math.pi)/180 # rayon du cercle 

# On a les différents points de circumférences grâce à l'angle
    p0x = radio
    p0y = 0
    p0z = 0
    points.append((p0x, p0y, p0z))

# Interval de temps distance / velocite
    time = (2.0 * float(radio)/float(velocite)) * math.sin(float(radAn))/2.0

    for item in range(divisions):
        
        point = item + 1
        px = radio * math.cos(point * radAn)
        py = radio * math.sin(point * radAn )
        points.append((round(px), round(py), 0))

    return points, time

def arc(self, velocite, divisions, radio, initialP, finalP):

    points, time = self.calcCircle(velocite, divisions, radio)

    newPoints = []

# InitialP = point de départ de l'arc et finalP = point d'arret
    if initialP > finalP:
        finalP = finalP + divisions

    for item in range(initialP, finalP + 1):
        position = item 

        if position >= divisions:
            position = position - divisions

        newPoints.append(points[position])
    return newPoints, time

# Diagonal avec un angle choisie
def diagonal(self, velocite, divisions, radio, direcAng, distance):

    # On crée un cercle et en fonction de l'angle on calcule les points 
    points, time = self.calcPtsCircle(velocite, divisions, radio)

    point = []

    divAng = self.div_ang(divisions)

    position = direcAng / divAng

    point = points[position]

    newTime = float(distance) / float(velocite)

    return point, newTime

# Commande si jamais utilisé permets d'envoyer les commandes en drone avec les bon coordonnées et la bonne intervalle de temps
def submitCommandToDrone(self, points, time):


    # Diagonal si plus de 3 points 
    if len(points) > 3:
        for item in points:

            x = item[0]
            y = item[1]
            z = item[2]

            self.tello(x, y, z, 0)
            time.sleep(time)

    elif len(points) <= 3:
        
        x = points[0]
        y = points[1]
        z = points[2]

        self.tello(x, y , z, 0)
        time.sleep(time)
    self.tello.stop()


# Changer les coordonnées d'un plan xy vers un plan x,z (default=x,y)
def changeCoord(self, points, plan):

    newPoints = []

    if len(points) > 3:

        for item in points:
            x = item[0]
            y = item[1]
            z = item[2]


            if plan is 'xz': 

                new_X = x
                new_Y = y
                new_Z = z

                newPoints.append((int(new_X), int(new_Y), int(new_Z) ))



# Example 

# Le drone va effectuer un cercle dans le plan x,y 
points, time = calcCircle(30,24,30) 
submitCommandToDrone(points, time)

# Dans ce cas il va effectuer un un arc dans le plan x,z
points, time = arc(30,24,30,4,8)
# On change les coordonnées pour les passer dans le plan x, z (car default en x, y)
points = changeCoord(points, 'xz')
submitCommandToDrone(points, time)

points, time = diagonal(30, 24, 30, 210, 40)
