# Pranshav Thakkar

# Let's get ramblin' ramblin' wrecked son!

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (1.0)
    
    # red box
    # fill (255, 0, 0)
    # pushMatrix()
    # translate (-30, 0, 0)
    # rotateX (time)
    # box(20)
    # popMatrix()

    # green sphere
    # fill (0, 250, 0)
    # pushMatrix()
    # translate (0, 8 * sin(4 * time), 0)  # move up and down
    # sphereDetail(60)  # this controls how many polygons are used to make a sphere
    # sphere(10)
    # popMatrix()

    # blue cylinder
    # fill (0, 0, 255)
    # pushMatrix()
    # translate (30, 0, 0)
    # rotateX (-time)
    # scale (10, 10, 10)
    # cylinder()
    # popMatrix()
    
    pushMatrix()
    
    rotateY(time)
    
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
    #rotateX(time)
    sphereDetail(60)
    sphere(10)
    popMatrix()
    
    #left eye
    fill(255, 255, 255)
    pushMatrix()
    translate(-3, -13, 9)
    #rotateX(time)
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