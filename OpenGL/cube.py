from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_X = 400
WINDOW_SIZE_Y = 400


class Cube:
    def __init__(self):
        self.rotate_x = 0.0
        self.rotate_y = 0.0
        self.rotate_speed = 5.0
        self.size = 2.0
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_FLAT)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glRotatef(self.rotate_y, 0.0, 1.0, 0.0)
        glRotatef(self.rotate_x, 1.0, 0.0, 0.0)

        # Внутренний куб
        glColor3f(0.0, 1.0, 1.0)
        glutSolidCube(self.size)

        # Границы куба
        glColor3f(1.0, 0.0, 0.0)
        glutWireCube(self.size)
        glFlush()

    def reshape(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glViewport(0, 0, GLsizei(w), GLsizei(h))
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def keyboard(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.rotate_y += self.rotate_speed
        if key == GLUT_KEY_LEFT:
            self.rotate_y -= self.rotate_speed
        if key == GLUT_KEY_UP:
            self.rotate_x += self.rotate_speed
        if key == GLUT_KEY_DOWN:
            self.rotate_x -= self.rotate_speed
        glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE_X, WINDOW_SIZE_Y)
    glutCreateWindow("Cube")
    cube = Cube()
    glutDisplayFunc(cube.display)
    glutReshapeFunc(cube.reshape)
    glutSpecialFunc(cube.keyboard)
    glutMainLoop()


if __name__ == '__main__':
    main()
