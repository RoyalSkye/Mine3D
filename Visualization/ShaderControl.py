from OpenGL.GL import *
import ctypes

class ShaderControl(object):
    def __init__(self):
        self.Program=GLuint
        self.Shaders=[]

    def LoadShader(self,path,type):
        #读取着色器源码
        with open(path,'r') as f:
            shadercode = f.read()
        #创建着色器对象
        shader = glCreateShader(type)
        #把源码附加到着色器对象
        glShaderSource(shader,shadercode)
        glCompileShader(shader)

        # success = GLuint
        # glGetShaderiv(shader,GL_COMPILE_STATUS,ctypes.byref(success))
        # if not success:
        #     inforlog=''
        #     glGetShaderInfoLog(shader,512,None,inforlog)
        #     print('ERROR SHADER: '+inforlog)

        self.Shaders.append(shader)



    def LinkProgram(self):
        self.Program = glCreateProgram()
        for cshader in self.Shaders:
            glAttachShader(self.Program,cshader)

        glLinkProgram(self.Program)

        # success = GLint
        # glGetProgramiv(self.Program,GL_LINK_STATUS,success)
        # if not success:
        #     inforlog=''
        #     glGetProgramInfoLog(self.Program,512,None,inforlog)
        #     print('ERROR PROGRAM: '+inforlog)
        #     return -1

        # for cshader in self.Shaders:
        #     glDeleteShader(cshader)

        self.Shaders=[]

    def UseProgram(self):
        glUseProgram(self.Program)

    def GetProgram(self):
        return self.Program

