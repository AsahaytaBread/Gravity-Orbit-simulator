class CelestialBody:
    def __init__(self,mass,color,radius):
        self.mx=0
        self.my =0
        self.acceleration = 0
        self.mass = mass
        self.radius = radius
        self.force = self.mass * self.acceleration
        self.velocity =0

        self.angle = 2*pi
        self.dtAngle =0

        self.color = color
        pass

    def setForce(self,force,v):
        self.force = force
        self.acceleration = force/self.mass
        self.velocity = v

 
    def makeBody(self,mx, my):
        self.mx = mx
        self.my = my

        if mx <0 and my < 0:
            self.angle = atan(my/mx) + pi
        elif mx < 0 and my > 0:
            self.angle = ((pi/2) + atan(my/mx))+(pi/2)
        elif mx > 0 and my <0:
            self.angle = (pi/2) + atan(my/mx) + (3*pi/2)
        else:
            self.angle = atan(my/mx)
               
        
    def movebody(self,angle,r):
        self.mx =  self.mx*cos(angle)
        self.my =  self.my*sin(angle)

    def setCenterX(self,mx):
        self.mx = self.mx + (mx*self.velocity)
        
        

    def setCenterY(self,my):
        self.my = self.my + (my*self.velocity)
        
    

    def drawBody(self):
        PlanetCircle(self.mx, self.my,self.color,self.radius)
