# Pranshav Thakkar

# Let's get ramblin' ramblin' wrecked, Morty!
# I will be instancing Pickle Rick!

time = 0   # use time to move objects from one frame to the next
moveMortyX = 0
moveMortyY = 0
moveMortyZ = 0
rotateMortyY = 0
rotateMortyZ = 0

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01
    
    print(frameCount)
    if frameCount == 3000:
        exit()
    
    camera(0, 0, 300 - 5*time, 0, 0, 0, 0, 1, 0)
            
    background (255, 255, 255)  # clear screen and set background to white
    
    # create a point light source
    ambientLight(50, 50, 50)
    lightSpecular(255, 255, 255)
    pointLight(255, 255, 255, 0, 0, 40)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
        
    pushMatrix()
    
    #Portal 1
    if time <= 13:
        fill(0, 255, 0)
        pushMatrix()
        translate(0, 0, -40)
        ellipse(90, 0, 75, 75)
        popMatrix()
        
    if time > 13 and time <= 15:
        #Portal 2
        fill(0, 255, 0)
        pushMatrix()
        translate(0, 0, -40)
        ellipse(-90, 0, 75, 75)
        popMatrix()
    
        #Portal 3
        fill(0, 255, 0)
        pushMatrix()
        translate(0, 0, -40)
        ellipse(0, 0, 75, 75)
        popMatrix()
    

    #left wall
    fill(102, 51, 0)
    pushMatrix()
    translate(-150, -15, 0)
    rotateY(radians(90))
    box(110, 150, 10)
    popMatrix()

    #right wall
    fill(102, 51, 0)
    pushMatrix()
    translate(150, -15, 0)
    rotateY(radians(90))
    box(110, 150, 10)
    popMatrix()
    
    #back wall
    fill(102, 51, 0)
    pushMatrix()
    translate(0, -15, -50)
    box(300, 150, 10)
    popMatrix()
    
    #ceiling
    fill(102, 51, 0)
    pushMatrix()
    translate(0, -85, 0)
    rotateX(radians(90))
    box(300, 110, 10)
    popMatrix()
    
    #floor
    fill(80, 80, 80)
    pushMatrix()
    translate(0, 55, 0)
    rotateX(radians(90))
    box(300, 110, 10)
    popMatrix()
    
    #Morty goes into the Portal
    if time <= 13:
        pushMatrix()
        translate(moveMortyX, moveMortyY, moveMortyZ)
        rotateY(radians(rotateMortyY))
        rotateZ(radians(rotateMortyZ))
        draw_morty()
        popMatrix()
        
    #Two Pickle Ricks Appear!    
    if time > 13 and time <= 15:
        pushMatrix()
        translate(0, 45, 0)
        pickle_rick()
        popMatrix()
        
        pushMatrix()
        translate(-90, 45, 0)
        pickle_rick()
        popMatrix()
        
    #It's a Pickle Rick Party    
    if time > 15:
        pushMatrix()
        translate(0, 45 * sin(time), 0)
        pickle_rick()
        popMatrix()
        
        pushMatrix()
        translate(-90, 45 * cos(time), 0)
        pickle_rick()
        popMatrix()
    
    popMatrix()
    
def pickle_rick():
    
    #torso
    fill(82, 163, 99)
    pushMatrix()
    scale(2, 4, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #upper curve
    fill(82, 163, 99)
    pushMatrix()
    translate(0, -4, 0)
    sphereDetail(60)
    sphere(2)
    popMatrix()
    
    #right eye
    fill(255, 255, 255)
    pushMatrix()
    translate(0.75, -3.5, 1.75)
    sphereDetail(60)
    sphere(0.5)
    popMatrix()
    
    #left eye
    fill(255, 255, 255)
    pushMatrix()
    translate(-0.75, -3.5, 1.75)
    sphereDetail(60)
    sphere(0.5)
    popMatrix()
    
    #left pupil
    fill(0, 0, 0)
    pushMatrix()
    translate(-0.75, -3.5, 2.25)
    sphereDetail(60)
    sphere(0.1)
    popMatrix()
    
    #right pupil
    fill(0, 0, 0)
    pushMatrix()
    translate(0.75, -3.5, 2.25)
    sphereDetail(60)
    sphere(0.1)
    popMatrix()
    
    #unibrow
    fill(126,192,238)
    pushMatrix()
    translate(0, -4.5, 1.5)
    scale(1.25, 0.2, 0.5)
    rotateY(radians(90))
    cylinder()
    popMatrix()
    
    #mouth
    fill(0, 100, 0)
    pushMatrix()
    translate(0, -2, 1.5)
    sphereDetail(60)
    sphere(0.65)
    popMatrix()
    
    #lower curve
    fill(82, 163, 99)
    pushMatrix()
    translate(0, 4, 0)
    sphereDetail(60)
    sphere(2)
    popMatrix()
    
def draw_morty():
    global moveMortyX, moveMortyY, moveMortyZ, rotateMortyY, rotateMortyZ
        
    if time >=0 and time <= 1:
        moveMortyX = 0
        moveMortyY = 0
        moveMortyZ = 0
        rotateMortyY = 0
        rotateMortyZ = 0
    elif time > 1 and time <= 1.5:
        rotateMortyY = 90
    elif time > 1.5 and time <= 8:
        moveMortyX = time * 10
    elif time > 8 and time <= 8.5:
        rotateMortyY = 180
    elif time > 8.5 and time <= 9.5:
        moveMortyZ = -time * 2
    elif time > 9.5 and time <= 13:
        rotateMortyZ = time * 45
    
    #hair
    fill(123, 63, 0)
    pushMatrix()
    translate(0, -15.5, 0)
    sphereDetail(60)
    sphere(9)
    popMatrix()
     
    #head 
    fill(255, 220, 177)
    pushMatrix()
    translate(0, -13, 0)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    #left eye
    fill(255, 255, 255)
    pushMatrix()
    translate(-3, -13, 9)
    sphereDetail(60)
    sphere(3)
    popMatrix()
    
    #right eye
    fill(255, 255, 255)
    pushMatrix()
    translate(3, -13, 9)
    sphereDetail(60)
    sphere(3)
    popMatrix()
    
    #left pupil
    fill(0,0,0)
    pushMatrix()
    translate(-3, -13, 12)
    sphere(0.5)
    popMatrix()
    
    #right pupil
    fill(0,0,0)
    pushMatrix()
    translate(3, -13, 12)
    sphere(0.5)
    popMatrix()
    
    #mouth
    fill(150,0,0)
    pushMatrix()
    translate(0, -7.5, 5.75)
    sphereDetail(60)
    sphere(2.5)
    popMatrix()
    
    #torso
    fill(255, 255, 0)
    pushMatrix()
    translate(0, 4.5, 0)
    scale(8,8,8)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #torso longer
    fill(255, 255, 0)
    pushMatrix()
    translate(0, 8.5, 0)
    scale(8,8,8)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #left sleeve
    fill(255, 255, 0)
    pushMatrix()
    translate(-9, 2.5, 0)
    rotateZ(radians(30))
    scale(2, 5, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #left arm
    fill(255, 220, 177)
    pushMatrix()
    translate(-13.25, 10, 0)
    rotateZ(radians(30))
    scale(1.75, 5, 1.75)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #left hand
    fill(255,220,177)
    pushMatrix()
    translate(-16.75, 16, 0)
    sphereDetail(60)
    sphere(2.25)
    popMatrix()
    
    #right sleeve
    fill(255, 255, 0)
    pushMatrix()
    translate(9, 2.5, 0)
    rotateZ(radians(330))
    scale(2, 5, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #right arm
    fill(255, 220, 177)
    pushMatrix()
    translate(13.25, 10, 0)
    rotateZ(radians(330))
    scale(1.75, 5, 1.75)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #right hand
    fill(255,220,177)
    pushMatrix()
    translate(16.75, 16, 0)
    sphereDetail(60)
    sphere(2.25)
    popMatrix()
    
    #rounded hips area
    fill(0, 0, 255)
    pushMatrix()
    translate(0, 16, 0)
    sphereDetail(60)
    sphere(7.9)
    popMatrix()
    
    #left leg
    fill(0, 0, 255)
    pushMatrix()
    translate(-4, 30, 0)
    scale(2, 15, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #left shoe
    fill(0,0,0)
    pushMatrix()
    translate(-4, 46.5, 1.25)
    box(4, 2.5, 6)
    popMatrix()
    
    #right leg
    fill(0, 0, 255)
    pushMatrix()
    translate(4, 30, 0)
    scale(2, 15, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    #right shoe
    fill(0,0,0)
    pushMatrix()
    translate(4, 46.5, 1.25)
    box(4, 2.5, 6)
    popMatrix()
    
# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2