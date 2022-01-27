from shapes import*
G = 6.674 * (10 ** -11) #Cavendish's Big G

class CelestialBody:
    def __init__(self,mass,color,radius, iniVelocity, iniAngle):
        self.mx=0
        self.my =0
        self.acceleration = 0
        self.mass = mass
        self.radius = radius
        self.force = 0

        self.velo = 0

        self.iniVelocity = iniVelocity
        
        self.iniAngle = iniAngle
      
        self.graVelocity=0
        #self.orbitVelocity =0
        self.angle = 2*pi
        self.dtAngle =0

        self.color = color
        pass

    def setForce(self,force,r,velo):
        self.force = force
        self.acceleration = force/self.mass
        self.graVelocity = (r*self.acceleration) **.5
        self.velo = velo
      
 
    def makeBody(self,mx, my):
        self.mx = mx
        self.my = my

        if mx ==0:
            if my>0:
                self.angle = pi/2
            else:
                self.angle = 3*pi/2
        else:
            if mx <0 and my < 0:
                self.angle = atan(my/mx) + pi
            elif mx < 0 and my > 0:
                self.angle = ((pi/2) + atan(my/mx))+(pi/2)
            elif mx > 0 and my <0:
                self.angle = (pi/2) + atan(my/mx) + (3*pi/2)
            else:
                self.angle = atan(my/mx)
               
        
    def movebody(self,angle,r):
        if r==0:
            return


        x = self.graVelocity*cos(angle) + self.iniVelocity*cos(self.iniAngle)
        y = self.graVelocity*sin(angle) + self.iniVelocity*sin(self.iniAngle)
        v = (x*x + y*y)**.5

        if x == 0 and y == 0:
            theta =2*pi

        elif x == 0:
            if y>0:
                theta = pi/2
            else:
                theta= 3*pi/2

        else:
            if x <0 and y < 0:
                theta = atan(y/x) + pi
            elif x < 0 and y > 0:   
                                    theta= ((pi/2) + atan(y/x))+(pi/2)
            elif x > 0 and y <0:
                theta = (pi/2) + atan(y/x) + (3*pi/2)
            else:
                theta = atan(y/x)
        
        if self.dtAngle == angle:
            self.mx += (v)*cos(theta) 
            self.my += (v)*sin(theta) 
            return

        self.dtAngle = angle
        self.iniAngle = theta
        self.mx += (v)*cos(theta) 
        self.my += (v)*sin(theta) 
            
        
        
        
    def drawBody(self):
        PlanetCircle(self.mx, self.my,self.color,self.radius)


def findRadiuSlope(body1, body2): #finds the radius and the slope
    
    x = (body1.mx - body2.mx) 
    y = (body1.my - body2.my)
    r = (x*x + y*y) ** .5
    
    if r < 7:
        r = 0
    

    if x == 0 and y == 0:
        Angle =2*pi

    elif x == 0:
        if y>0:
            Angle = pi/2
        else:
            Angle= 3*pi/2
    
    else:
        if x <0 and y < 0:
            Angle = atan(y/x) + pi
        elif x < 0 and y > 0:
            Angle= ((pi/2) + atan(y/x))+(pi/2)
        elif x > 0 and y <0:
            Angle = (pi/2) + atan(y/x) + (3*pi/2)
        else:
            Angle = atan(y/x)
    
    
    return r,Angle

def findForce(body1, body2, r):

    if r == 0:
        force =0
        v1 =0
        v2=0
    else:
        force = G*body1.mass*body2.mass/(r*r)
        v1 = (G*body2.mass/r)**.5
        v2 = (G*body1.mass/r)**.5

    body1.setForce(force,r,v1)
    body2.setForce(force,r,v2)
    
    
def twoBodies(body1, body2):

    r, angle= findRadiuSlope(body1,body2)
    findForce(body1,body2,r)

    body2.movebody(angle,r)
    body1.movebody(angle+pi,r)
    
    pass

