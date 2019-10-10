import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

window = 0 

def draw2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(0.0,1.0,0.0)
    drawline()
    glutSwapBuffers()

def drawline():
    glBegin(GL_POLYGON)
    glVertex3f(0.0f,0.4f,0.0f)
    glVertex3f(1.0f,2.4f,0.2f)
    flVertex3f(2.0f,1.0f,2.2f)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(600,800)
glutInitWindosPosition(0,0)
window = glutCreateWindow("grafica1_3d")
glutDisplayFunc(draw2d)
glutIdleFunc(draw2d)
glutMainLoop()