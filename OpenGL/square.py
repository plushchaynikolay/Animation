from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 600

SQUARE_SIZE = 50

x1 = int(WINDOW_SIZE_X / 2 - SQUARE_SIZE)
x2 = int(WINDOW_SIZE_X / 2 + SQUARE_SIZE)
y1 = int(WINDOW_SIZE_Y / 2 - SQUARE_SIZE)
y2 = int(WINDOW_SIZE_Y / 2 + SQUARE_SIZE)

# Увеличить по оси y в 3 раза
# y2 = int(WINDOW_SIZE_Y / 2 + 3 * SQUARE_SIZE)


class Square:
    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2i(x1, y2)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2i(x1, y1)
        glColor3f(1.0, 0.0, 1.0)
        glVertex2i(x2, y1)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2i(x2, y2)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.draw()
        glutSwapBuffers()

    def reshape(self, w, h):
        gluOrtho2D(0, w, 0, h)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
    glutCreateWindow("Square")
    square = Square()
    # The callback for display function
    glutDisplayFunc(square.display)
    # The callback for reshape function
    glutReshapeFunc(square.reshape)
    glutMainLoop()


if __name__ == '__main__':
    main()
