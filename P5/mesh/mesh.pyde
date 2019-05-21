# Sample code for starting the mesh processing project
# Pranshav Thakkar

from polyhedra import Polyhedra
from vtx import Vtx

rotate_flag = False    # automatic rotation of model?
time = 0   # keep track of passing time, for automatic rotation
polyhedra = None
random_flag = False
shading_flag = False   # False = flat, True = smooth
vtxNormals = None

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()
    read_mesh ('tetra.ply')

# draw the current mesh
def draw():
    global time
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();


    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
    
    
  
    
    rotate (time, 1.0, 0.0, 0.0)
    
    

    
    # THIS IS WHERE YOU SHOULD DRAW THE MESH
    count = 0
    for v in polyhedra.vtable:
        if (count % 3 == 0):
            beginShape()
            if random_flag:
                clr = polyhedra.ctable[count/3]
                r = clr.x
                g = clr.y
                b = clr.z
            else:
                r = 200
                g = 200
                b = 200
        fill(r, g, b)
        if shading_flag:
            vtxNormal = vtxNormals[v]
            normal(vtxNormal.x, vtxNormal.y, vtxNormal.z)
        vertex(polyhedra.gtable[v].x, polyhedra.gtable[v].y, polyhedra.gtable[v].z)
        if (count % 3 == 2):
            endShape(CLOSE)
        count = count + 1

    
    
    # beginShape()
    # normal (0.0, 0.0, 1.0)
    # vertex (-1.0, -1.0, 0.0)
    # vertex ( 1.0, -1.0, 0.0)
    # vertex ( 1.0,  1.0, 0.0)
    # vertex (-1.0,  1.0, 0.0)
    # endShape(CLOSE)
    
    popMatrix() 
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        global shading_flag
        shading_flag = not shading_flag
    elif key == 'r':
        global random_flag
        random_flag = True
    elif key == 'w':
        global random_flag
        random_flag = False
    elif key == 'd':
        dual()
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):
    gTable = []
    vTable = []
    oTable = []
    cTable = []
    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        #print "vertex = ", x, y, z
        gTable.append(Vtx(x, y, z))
    
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        vTable.append(index1)
        vTable.append(index2)
        vTable.append(index3)
        r = random(0, 255)
        g = random(0, 255)
        b = random(0, 255)
        clr = PVector(r, g, b)
        cTable.append(clr)
        #print "face =", index1, index2, index3
        
    for i in range(len(vTable)):
        oTable.append(None)    
        
    for a in range(len(vTable)):
        for b in range(len(vTable)):
            if (a != b):
                if (gTable[vTable[next(a)]] == gTable[vTable[previous(b)]] and gTable[vTable[previous(a)]] == gTable[vTable[next(b)]]):
                    oTable[a] = b
                    oTable[b] = a
                
    global polyhedra
    polyhedra = Polyhedra(gTable, vTable, oTable, cTable)
    
    global vtxNormals
    vtxNormals = perVertexShading()
    
def dual():
    newGTable = []
    newVTable = []
    newOTable = []
    newCTable = []
    supersAndCents = []
    for i in range(0, len(polyhedra.vtable), 3):
        v1 = polyhedra.gtable[polyhedra.vtable[i]]
        v2 = polyhedra.gtable[polyhedra.vtable[i + 1]]
        v3 = polyhedra.gtable[polyhedra.vtable[i + 2]]
        centroid = calculateCentroid(v1, v2, v3)
        newGTable.append(centroid)
    
    for vtx in range(len(polyhedra.gtable)):
        centroidList = []
        firstCorner = polyhedra.vtable.index(vtx)
        nextCorner = next(firstCorner)
        prevCorner = previous(firstCorner)
        sVtx = polyhedra.gtable[polyhedra.vtable[firstCorner]]
        nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
        pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
        centroid = calculateCentroid(sVtx, nVtx, pVtx)
        centroidList.append(centroid)
        superCentroid = Vtx(0.0, 0.0, 0.0)
        superCentroid.x = superCentroid.x + centroidList[0].x
        superCentroid.y = superCentroid.y + centroidList[0].y
        superCentroid.z = superCentroid.z + centroidList[0].z
        swingCorner = swing(firstCorner)
        while (swingCorner != firstCorner):
            nextCorner = next(swingCorner)
            prevCorner = previous(swingCorner)
            sVtx = polyhedra.gtable[polyhedra.vtable[swingCorner]]
            nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
            pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
            swingCentroid = calculateCentroid(sVtx, nVtx, pVtx)
            centroidList.append(swingCentroid)
            superCentroid.x = superCentroid.x + swingCentroid.x
            superCentroid.y = superCentroid.y + swingCentroid.y
            superCentroid.z = superCentroid.z + swingCentroid.z
            swingCorner = swing(swingCorner)
        superCentroid.x = superCentroid.x / len(centroidList)         #now we actually calculate the centroid of centroids, by averaging the added values together
        superCentroid.y = superCentroid.y / len(centroidList)
        superCentroid.z = superCentroid.z / len(centroidList)
        
        newGTable.append(superCentroid)
        supersAndCents.append((superCentroid, centroidList))        
        
    preVTable = []
    
    for pair in supersAndCents:
        super = pair[0]
        cents = pair[1]
        filtered = []
        for i in range(len(cents)):
            for j in range(len(newGTable)):
                if round(cents[i].x, 3) == round(newGTable[j].x, 3) and round(cents[i].y, 3) == round(newGTable[j].y, 3) and round(cents[i].z, 3) == round(newGTable[j].z, 3):
                    filtered.append(j)
        preVTable.append((newGTable.index(super), filtered))
    
    for pair in preVTable:
        super = pair[0]
        filteredCents = pair[1]
        for i in range(len(filteredCents)):
            r = random(0, 255)
            g = random(0, 255)
            b = random(0, 255)
            clr = PVector(r, g, b)
            newCTable.append(clr)
            newVTable.append(super)
            newVTable.append(filteredCents[i])
            if (i == len(filteredCents) - 1):
                newVTable.append(filteredCents[0])
            else:
                newVTable.append(filteredCents[i + 1])

    for i in range(len(newVTable)):
        newOTable.append(None)
    
    for a in range(len(newVTable)):
        for b in range(len(newVTable)):
            if (a != b):
                if (newGTable[newVTable[next(a)]] == newGTable[newVTable[previous(b)]] and newGTable[newVTable[previous(a)]] == newGTable[newVTable[next(b)]]):
                    newOTable[a] = b
                    newOTable[b] = a
                    
    polyhedra.gtable = newGTable
    polyhedra.vtable = newVTable
    polyhedra.otable = newOTable
    polyhedra.ctable = newCTable
    
    
    global vtxNormals
    vtxNormals = perVertexShading()

    
# def dual():
#     newGTable = []
#     newVTable = []
#     newOTable = []
#     newCTable = []
#     for vtx in range(len(polyhedra.gtable)):
#         centroidList = []
#         firstCorner = polyhedra.vtable.index(vtx)
#         nextCorner = next(firstCorner)
#         prevCorner = previous(firstCorner)
#         sVtx = polyhedra.gtable[polyhedra.vtable[firstCorner]]
#         nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
#         pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
#         centroid = calculateCentroid(sVtx, nVtx, pVtx)
#         centroidList.append(centroid)
#         if not centroid in newGTable:
#             newGTable.append(centroid)
#             # print(newGTable)
#         # superCentroid = centroidList[0]  #initialize supercentroid with the first centroid, will add other centroid values later
#         superCentroid = Vtx(0.0, 0.0, 0.0)
#         superCentroid.x = superCentroid.x + centroidList[0].x
#         superCentroid.y = superCentroid.y + centroidList[0].y
#         superCentroid.z = superCentroid.z + centroidList[0].z
#         swingCorner = swing(firstCorner)
#         while (swingCorner != firstCorner):
#             nextCorner = next(swingCorner)
#             prevCorner = previous(swingCorner)
#             sVtx = polyhedra.gtable[polyhedra.vtable[swingCorner]]
#             nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
#             pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
#             swingCentroid = calculateCentroid(sVtx, nVtx, pVtx)
#             centroidList.append(swingCentroid)
#             if not swingCentroid in newGTable:
#                 newGTable.append(swingCentroid)
#             superCentroid.x = superCentroid.x + swingCentroid.x
#             superCentroid.y = superCentroid.y + swingCentroid.y
#             superCentroid.z = superCentroid.z + swingCentroid.z
#             swingCorner = swing(swingCorner)
#         superCentroid.x = superCentroid.x / len(centroidList)         #now we actually calculate the centroid of centroids, by averaging the added values together
#         superCentroid.y = superCentroid.y / len(centroidList)
#         superCentroid.z = superCentroid.z / len(centroidList)
#         # print(centroidList)
#         superCentroidIndex = len(newGTable)
#         newGTable.append(superCentroid)
#         vtablehelper = [None] * len(centroidList)
#         for i in range(len(centroidList)):
#             if centroidList[i] in newGTable:
#                 vtablehelper[i] = newGTable.index(centroidList[i])
#         for i in range(len(centroidList)):
#             r = random(0, 255)
#             g = random(0, 255)
#             b = random(0, 255)
#             clr = PVector(r, g, b)
#             newCTable.append(clr)
#             newVTable.append(superCentroidIndex)
#             newVTable.append(vtablehelper[i])
#             if (i == len(centroidList) - 1):
#                 newVTable.append(vtablehelper[0])
#             else:
#                 newVTable.append(vtablehelper[i + 1])
    
#     for i in range(len(newVTable)):
#         newOTable.append(None)
    
#     for a in range(len(newVTable)):
#         for b in range(len(newVTable)):
#             if (a != b):
#                 if (newGTable[newVTable[next(a)]] == newGTable[newVTable[previous(b)]] and newGTable[newVTable[previous(a)]] == newGTable[newVTable[next(b)]]):
#                     newOTable[a] = b
#                     newOTable[b] = a
#                 # if(newVTable[next(a)] == newVTable[previous(b)] and newVTable[previous(a)] == newVTable[next(b)]):
#                 #     newOTable[a] = b
#                 #     newOTable[b] = a
    
#     # print(newGTable)
#     # print(newVTable)
#     # print(newOTable)
#     for i in range(len(newGTable)):
#         print(newGTable[i].x, newGTable[i].y , newGTable[i].z)
#     print(newVTable)
#     print(newOTable)
#     polyhedra.gtable = newGTable
#     polyhedra.vtable = newVTable
#     polyhedra.otable = newOTable
#     polyhedra.ctable = newCTable
    
#     global vtxNormals
#     vtxNormals = perVertexShading()
#     print("end of dual")
    
        
def calculateCentroid(curr, next, prev):
    x = (curr.x + next.x + prev.x)/3
    y = (curr.y + next.y + prev.y)/3
    z = (curr.z + next.z + prev.z)/3
    centroid = Vtx(x, y, z)
    return centroid

def tri(corner):
    return corner/3

def next(corner):
    return ((3 * tri(corner)) + ((corner + 1) % 3))

def previous(corner):
    return next(next(corner))

def getOpposite(corner):
    return polyhedra.otable[corner]

def swing(corner):
    return next(getOpposite(next(corner)))

def perVertexShading():
    vtxNormals = []
    for vtx in range(len(polyhedra.gtable)):
        normals = []
        firstCorner = polyhedra.vtable.index(vtx)
        nextCorner = next(firstCorner)
        prevCorner = previous(firstCorner)
        sVtx = polyhedra.gtable[polyhedra.vtable[firstCorner]]
        nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
        pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
        e1 = PVector(nVtx.x - sVtx.x, nVtx.y - sVtx.y, nVtx.z - sVtx.z)
        e2 = PVector(pVtx.x - sVtx.x, pVtx.y - sVtx.y, pVtx.z - sVtx.z)
        n = PVector.cross(e2, e1)
        n.normalize()
        normals.append(n)
        swingCorner = swing(firstCorner)
        while (swingCorner != firstCorner):
            nextCorner = next(swingCorner)
            prevCorner = previous(swingCorner)
            sVtx = polyhedra.gtable[polyhedra.vtable[swingCorner]]
            nVtx = polyhedra.gtable[polyhedra.vtable[nextCorner]]
            pVtx = polyhedra.gtable[polyhedra.vtable[prevCorner]]
            e1 = PVector(nVtx.x - sVtx.x, nVtx.y - sVtx.y, nVtx.z - sVtx.z)
            e2 = PVector(pVtx.x - sVtx.x, pVtx.y - sVtx.y, pVtx.z - sVtx.z)
            n = PVector.cross(e2, e1)
            n.normalize()
            normals.append(n)
            swingCorner = swing(swingCorner)
        x = 0.0
        y = 0.0
        z = 0.0
        for n in normals:
            x = x + n.x
            y = y + n.y
            z = z + n.z
        xvtx = x / len(normals)
        yvtx = y / len(normals)
        zvtx = z / len(normals)
        vtxNorm = PVector(xvtx, yvtx, zvtx)
        vtxNorm.normalize()
        vtxNormals.append(vtxNorm)
    return vtxNormals
        
            