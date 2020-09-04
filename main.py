# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin

xrot = 0.0
yrot = 0.0
rot = 0.0


def init():
    glShadeModel(GL_SMOOTH)  # разрешает плавное цветовое сглаживание
    glClearColor(0.0, 0.0, 0.0, 0.0)  # очистка экрана в черный цвет
    glClearDepth(1.0)  # разрешить очистку буфера глубины
    glEnable(GL_BLEND)  # контролирует наложение RGBA – величин
    glEnable(GL_DEPTH_TEST)  # разрешить тест глубины
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)  # Улучшение в вычислении перспективы


def reshape(width, height):
    if height == 0:  # предотвращение деления на 0
        height += 1
    glViewport(0, 0, width, height)  # задает область вывода, начиная с левого нижнего угла
    glMatrixMode(GL_PROJECTION)  # выбераем матрицу проекций перспективного вида
    glLoadIdentity()  # сбрасывает матрицу обратно в ее состояние по умолчанию
    gluPerspective(45.0, width / height, 0.1, 100.0)  # задает усеченный конус видимости в левосторонней системе коорд.
    glMatrixMode(GL_MODELVIEW)  # выбераем матрицу проекций моедель вида
    glLoadIdentity()  # сбрасывает матрицу обратно в ее состояние по умолчанию


def dodecahedron():
    radius = 1
    arr_vertex = []
    angle_increment = 360 / 5
    angle_increment *= pi / 180.0
    angle = 0.0
    for i in range(5):
        arr_vertex.append([radius * cos(angle), radius * sin(angle)])
        angle += angle_increment
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glTranslatef(0, -1.16, -0.72)
    glRotatef(-116, 1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(117, 0.0, 1.0, 0.0)
    glRotatef(16, 1.0, 0.0, 0.0)
    glTranslatef(-1.14, -0.16, 0.72)
    glRotatef(26, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(118, 0.0, 1.0, 0.0)
    glRotatef(-16, 1.0, 0.0, 0.0)
    glTranslatef(1.16, -0.16, -0.72)
    glRotatef(-26, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(118, 0.0, 1.0, 0.0)
    glRotatef(16, 1.0, 0.0, 0.0)
    glTranslatef(-1.16, -0.17, 0.71)
    glRotatef(26.5, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(117.7, 0.0, 1.0, 0.0)
    glRotatef(-16, 1.0, 0.0, 0.0)
    glTranslatef(1.15, -0.18, -0.71)
    glRotatef(-26.5, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-122, 1.0, 0.0, 0.0)
    glRotatef(-31, 0.0, 1.0, 0.0)
    glTranslatef(-0.38, -1.11, 0.71)
    glRotatef(18, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-150, 1.0, 0.0, 0.0)
    glRotatef(60, 0.0, 1.0, 0.0)
    glTranslatef(-0.94, 0.67, -0.72)
    glRotatef(-17, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-121, 1.0, 0.0, 0.0)
    glRotatef(-33, 0.0, 1.0, 0.0)
    glTranslatef(-0.37, -1.09, 0.72)
    glRotatef(17, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-117, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 1.17, -0.72)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-120, 1.0, 0.0, 0.0)
    glRotatef(31, 0.0, 1.0, 0.0)
    glTranslatef(0.33, -1.106, 0.72)
    glRotatef(-19.5, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()
    glColor4f(1.0, 0.0, 0.0, 0.5)
    glRotatef(-130, 0.0, 1.0, 0.0)
    glRotatef(46.8, 1.0, 0.0, 0.0)
    glTranslatef(-1.0, 0.6, -0.72)
    glRotatef(-13.0, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    for vertex in arr_vertex:
        glVertex3f(vertex[1], vertex[0], 0)
    glEnd()


def torus():
    numc = 32
    numt = 32
    twopi = 2 * pi
    i = 0
    while i < numc:
        glBegin(GL_QUAD_STRIP)
        j = 0
        while j <= numt:
            k = 1
            while k >= 0:
                s = (i + k) % numc + 0.5
                t = j % numt

                x = (1 + 0.1 * cos(s * twopi / numc)) * cos(t * twopi / numt)
                y = (1 + 0.1 * cos(s * twopi / numc)) * sin(t * twopi / numt)
                z = 0.1 * sin(s * twopi / numc)

                glVertex3d(1 * x, 1 * y, 1 * z)
                k -= 1
            j += 1
        glEnd()
        i += 1


def display():
    global xrot
    global yrot
    global rot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # очистка экрана и буфера глубины
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glRotatef(yrot, 0.0, 0.0, -1.0)

    glTranslatef(0.0, 4, -15.0)
    glRotatef(xrot, -1.0, .0, 0.0)
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor4f(1.0, 1.0, 0.0, 1.0)
    cylinder = gluNewQuadric()
    disc = gluNewQuadric()
    gluQuadricDrawStyle(cylinder, GLU_FILL)
    gluCylinder(cylinder, 2, 2, 7, 32, 32)
    glColor4f(1.0, 0.0, 1.0, 1.0)
    gluQuadricDrawStyle(disc, GLU_FILL)
    gluDisk(disc, 0, 2, 32, 32)
    glTranslatef(0.0, 0.0, 7)
    gluQuadricDrawStyle(disc, GLU_FILL)
    gluDisk(disc, 0, 2, 32, 32)

    glRotatef(90, 0.0, 1.0, 0.0)
    glRotatef(rot, 1.0, 0.0, 0.0)
    glTranslatef(3.0, 0.0, -5)
    glColor(0.0, 0.0, 1.0)
    torus()
    glTranslatef(0.0, 0.0, 1.3)
    glEnable(GL_BLEND)
    glDepthMask(GL_FALSE)
    glBlendFunc(GL_ONE, GL_SRC_ALPHA)
    dodecahedron()
    glDepthMask(GL_TRUE)
    glDisable(GL_BLEND)
    rot += 1
    if rot >= 360:
        rot = 0.0
    glutSwapBuffers()
    glutPostRedisplay()


def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 2.0             # Увеличиваем угол вращения по оси Y
    glutPostRedisplay()         # Вызываем процедуру перерисовки


# Инициализация библиотеки Glut
glutInit()
# Указывает режим отображения для окна
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
# Задает размер окна
glutInitWindowSize(800, 600)
# Задает расположение окна относительно верхнего левого угла экрана
glutInitWindowPosition(100, 100)
# Открывает окно с предварительно установленными характеристиками
glutCreateWindow('window')
# Инициализация базовых параметров
init()
# После того, как окно создано, но до входа в главный цикл программы, нужно
# зарегистрировать функции обратного вызова, используя следующие функции GLUT:
# 1. Позволяет указать функцию (аргументом func), которая будет вызываться каждый раз,
#    когда содержимое окна требует перерисовки.
glutDisplayFunc(display)
# 2. Позволяет указать функцию, которая вызывается каждый раз при изменении размера
#    окна или его позиции на экране.
glutReshapeFunc(reshape)
# 3. Задает функцию func, которая вызывается, когда нажимается клавиша, имеющая
#    ASCII-код
# glutKeyboardFunc()
# 4. Указывает функцию, которая вызывается при нажатии или отпускании кнопки мыши.
# glutMouseFunc(mouse)
# 5. Указывает функцию, которая будет вызываться при движении мыши внутри окна в то
#    время, как на ней нажата одна или несколько клавиш.
# glutMotionFunc()
# 6. Помечает, что текущее окно требует перерисовки.
# glutPostRedisplay()
# 7. Задает функцию func, которая вызывается, когда нажимается спец клавиша
glutSpecialFunc(specialkeys)
# Главный цикл программы
glutMainLoop()