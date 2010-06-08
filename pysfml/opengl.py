# -*- encoding: utf-8 -*-
from PySFML import sf

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *




def draw_with_opengl(window):
    """Draw tank"""
    
    glPushMatrix()
    
    # draw tank body
    glColor3f(1.0, 1.0, 1.0)
    
    glBegin(GL_QUADS)
    
    cosa = 1
    cosb = 0
    
    sina = 1 
    sinb = 0
    
    glTexCoord(1.0, 1.0)
    glVertex2f( 64 * cosa + 64 * cosb, 64 * sina + 64 * sinb )
    
    glTexCoord(1.0, 0.0)
    glVertex2f( 64 * cosa - 64 * cosb, 64 * sina - 64 * sinb )
    
    glTexCoord(0.0, 0.0)
    glVertex2f( - 64 * cosa - 64 * cosb, - 64 * sina - 64 * sinb )
    
    glTexCoord(0.0, 1.0)
    glVertex2f( - 64 * cosa + 64 * cosb, - 64 * sina + 64 * sinb )
    
    glEnd()
    
    glPopMatrix()
    




import sys

app = sf.RenderWindow()
app.Create(sf.VideoMode(640, 480), "Simple")

app.PreserveOpenGLStates(True)









# Enable Z-buffer read and write
glEnable(GL_DEPTH_TEST)
glDepthMask(GL_TRUE)
glClearDepth(1.)

# Setup a perspective projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()

# Bind our texture
glEnable(GL_TEXTURE_2D)
#glBindTexture(GL_TEXTURE_2D, Texture)
glColor4f(1., 1., 1., 1.)






# Es el contenedor del evento.
event = sf.Event()
input = app.GetInput()


sound = sf.Sound()
sound.SetBuffer(buffer)
sound.Play()

color = sf.Color(80, 80, 80)

playing_music = False
message = sf.String("Hi, this show some OpenGL")






while True:
    app.Clear(color)
    app.Draw(message)
    draw_with_opengl(app)







    # Retorna true si existe un evento para atender
    while app.GetEvent(event):

        x = input.GetMouseX()
        y = input.GetMouseY()


        if event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Escape:
                app.Close()
                sys.exit(0)


    app.Display()
