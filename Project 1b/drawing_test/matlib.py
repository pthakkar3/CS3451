# Matrix Stack Library -- Use your code from Project 1A

# Pranshav Thakkar

import math

global stack
stack = []

def gtInitialize():
    #create a list inside a list, effectively a matrix
    matrix = [[0 for x in range(4)] for y in range(4)]
    #matrix is initialized as the identity matrix
    matrix[0][0] = 1
    matrix[1][1] = 1
    matrix[2][2] = 1
    matrix[3][3] = 1
    global stack
    #clears the matrix stack every time initialize is called, to ensure that we are starting from scratch
    del stack[:]
    stack.append(matrix)

def gtPushMatrix():
    global stack
    fromStack = stack[len(stack) - 1]
    #I copy fromStack to new_ctm like this to ensure that it is a copy, not a reference to the value. It may be unnecessary, but it works!
    new_ctm = fromStack[:][:]
    stack.append(new_ctm)

def gtPopMatrix():
    global stack
    if len(stack) == 1:
        print "Cannot pop the matrix stack \n"
        return
    else:
        #pops the topmost matrix off of the stack
        stack.pop()

def gtTranslate(x, y, z):
    global stack
    fromStack = stack[len(stack) - 1]
    old_ctm = fromStack[:][:]
    translate_matrix = [[0 for a in range(4)] for b in range(4)]
    #creates the translation matrix
    translate_matrix[0][0] = 1
    translate_matrix[1][1] = 1
    translate_matrix[2][2] = 1
    translate_matrix[3][3] = 1
    translate_matrix[0][3] = x
    translate_matrix[1][3] = y
    translate_matrix[2][3] = z
    
    #matrix multiply calculates old_ctm * translate_matrix
    new_ctm = matrix_multiply(old_ctm, translate_matrix)
    #update the current ctm by removing the old one and appending the new ctm
    del stack[len(stack) - 1]
    stack.append(new_ctm)

def gtScale(x, y, z):
    global stack
    fromStack = stack[len(stack) - 1]
    old_ctm = fromStack[:][:]
    scale_matrix = [[0 for a in range(4)] for b in range(4)]
    #creates scaling matrix
    scale_matrix[0][0] = x
    scale_matrix[1][1] = y
    scale_matrix[2][2] = z
    scale_matrix[3][3] = 1
    
    new_ctm = matrix_multiply(old_ctm, scale_matrix)
    del stack[len(stack) - 1]
    stack.append(new_ctm)

def gtRotateX(theta):
    global stack
    fromStack = stack[len(stack) - 1]
    old_ctm = fromStack[:][:]
    rotateX_matrix = [[0 for a in range(4)] for b in range(4)]
    #creates rotation matrix in X
    rotateX_matrix[0][0] = 1
    rotateX_matrix[1][1] = cos(math.radians(theta))
    rotateX_matrix[1][2] = (sin(math.radians(theta))) * -1
    rotateX_matrix[2][1] = sin(math.radians(theta))
    rotateX_matrix[2][2] = cos(math.radians(theta))
    rotateX_matrix[3][3] = 1
    
    new_ctm = matrix_multiply(old_ctm, rotateX_matrix)
    del stack[len(stack) - 1]
    stack.append(new_ctm)

def gtRotateY(theta):
    global stack
    fromStack = stack[len(stack) - 1]
    old_ctm = fromStack[:][:]
    rotateY_matrix = [[0 for a in range(4)] for b in range(4)]
    #creates rotation matrix in Y
    rotateY_matrix[0][0] = cos(math.radians(theta))
    rotateY_matrix[0][2] = sin(math.radians(theta))
    rotateY_matrix[1][1] = 1
    rotateY_matrix[2][0] = (sin(math.radians(theta))) * -1
    rotateY_matrix[2][2] = cos(math.radians(theta))
    rotateY_matrix[3][3] = 1
    
    new_ctm = matrix_multiply(old_ctm, rotateY_matrix)
    del stack[len(stack) - 1]
    stack.append(new_ctm)

def gtRotateZ(theta):
    global stack
    fromStack = stack[len(stack) - 1]
    old_ctm = fromStack[:][:]
    rotateZ_matrix = [[0 for a in range(4)] for b in range(4)]
    #creates rotation matrix in Z
    rotateZ_matrix[0][0] = cos(math.radians(theta))
    rotateZ_matrix[0][1] = (sin(math.radians(theta))) * -1
    rotateZ_matrix[1][0] = sin(math.radians(theta))
    rotateZ_matrix[1][1] = cos(math.radians(theta))
    rotateZ_matrix[2][2] = 1
    rotateZ_matrix[3][3] = 1
    
    new_ctm = matrix_multiply(old_ctm, rotateZ_matrix)
    del stack[len(stack) - 1]
    stack.append(new_ctm)

def gtGetMatrix():
    #returns CTM
    global stack
    return stack[len(stack) - 1]

def print_ctm():
    global stack
    ctm = stack[len(stack) - 1]
    for x in range(4):
        print ctm[x]
    print \n
    
def matrix_multiply(old_ctm, transform):
    
    new_ctm = [[0 for x in range(4)] for y in range(4)]
    new_ctm[0][0] = (old_ctm[0][0] * transform[0][0]) + (old_ctm[0][1] * transform[1][0]) + (old_ctm[0][2] * transform[2][0]) + (old_ctm[0][3] * transform[3][0])
    new_ctm[1][0] = (old_ctm[1][0] * transform[0][0]) + (old_ctm[1][1] * transform[1][0]) + (old_ctm[1][2] * transform[2][0]) + (old_ctm[1][3] * transform[3][0])
    new_ctm[2][0] = (old_ctm[2][0] * transform[0][0]) + (old_ctm[2][1] * transform[1][0]) + (old_ctm[2][2] * transform[2][0]) + (old_ctm[2][3] * transform[3][0])
    new_ctm[3][0] = (old_ctm[3][0] * transform[0][0]) + (old_ctm[3][1] * transform[1][0]) + (old_ctm[3][2] * transform[2][0]) + (old_ctm[3][3] * transform[3][0])
    new_ctm[0][1] = (old_ctm[0][0] * transform[0][1]) + (old_ctm[0][1] * transform[1][1]) + (old_ctm[0][2] * transform[2][1]) + (old_ctm[0][3] * transform[3][1])
    new_ctm[1][1] = (old_ctm[1][0] * transform[0][1]) + (old_ctm[1][1] * transform[1][1]) + (old_ctm[1][2] * transform[2][1]) + (old_ctm[1][3] * transform[3][1])
    new_ctm[2][1] = (old_ctm[2][0] * transform[0][1]) + (old_ctm[2][1] * transform[1][1]) + (old_ctm[2][2] * transform[2][1]) + (old_ctm[2][3] * transform[3][1])
    new_ctm[3][1] = (old_ctm[3][0] * transform[0][1]) + (old_ctm[3][1] * transform[1][1]) + (old_ctm[3][2] * transform[2][1]) + (old_ctm[3][3] * transform[3][1])
    new_ctm[0][2] = (old_ctm[0][0] * transform[0][2]) + (old_ctm[0][1] * transform[1][2]) + (old_ctm[0][2] * transform[2][2]) + (old_ctm[0][3] * transform[3][2])
    new_ctm[1][2] = (old_ctm[1][0] * transform[0][2]) + (old_ctm[1][1] * transform[1][2]) + (old_ctm[1][2] * transform[2][2]) + (old_ctm[1][3] * transform[3][2])
    new_ctm[2][2] = (old_ctm[2][0] * transform[0][2]) + (old_ctm[2][1] * transform[1][2]) + (old_ctm[2][2] * transform[2][2]) + (old_ctm[2][3] * transform[3][2])
    new_ctm[3][2] = (old_ctm[3][0] * transform[0][2]) + (old_ctm[3][1] * transform[1][2]) + (old_ctm[3][2] * transform[2][2]) + (old_ctm[3][3] * transform[3][2])
    new_ctm[0][3] = (old_ctm[0][0] * transform[0][3]) + (old_ctm[0][1] * transform[1][3]) + (old_ctm[0][2] * transform[2][3]) + (old_ctm[0][3] * transform[3][3])
    new_ctm[1][3] = (old_ctm[1][0] * transform[0][3]) + (old_ctm[1][1] * transform[1][3]) + (old_ctm[1][2] * transform[2][3]) + (old_ctm[1][3] * transform[3][3])
    new_ctm[2][3] = (old_ctm[2][0] * transform[0][3]) + (old_ctm[2][1] * transform[1][3]) + (old_ctm[2][2] * transform[2][3]) + (old_ctm[2][3] * transform[3][3])
    new_ctm[3][3] = (old_ctm[3][0] * transform[0][3]) + (old_ctm[3][1] * transform[1][3]) + (old_ctm[3][2] * transform[2][3]) + (old_ctm[3][3] * transform[3][3])
    
    return new_ctm