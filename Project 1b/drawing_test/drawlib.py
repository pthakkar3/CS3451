# Drawing Routines, like OpenGL

# Pranshav Thakkar

from matlib import *

global vertexList, orthoOrPersp, gLeft, gRight, gBottom, gTop, gFov
vertexList, orthoOrPersp, gLeft, gRight, gBottom, gTop, gFov = [], "", 0.0, 0.0, 0.0, 0.0, 0.0

def gtOrtho(left, right, bottom, top, near, far):
    #Update global variables for orthoOrPerspective and left, right, bottom, top
    global orthoOrPersp, gLeft, gRight, gBottom, gTop
    orthoOrPersp, gLeft, gRight, gBottom, gTop = "ortho", left, right, bottom, top

def gtPerspective(fov, near, far):
    #Update global variables for orthoOrPerspective and fov
    global orthoOrPersp, gFov
    orthoOrPersp, gFov = "persp", fov

def gtBeginShape():
    #clear global list of vertices
    global vertexList
    del vertexList[:]

def gtEndShape():
    #global list of vertices present
    #1. start loop through list of vertices, increment i by 2. take two vertices at a time, i and i+1
    #2. apply ctm to i and i+1
    #3. apply the projection to i and i+1 (based on whether projection is ortho or perspective)
    #4. draw line with i and i+1
    
    global vertexList, orthoOrPersp, gLeft, gRight, gBottom, gTop, gFov
    
    if (len(vertexList) % 2 == 0):
        for i in range(0, len(vertexList) - 1, 2):
            ctm = gtGetMatrix()
            p1 = multMatrixWithVector(ctm, vertexList[i])
            p2 = multMatrixWithVector(ctm, vertexList[i + 1])
            if (orthoOrPersp == "ortho"):
                xp1 = (800/(gRight - gLeft)) * (p1[0] - gLeft)
                yp1 = (800/(gTop - gBottom)) * (p1[1] - gBottom)
                
                xp2 = (800/(gRight - gLeft)) * (p2[0] - gLeft)
                yp2 = (800/(gTop - gBottom)) * (p2[1] - gBottom)
                
                yflip1 = 800 - yp1
                yflip2 = 800 - yp2
                
                line(xp1, yflip1, xp2, yflip2)
            elif (orthoOrPersp == "persp"):
                k = tan(math.radians(gFov/2))
                
                xp1 = p1[0] / abs(p1[2])
                yp1 = p1[1] / abs(p1[2])
                
                xdp1 = (xp1 + k) * (800/(2*k))
                ydp1 = (yp1 + k) * (800/(2*k))
                
                xp2 = p2[0] / abs(p2[2])
                yp2 = p2[1] / abs(p2[2])
                
                xdp2 = (xp2 + k) * (800/(2*k))
                ydp2 = (yp2 + k) * (800/(2*k))
                
                yflip1 = 800 - ydp1
                yflip2 = 800 - ydp2
                
                line(xdp1, yflip1, xdp2, yflip2)

def gtVertex(x, y, z):
    #add vertex to global list of vertices
    vtx = []
    vtx.append(x)
    vtx.append(y)
    vtx.append(z)
    vtx.append(1)
    global vertexList
    vertexList.append(vtx)
    
def multMatrixWithVector(ctm, vector):
    vertexToReturn = []
    vertexToReturn.append((ctm[0][0] * vector[0]) + (ctm[0][1] * vector[1]) + (ctm[0][2] * vector[2]) + (ctm[0][3] * vector[3]))
    vertexToReturn.append((ctm[1][0] * vector[0]) + (ctm[1][1] * vector[1]) + (ctm[1][2] * vector[2]) + (ctm[1][3] * vector[3]))
    vertexToReturn.append((ctm[2][0] * vector[0]) + (ctm[2][1] * vector[1]) + (ctm[2][2] * vector[2]) + (ctm[2][3] * vector[3]))
    vertexToReturn.append((ctm[3][0] * vector[0]) + (ctm[3][1] * vector[1]) + (ctm[3][2] * vector[2]) + (ctm[3][3] * vector[3])) 
    return vertexToReturn