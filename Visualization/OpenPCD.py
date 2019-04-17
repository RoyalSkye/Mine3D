from Visualization.glfw import *
from OpenGL.GL import *
from Visualization.ShaderControl import ShaderControl
import sys
import numpy as np
from Visualization.MeshTool import ModelObjS
import Visualization.MeshTool as MeshTool
import time
#global
shadercontrol = ShaderControl()
VAO = GLuint  # 存储读取数据的方法？
VBO = GLuint
EBO = GLuint
texture = GLuint
#移动
MoveControl = MeshTool.ObjectMove()
rotate = [0,0,0]
tranlate = [0,0,0]
scale = 1



#屏幕大小
size_x=800
size_y=600
#鼠标控制
mouseDown='false'
sensitiveley = 0.1
LastMouseX=0
LastMouseY=0
RotateChangeMatrix = [0,0]
MouseScale = 1
mouseDown_m='false'
LastMouseX_m=0
LastMouseY_m=0
moveSpeed=5
TranslateChangeMatrix=[0,0]


#---------------------------------------------------------------------------------------------------------------
shaderpath_vs = '/Users/skye/PycharmProjects/20190302/Visualization/POINT.vs'
shaderpath_frag = '/Users/skye/PycharmProjects/20190302/Visualization/POINT.frag'
path='/Users/skye/PycharmProjects/20190302/Visualization/NewnewTUZIS.obj'
#model
#rabbit_gra
#NewnewTUZIS



def InitMap():
    global shadercontrol,VAO,VBO,EBO,texture,MoveControl
    Obj = ModelObjS()
    Obj.Load(path)
    indices = np.array(Obj.faces, dtype=np.uint32)
    ver_nors = np.array(Obj.GetVerticles_Normals(), dtype=np.float32)
    ver_nors=ver_nors/20
    print('aa',len(ver_nors))
    # vertices = np.array([		-0.5, -0.5, -0.5,  0.0,  0.0, -1.0,
	# 	 0.5, -0.5, -0.5,  0.0,  0.0, -1.0,
	# 	 0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
	# 	 0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
	# 	-0.5,  0.5, -0.5,  0.0,  0.0, -1.0,
	# 	-0.5, -0.5, -0.5,  0.0,  0.0, -1.0,
    #
	# 	-0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
	# 	 0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
	# 	 0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
	# 	 0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
	# 	-0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
	# 	-0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
    #
	# 	-0.5,  0.5,  0.5, -1.0,  0.0,  0.0,
	# 	-0.5,  0.5, -0.5, -1.0,  0.0,  0.0,
	# 	-0.5, -0.5, -0.5, -1.0,  0.0,  0.0,
	# 	-0.5, -0.5, -0.5, -1.0,  0.0,  0.0,
	# 	-0.5, -0.5,  0.5, -1.0,  0.0,  0.0,
	# 	-0.5,  0.5,  0.5, -1.0,  0.0,  0.0,
    #
	# 	 0.5,  0.5,  0.5,  1.0,  0.0,  0.0,
	# 	 0.5,  0.5, -0.5,  1.0,  0.0,  0.0,
	# 	 0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
	# 	 0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
	# 	 0.5, -0.5,  0.5,  1.0,  0.0,  0.0,
	# 	 0.5,  0.5,  0.5,  1.0,  0.0,  0.0,
    #
	# 	-0.5, -0.5, -0.5,  0.0, -1.0,  0.0,
	# 	 0.5, -0.5, -0.5,  0.0, -1.0,  0.0,
	# 	 0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
	# 	 0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
	# 	-0.5, -0.5,  0.5,  0.0, -1.0,  0.0,
	# 	-0.5, -0.5, -0.5,  0.0, -1.0,  0.0,
    #
	# 	-0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
	# 	 0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
	# 	 0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
	# 	 0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
	# 	-0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
	# 	-0.5,  0.5, -0.5,  0.0,  1.0,  0.0], dtype=np.float32)
    # indices = np.array([0,1,3,
    #                     1,2,3], dtype=np.uint32)



    #缓冲对象的好处是我们可以一次性的发送一大批数据到显卡上，而不是每个顶点发送一次
    # print(bool(glGenVertexArrays))
    print("test0")
    VAO = glGenVertexArrays(1)
    print("test1")
    glBindVertexArray(VAO)
    VBO=glGenBuffers(1) #生成2个缓冲ID
    glBindBuffer(GL_ARRAY_BUFFER,VBO)
    glBufferData(GL_ARRAY_BUFFER,sys.getsizeof(ver_nors),ver_nors,GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sys.getsizeof(indices), indices, GL_STATIC_DRAW);

    #设置读取属性
    glVertexAttribPointer(0, 3, GL_FLOAT,GL_FALSE, 6 * sizeof(GLfloat), ctypes.c_void_p(0));
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (ctypes.c_void_p(3*sizeof(GLfloat))))
    glEnableVertexAttribArray(1)

    #解绑
    glBindVertexArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);

    #Shader相关
    shadercontrol.LoadShader(shaderpath_vs,GL_VERTEX_SHADER)
    shadercontrol.LoadShader(shaderpath_frag, GL_FRAGMENT_SHADER)
    shadercontrol.LinkProgram()

    #位移相关
    shadercontrol.UseProgram()
    trans = MoveControl.GetTransformMatrix(0,0,0)
    rotate = MoveControl.GetRotateMatrix(0,0,0,0)
    model = np.matmul(trans,rotate)
    transformLoc = glGetUniformLocation(shadercontrol.Program, "model")
    glUniformMatrix4fv(transformLoc, 1, GL_FALSE, model)

    view = MoveControl.GetTransformMatrix(0,0,-3)
    viewLoc = glGetUniformLocation(shadercontrol.Program, "view")
    glUniformMatrix4fv(viewLoc, 1, GL_FALSE, view)

    perspective = MoveControl.GetPerspective(0.785,1,0.1,100)
    perspectiveLoc = glGetUniformLocation(shadercontrol.Program, "projection")
    print(perspective)
    glUniformMatrix4fv(perspectiveLoc, 1, GL_FALSE, perspective)


    #光照相关
    objectColorLoc = glGetUniformLocation(shadercontrol.Program, "objectColor")
    glUniform3f(objectColorLoc,1.0,1.0,1.0)
    lightColorLoc = glGetUniformLocation(shadercontrol.Program, "lightColor")
    glUniform3f(lightColorLoc,1.0,1.0,1.0)

    lightPosLoc = glGetUniformLocation(shadercontrol.Program, "lightPos")
    glUniform3f(lightPosLoc,0.0, -2.0, -1.0)


def key_callback(window,key,scancode,action,mode):
    global rotate
    if key== GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GL_TRUE)
    if key==GLFW_KEY_A and action == GLFW_PRESS:
        rotate=rotate-0.1;



def mouseButton_callback(window,button,action,mods):
    global mouseDown,RotateChangeMatrix,mouseDown_m,TranslateChangeMatrix
    if action==GLFW_PRESS:


        if button==GLFW_MOUSE_BUTTON_LEFT:
            mouseDown = 'first'
            buttons=glfwGetMouseButton()
        if button==GLFW_MOUSE_BUTTON_RIGHT:
            mouseDown_m='first'
    if action == GLFW_RELEASE:
        mouseDown = 'false'
        mouseDown_m='false'




def mouseMove_callback(window,xpos,ypos):
    global LastMouseX,LastMouseY,mouseDown,RotateChangeMatrix,size_x,size_y,LastMouseX_m,LastMouseY_m,mouseDown_m,moveSpeed,TranslateChangeMatrix
    if mouseDown=='first':
        LastMouseX = xpos
        LastMouseY = ypos
        mouseDown='true'

    if mouseDown_m=='first':
        LastMouseX_m = xpos
        LastMouseY_m = ypos
        mouseDown_m='true'


    if mouseDown=='true':
        currentx = -(xpos - LastMouseX)/size_x * 180
        LastMouseX=xpos
        currenty = -(ypos - LastMouseY)/size_y *180
        LastMouseY=ypos
        currentx=  currentx*sensitiveley
        currenty=  currenty*sensitiveley
        RotateChangeMatrix[0] =RotateChangeMatrix[0]+ currentx
        RotateChangeMatrix[1] =RotateChangeMatrix[1]+ currenty

    if mouseDown_m=='true':
        currentx_m = (xpos - LastMouseX_m)/size_x
        LastMouseX_m = xpos
        print(currentx_m)
        currenty_m = -(ypos - LastMouseY_m)/size_y
        LastMouseY_m = ypos
        currentx_m=  currentx_m*moveSpeed
        currenty_m=  currenty_m*moveSpeed
        TranslateChangeMatrix[0] = TranslateChangeMatrix[0]+currentx_m
        TranslateChangeMatrix[1] = TranslateChangeMatrix[1]+currenty_m





aspect=10.0
def scroll_callback(window,xoffset,yoffset):
    global aspect,MouseScale
    print(aspect)
    if aspect >= 1.0 and aspect <= 45.0:
        aspect -= yoffset;
        if aspect <= 0.10:
            aspect = 0.10
        if aspect >= 45.0:
            aspect = 45.0
    MouseScale = aspect/10


if __name__=='__main__':
    glfwInit() #初始化
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3)
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
    #指定创建的上下文必须兼容的客户端API版本。这些提示的确切行为取决于请求的客户端API。
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)
    #窗口是否可调整大小
    #glfwWindowHint(GLFW_RESIZABLE, GL_FALSE)
    window = glfwCreateWindow(800,600,'AstarVisualization')
    if window==None:
        print('GLFW窗口启动失败')
        glfwTerminate()

    glfwMakeContextCurrent(window)
    # glViewport(0, 0, size_x, size_y)
    # #渲染窗口尺寸的大小  （左下角x，左下角y，宽，高）
    # glfwSetKeyCallback(window, key_callback)
    # glfwSetMouseButtonCallback(window, mouseButton_callback)
    # glfwSetCursorPosCallback(window,mouseMove_callback)
    # glfwSetScrollCallback(window, scroll_callback)
    InitMap()

    ltime = time.time()

    glEnable(GL_DEPTH_TEST)# 开启深度缓冲
    while not glfwWindowShouldClose(window):
        glfwPollEvents()#检查有没有触发什么事件
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


        shadercontrol.UseProgram()
        model_fr = MoveControl.GetRotateMatrix(RotateChangeMatrix[0], 0, 1, 0)
        model_ud = MoveControl.GetRotateMatrix(RotateChangeMatrix[1], 1, 0, 0)
        model = np.matmul(model_fr,model_ud)
        model_scale = MoveControl.GetScaleMatrix(MouseScale)
        model = np.matmul(model,model_scale)
        model_trals = MoveControl.GetTransformMatrix(TranslateChangeMatrix[0],TranslateChangeMatrix[1],0)
        model =  np.matmul(model,model_trals)
        transformLoc = glGetUniformLocation(shadercontrol.Program, "model")
        glUniformMatrix4fv(transformLoc, 1, GL_FALSE, model)


        glBindVertexArray(VAO)
        #glDrawArrays(GL_TRIANGLES, 0, 36);
        glDrawElements(GL_TRIANGLES, 400000, GL_UNSIGNED_INT, None);
        #glDrawArrays(GL_POINTS, 0, 44556)
        glBindVertexArray(0)



        glfwSwapBuffers(window)

    glfwTerminate(); #释放GLFW分配的内存





