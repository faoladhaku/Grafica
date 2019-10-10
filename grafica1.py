import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

window = 0 

def traslacion(puntox,puntoy):
    a = input("movimiento en x")
    b = input("movimiento en y")
    traslada  = np.matrix([[1,0,a],[0,1,b],[0,0,1]])
    puntos = np.matrix([puntox],[puntoy],[1])
    return traslada.dot(puntos)

def rotacion(puntox,puntoy):
    angulo = input("angulo de rotacion")
    rotacion  = np.matrix([[np.cos(angulo),-np.sen(angulo),0],[np.sen(angulo),np.cos(angulo),0],[0,0,0]])
    puntos = np.matrix([puntox],[puntoy],[1])
    return rotacion.dot(puntos)

def escalaX(puntox,puntoy):
    escalar = input("escalacion en X")
    rotacion  = np.matrix([[1,0,0],[escalar,1,0],[0,0,1]])
    puntos = np.matrix([puntox],[puntoy],[1])
    return rotacion.dot(puntos)


def escalaY(puntox,puntoy):
    escalar = input("escalacion en Y")
    rotacion  = np.matrix([[1,escalar,0],[0,1,0],[0,0,1]])
    puntos = np.matrix([puntox],[puntoy],[1])
    return rotacion.dot(puntos)

def draw2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0,0.0,0.0)
    drawline()
    glutSwapBuffers()

def drawline():
    glBegin(GL_LINES)
    glVertex2f(0.0f,0.4f)
    glVertex2f(1.0f,2.4f)
    glEnd()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(600,800)
glutInitWindosPosition(0,0)
window = glutCreateWindow("grafica1_2d")
glutDisplayFunc(draw2d)
glutIdleFunc(draw2d)
glutMainLoop()