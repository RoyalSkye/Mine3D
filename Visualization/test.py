# # -*- coding:utf-8 -*-
# # Author:WYC
# from OpenGL.GL import *
#
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# def drawFunc():
# #清楚之前画面
#     glClear(GL_COLOR_BUFFER_BIT)
#     glRotatef(0.1, 0,5,0)
# #(角度,x,y,z)
#     glutWireTeapot(0.5)
# #刷新显示
#     glFlush()
# #使用glut初始化OpenGL
# glutInit()
# #显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
# glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# #窗口位置及大小-生成
# glutInitWindowPosition(0,0)
# glutInitWindowSize(400,400)
# glutCreateWindow(b"first")
# #调用函数绘制图像
# glutDisplayFunc(drawFunc)
# glutIdleFunc(drawFunc)
# #主循环
# glutMainLoop()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import OpenGL.GL as gl
import Visualization.glfw as glfw

WIN_WIDTH = 800
WIN_HEIGHT = 600

def framebuffer_size_callback(window, width, height):
    gl.glViewport(0, 0, width, height)

def processInput(window):
    if glfw.glfwGetKey(window, glfw.GLFW_KEY_ESCAPE) == glfw.GLFW_PRESS:
        glfw.glfwSetWindowShouldClose()

def main():
    glfw.glfwInit()

    glfw.glfwWindowHint(glfw.GLFW_CONTEXT_VERSION_MAJOR, 3)
    glfw.glfwWindowHint(glfw.GLFW_CONTEXT_VERSION_MINOR, 3)
    glfw.glfwWindowHint(glfw.GLFW_OPENGL_PROFILE, glfw.GLFW_OPENGL_CORE_PROFILE)

    window = glfw.glfwCreateWindow(WIN_WIDTH, WIN_HEIGHT, "学习OpenGL".encode(), 0, 0)
    if window == 0:
        print("failed to create window")
        glfw.glfwTerminate()

    glfw.glfwMakeContextCurrent(window)
    glfw.glfwSetFramebufferSizeCallback(window, framebuffer_size_callback)

    while not glfw.glfwWindowShouldClose(window):
        processInput(window)
        gl.glClearColor(0.2, 0.3, 0.3, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        glfw.glfwSwapBuffers(window)
        glfw.glfwPollEvents()

glfw.glfwTerminate()

if __name__ == "__main__":
    main()