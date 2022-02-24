# why not working????????
# 으ㅏ아아아ㅏ아ㅏ아아ㅏ아아ㅏ아아ㅏ아아 실패 Opengl

__author__ = 'yoonhero'

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OopenGL.GLU import *
import numpy

vertices = ((1,-1,-1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))

edges = ((0, 1), (0, 3), (0, 4), (2,1), (2,3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))


def drawCube(): 
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertext3fv(vertices[vertex])
	glEnd()
 
def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -7)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT():
				pygame.quit()
				quit()

		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		drawCube()
		pygame.display.flip()
		pygame.time.wait(10)
 
if __name__ == "__main__":
    main()
