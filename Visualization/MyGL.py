from PyQt5.QtWidgets import QOpenGLWidget
from Visualization.glfw import *
from OpenGL.GL import *
from Visualization.ShaderControl import ShaderControl
import sys
import numpy as np
from Visualization.MeshTool import ModelObjS
import Visualization.MeshTool
import time
from PyQt5.QtCore import *

class OpenGLWidget(QOpenGLWidget):
    def __init__(self,parent=None):
        super(OpenGLWidget,self).__init__(parent)

        self.shadercontrol = ShaderControl()
        self.VAO = GLuint  # 存储读取数据的方法？
        self.VBO = GLuint
        self. EBO = GLuint
        self.texture = GLuint
        # 移动
        self.MoveControl = Visualization.MeshTool.ObjectMove()
        self.rotate = [0, 0, 0]
        self.tranlate = [0, 0, 0]
        self.scale = 1

        # 屏幕大小
        self.size_x = 800
        self.size_y = 600
        # 鼠标控制
        self.mouseDown = 'false'
        self.sensitiveley = 0.1
        self.LastMouseX = 0
        self.LastMouseY = 0
        self.RotateChangeMatrix = [0, 0]
        self.MouseScale = 1
        self.mouseDown_m = 'false'
        self.LastMouseX_m = 0
        self.LastMouseY_m = 0
        self. moveSpeed = 5
        self.TranslateChangeMatrix = [0, 0]
        self.shaderpath_vs = '/Users/skye/PycharmProjects/20190302/Visualization/POINT.vs'
        self.shaderpath_frag = '/Users/skye/PycharmProjects/20190302/Visualization/POINT.frag'
        self.path = '/Users/skye/PycharmProjects/20190302/Visualization/model.obj'
        self.aspect = 10.0

    def initializeGL(self):
        Obj = ModelObjS()
        Obj.Load(self.path)
        indices = np.array(Obj.faces, dtype=np.uint32)
        ver_nors = np.array(Obj.GetVerticles_Normals(), dtype=np.float32)
        ver_nors = ver_nors / 20

        # 缓冲对象的好处是我们可以一次性的发送一大批数据到显卡上，而不是每个顶点发送一次
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)
        self.VBO = glGenBuffers(1)  # 生成2个缓冲ID
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, sys.getsizeof(ver_nors), ver_nors, GL_STATIC_DRAW)

        self. EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sys.getsizeof(indices), indices, GL_STATIC_DRAW);

        # 设置读取属性
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), ctypes.c_void_p(0));
        glEnableVertexAttribArray(0);
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (ctypes.c_void_p(3 * sizeof(GLfloat))))
        glEnableVertexAttribArray(1)

        # 解绑
        glBindVertexArray(0);
        glBindBuffer(GL_ARRAY_BUFFER, 0);

        # Shader相关
        self.shadercontrol.LoadShader(self.shaderpath_vs, GL_VERTEX_SHADER)
        self.shadercontrol.LoadShader(self.shaderpath_frag, GL_FRAGMENT_SHADER)
        self.shadercontrol.LinkProgram()

        # 位移相关
        self.shadercontrol.UseProgram()
        trans = self.MoveControl.GetTransformMatrix(0, 0, 0)
        rotate = self.MoveControl.GetRotateMatrix(0, 0, 0, 0)
        model = np.matmul(trans, rotate)
        transformLoc = glGetUniformLocation(self.shadercontrol.Program, "model")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, model)

        view = self.MoveControl.GetTransformMatrix(0, 0, -3)
        viewLoc = glGetUniformLocation(self.shadercontrol.Program, "view")
        glUniformMatrix4fv(viewLoc, 1, GL_FALSE, view)

        perspective = self.MoveControl.GetPerspective(0.785, 1, 0.1, 100)
        perspectiveLoc = glGetUniformLocation(self.shadercontrol.Program, "projection")
        print(perspective)
        glUniformMatrix4fv(perspectiveLoc, 1, GL_FALSE, perspective)

        # 光照相关
        objectColorLoc = glGetUniformLocation(self.shadercontrol.Program, "objectColor")
        glUniform3f(objectColorLoc, 1.0, 1.0, 1.0)
        lightColorLoc = glGetUniformLocation(self.shadercontrol.Program, "lightColor")
        glUniform3f(lightColorLoc, 1.0, 1.0, 1.0)

        lightPosLoc = glGetUniformLocation(self.shadercontrol.Program, "lightPos")
        glUniform3f(lightPosLoc, 0.0, -2.0, -1.0)

        glfwInit();  # 初始化
        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
        # 指定创建的上下文必须兼容的客户端API版本。这些提示的确切行为取决于请求的客户端API。
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)
        # 窗口是否可调整大小
        glfwWindowHint(GLFW_RESIZABLE, GL_FALSE)
        # window = glfwCreateWindow(800, 600, 'AstarVisualization')
        # if window == None:
        #     print('GLFW窗口启动失败')
        #     glfwTerminate()

        #glfwMakeContextCurrent(window)
        glViewport(0, 0, self.size_x, self.size_y);
        # 渲染窗口尺寸的大小  （左下角x，左下角y，宽，高）
        #glfwSetKeyCallback(window, key_callback)
        #glfwSetMouseButtonCallback(self, self.mouseButton_callback)
        #glfwSetCursorPosCallback(window, mouseMove_callback)
        #glfwSetScrollCallback(window, scroll_callback);


        glEnable(GL_DEPTH_TEST)  # 开启深度缓冲

    def paintGL(self):
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        self.shadercontrol.UseProgram()
        model_fr = self.MoveControl.GetRotateMatrix(self.RotateChangeMatrix[0], 0, 1, 0)
        model_ud = self.MoveControl.GetRotateMatrix(self.RotateChangeMatrix[1], 1, 0, 0)
        model = np.matmul(model_fr,model_ud)
        model_scale = self.MoveControl.GetScaleMatrix(self.MouseScale)
        model = np.matmul(model,model_scale)
        model_trals = self.MoveControl.GetTransformMatrix(self.TranslateChangeMatrix[0],self.TranslateChangeMatrix[1],0)
        model =  np.matmul(model,model_trals)
        transformLoc = glGetUniformLocation(self.shadercontrol.Program, "model")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, model)

        glBindVertexArray(self.VAO)
        #glDrawArrays(GL_TRIANGLES, 0, 36);
        glDrawElements(GL_TRIANGLES, 400000, GL_UNSIGNED_INT, None);
        #glDrawArrays(GL_POINTS, 0, 44556)
        glBindVertexArray(0)


        #glfwSwapBuffers(window)

    # def key_callback(self,window, key, scancode, action, mode):
    #     if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
    #         glfwSetWindowShouldClose(window, GL_TRUE)
    #     if key == GLFW_KEY_A and action == GLFW_PRESS:
    #         self.rotate = self.rotate - 0.1;
    #
    #
    #
    #
    # def scroll_callback(self,window, xoffset, yoffset):
    #     print(self.aspect)
    #     if self.aspect >= 1.0 and self.aspect <= 45.0:
    #         self.aspect -= yoffset;
    #         if self.aspect <= 0.10:
    #             self.aspect = 0.10
    #         if self.aspect >= 45.0:
    #             self.aspect = 45.0
    #     self.MouseScale = self.aspect / 10

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("鼠标左键点击")
            self.mouseDown = 'first'
            self.buttons = glfwGetMouseButton()
        elif event.button() == Qt.RightButton:
            print("鼠标右键点击")
            self.mouseDown_m = 'first'
        elif event.button() == Qt.MidButton:
            print("鼠标中键点击")

    def mouseReleaseEvent(self, event):
        print('鼠标放开')
        self.mouseDown = 'false'
        self.mouseDown_m = 'false'

    def mouseMoveEvent(self, event):
        if self.mouseDown == 'first':
            self.LastMouseX = event.x()
            self.LastMouseY = event.y()
            self.mouseDown = 'true'

        if self.mouseDown_m == 'first':
            self.LastMouseX_m = event.x()
            self.LastMouseY_m = event.y()
            self.mouseDown_m = 'true'

        if self.mouseDown == 'true':
            currentx = -(event.x() - self.LastMouseX) / self.size_x * 180
            self.LastMouseX =event.x()
            currenty = -(event.y() - self.LastMouseY) / self.size_y * 180
            self.LastMouseY = event.y()
            currentx = currentx * self.sensitiveley
            currenty = currenty * self.sensitiveley
            self.RotateChangeMatrix[0] = self.RotateChangeMatrix[0] + currentx
            self.RotateChangeMatrix[1] = self.RotateChangeMatrix[1] + currenty

        if self.mouseDown_m == 'true':
            currentx_m = (event.x() - self.LastMouseX_m) / self.size_x
            self.LastMouseX_m = event.x()
            print(currentx_m)
            currenty_m = -(event.y() - self.LastMouseY_m) / self.size_y
            self.LastMouseY_m = event.y()
            currentx_m = currentx_m * self.moveSpeed
            currenty_m = currenty_m * self.moveSpeed
            self.TranslateChangeMatrix[0] = self.TranslateChangeMatrix[0] + currentx_m
            self.TranslateChangeMatrix[1] = self.TranslateChangeMatrix[1] + currenty_m
        self.update()
