from OpenGL.GL import*
from OpenGL.GLU import*
from math import (pi, sin, cos,tan,acos,asin,atan)

from pygame.version import ver

def Triangle():

    vertices = (
        (-1,-1),
        (1,-1),
        (0,1),
    )

    indices = (
        (0,1,2),
    )

    glBegin(GL_POLYGON)
    glColor3f(.5,.5,.5)
    for index in indices:
        for vertex in index:
            glVertex2dv(vertices[vertex])
    glFlush()
    #glEnd()



def Square():

    vertices = (
    (-1,-1),
    (1,-1),
    (1,1),
    (-1,1)
    )

    indices = (
    (0,1,3),
    (1,2,3)
    
    )
  
    glBegin(GL_POLYGON)
    glColor3f(.5,.5,.5)
    for vertex in range(0, len(vertices)):
        glVertex2fv(vertices[vertex])
    #glFlush()
    glEnd()



def mySquare(xCenter, yCenter):

    LeftUpper = ((xCenter-145)/145,(yCenter+145)/145)
    LeftLower = ((xCenter-145)/145,(yCenter-145)/145)

    RightUpper = ((xCenter+145)/145,(yCenter+145)/145)
    RightLower = ((xCenter+145)/145,(yCenter-145)/145)

    vertices = (
    LeftLower,
    RightLower,
    RightUpper,
    LeftUpper
    )

    #
    
  
    glBegin(GL_POLYGON)
    glColor3f(.5,.5,.5)
    for vertex in range(0, len(vertices)):
        glVertex2fv(vertices[vertex])
    #glFlush()
    glEnd()


def FollowCircle(mx,my):
    
    circle_points = 10000

    glBegin(GL_TRIANGLE_FAN) 
    for i in range(0,circle_points+1):    
        angle = 2*pi*i/circle_points; 
        glVertex2f(cos(angle)+(mx/145), sin(angle)+(my/145)); 
    glEnd()


def PlanetCircle(mx, my,color,r):
    
    circle_points = 100
    #r = .35
    glBegin(GL_TRIANGLE_FAN) 
    glColor3fv(color)
    for i in range(0,circle_points+1):    
        angle = 2*pi*i/circle_points; 
        glVertex2f( r*cos(angle)+(mx/145), r*sin(angle)+(my/145)); 
    glEnd()



def myCircle():
    
    vertices = [(0,0)]
    edges = []
    angle =0
    while angle < 2*pi:
        vertices.append( (cos(angle),sin(angle)) )
        angle += (2*pi/360)

    for vertex in range(1, len(vertices)):
        edges.append( (0,vertex) )   


    #print(f"Here are the vertices:{vertices}\n")
    #print(f"Here are the edges:{edges}\n")
    
    glBegin(GL_TRIANGLES) 
    for edge in edges:
        for vertex in edge:
            glVertex2fv(vertices[vertex])
    glEnd()
    

def cube():
    
    vertices = (

    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1, -1, 1),
    (1,1,1),
    (-1, -1, 1),
    (-1,1,1)

 )

    edges = (
    
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
 )
    glBegin(GL_TRIANGLE_FAN)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        
    glEnd()
