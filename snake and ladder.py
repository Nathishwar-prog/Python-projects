import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the vertices of the board
vertices = [
    (1, 1, 0), (1, -1, 0), (-1, -1, 0), (-1, 1, 0),
    (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)
]

# Define the edges of the board
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Define the colors of the cells
colors = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), 
    (1, 0, 1), (0, 1, 1), (1, 0.5, 0), (0.5, 0, 1)
]

# Function to draw the board
def draw_board():
    glBegin(GL_QUADS)
    for i, color in enumerate(colors):
        glColor3fv(color)
        for j in edges:
            glVertex3fv(vertices[j[0]])
            glVertex3fv(vertices[j[1]])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialize Pygame and OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_board()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
