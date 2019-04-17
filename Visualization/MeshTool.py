import numpy as np
import OpenGL.GLU as gu
import sys
class ModelObj:
    def __init__(self):
        self.vertices=[]
        self.normals=[]
        self.faces=[]

    def Load(self,path):
        i=0
        for line in open(path, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                i=i+1
                temp = []
                for x in values[1:4]:
                    temp.append(float(x))
                self.vertices.append(temp)
            elif values[0] == 'vn':
                for x in values[1:4]:
                     self.normals.append(float(x))
            elif values[0] == 'f':
                face = []
                temp=[]
                for v in values[1:]:
                    w = v.split('//')
                    face.append(w[0])
                for x in face:
                     temp.append(int(x))
                self.faces.append(temp)

        print('ssssssssssssss ',i)


class ModelObjS:
    def __init__(self):
        self.vertices=[]
        self.normals=[]
        self.faces=[]
        self.ver_nors=[]

    def Load(self,path):
        i=0
        for line in open(path, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                i=i+1
                for x in values[1:4]:
                    self.vertices.append(float(x))
            elif values[0] == 'vn':
                for x in values[1:4]:
                     self.normals.append(float(x))
            elif values[0] == 'f':
                face = []
                for v in values[1:]:
                    w = v.split('//')
                    face.append(w[0])
                for x in face:
                    self.faces.append((int(x)-1))

        print(len(self.vertices),'ssssssssssssss ',i)

    def GetVerticles_Normals(self):
        i=0
        while True:
            self.ver_nors.append(self.vertices[i])
            self.ver_nors.append(self.vertices[i+1])
            self.ver_nors.append(self.vertices[i+2])
            self.ver_nors.append(self.normals[i])
            self.ver_nors.append(self.normals[i+1])
            self.ver_nors.append(self.normals[i+2])
            i=i+3
            if i>=len(self.vertices):
                break
        return self.ver_nors



class ObjectMove():
    def __init__(self):
        print("用于生成各种变换矩阵")


    def GetTransformMatrix(self,x,y,z):
        v = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]], dtype=np.float32)
        return v

    def GetScaleMatrix(self,scale):
        v = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, scale]], dtype=np.float32)
        return v

    def GetRotateMatrix(self,angle,x,y,z):
        v = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=np.float32)
        if x>0:
            v[1][1] = np.cos(angle)
            v[1][2] = -np.sin(angle)
            v[2][1] = np.sin(angle)
            v[2][2] = np.cos(angle)
        if y>0:
            v[0][0] = np.cos(angle)
            v[0][2] = np.sin(angle)
            v[2][0] = -np.sin(angle)
            v[2][2] = np.cos(angle)
        if z>0:
            v[0][0] = np.cos(angle)
            v[0][1] = -np.sin(angle)
            v[1][0] = np.sin(angle)
            v[1][1] = np.cos(angle)
        return v

    def GetPerspective(self,angle,aspect,near,far):
        v = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], dtype=np.float32)
        v[0][0] = 1/(np.tan(angle/2)*aspect)
        v[1][1] = np.cos(angle/2)/np.sin(angle/2)
        v[2][2] = -(far+near)/(far-near)
        v[2][3] = -1
        v[3][2] = -2*far*near/(far-near)
        return v

if __name__=='__main__':
    a = ObjectMove()
    b = a.GetRotateMatrix(30,0,0,1)
    c = a.GetPerspective(0.785,1,0.1,100)
    print(c)

    path = 'C:/study/FYZLearn/C++DLL/SurfaceTest/SurfaceTest/PCD/NewnewTUZIS.obj'
    Obj = ModelObjS()
    Obj.Load(path)


    for i in range(20):
        print(Obj.faces[i],Obj.vertices[Obj.faces[i]])

    print(len(Obj.faces))
