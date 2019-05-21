 # This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

# Pranshav Thakkar
import Queue
from scene import Scene
from backgrnd import Background
from light import Light
from ray import Ray
from spherez import Sphere
from surface import Surface
scn = None
backgrnd = Background(0,0,0)
lightz = []
objects = []
surfaces = Queue.Queue(maxsize=0)
k = 0.0
surfaceFlag = 0



def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global scn, backgrnd, lightz, objects, surfaces, k, surfaceFlag
    scn = None
    backgrnd = Background(0, 0, 0)
    lightz = []
    objects = []
    surfaces = Queue.Queue(maxsize=0)
    k = 0.0
    surfaceFlag = 0
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            # call your sphere creation routine here
            # for example: create_sphere(radius,x,y,z)
            if surfaceFlag == 1:
                global surfaces, surfaceFlag
                surf = surfaces.get()
                surfaceFlag = 0
                sp = Sphere(radius, x, y, z, surf)
                global objects
                objects.append(sp)
        elif words[0] == 'fov':
            degree_angle = float(words[1])
            #store fov angle
            
            global k
            k = tan(radians(degree_angle/2))
        elif words[0] == 'background':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            #store background color
            global backgrnd
            backgrnd = Background(r, g, b)
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            #store point light
            l = Light(x, y, z, r, g, b)
            global lightz
            lightz.append(l)
        elif words[0] == 'surface':
            cdr = float(words[1])
            cdg = float(words[2])
            cdb = float(words[3])
            car = float(words[4])
            cag = float(words[5])
            cab = float(words[6])
            csr = float(words[7])
            csg = float(words[8])
            csb = float(words[9])
            p = float(words[10])
            krefl = float(words[11])
            #add surface
            global surfaceFlag
            surfaceFlag = 1
            s = Surface(cdr, cdg, cdb, car, cag, cab, csr, csg, csb, p, krefl)
            global surfaces
            surfaces.put(s)
        elif words[0] == 'begin':
            #just to handle the surfaces for now
            if surfaceFlag == 1:
                surf = surfaces.get()
                global surfaceFlag
                surfaceFlag = 0
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass
            
        global scn
        scn = Scene(backgrnd, lightz, objects, surfaces, k)

# render the ray tracing scene
def render_scene():
    for j in range(height):
        for i in range(width):
            # create an eye ray for pixel (i,j) and cast it into the scene
            orig = PVector(0, 0, 0)
            xpr = (i *((2*scn.k)/width)) - scn.k
            ypr = ((j *((2*scn.k)/height)) - scn.k) * -1
            direc = PVector(xpr, ypr, -1)
            ray = Ray(orig, direc)
            closestT = 99999
            closestObj = None
            for object in scn.objects:
                roots = calculateT(ray, object)
                if roots == None:
                    closestT = closestT
                    closestObj = closestObj
                elif len(roots) == 1:
                    if roots[0] > 0 and roots[0] < closestT:
                        closestT = roots[0]
                        closestObj = object
                elif len(roots) == 2:
                    a = 0
                    if roots[0] > 0 and roots[1] < 0:
                        a = roots[0]
                        if a < closestT:
                            closestT = a
                            closestObj = object
                    elif roots[0] < 0 and roots[1] > 0:
                        a = roots[1]
                        if a < closestT:
                            closestT = a
                            closestObj = object
                    elif roots[0] > 0 and roots[1] > 0:
                        a = min(roots[0], roots[1])
                        if a < closestT:
                            closestT = a
                            closestObj = object
            
            if closestT == 99999:
                pix_color = color(scn.backgrnd.r, scn.backgrnd.g, scn.backgrnd.b)
            else:
                #pix_color = color(0.8, 0.2, 0.4)  # you should calculate the correct pixel color here
                clr = 0.0
                clg = 0.0
                clb = 0.0
                for light in scn.lightz:
                    if type(closestObj) is Sphere:
                        n = PVector((ray.direction.x*closestT) - closestObj.x, (ray.direction.y*closestT) - closestObj.y, (ray.direction.z*closestT) - closestObj.z)
                        n.normalize()
                    l = PVector(light.x - (ray.direction.x*closestT), light.y - (ray.direction.y*closestT), light.z - (ray.direction.z*closestT))
                    l.normalize()
                    nl = max(0,n.dot(l))
                    clr = clr + (light.r * nl)
                    clg = clg + (light.g * nl)
                    clb = clb + (light.b * nl)
                    
                
                pix_color = color(closestObj.surface.cdr * clr,closestObj.surface.cdg * clg,closestObj.surface.cdb * clb )
            set (i, j, pix_color)         # fill the pixel with the calculated color
    pass

def calculateT(ray, object):
    x0 = ray.origin.x
    y0 = ray.origin.y
    z0 = ray.origin.z
    dx = ray.direction.x
    dy = ray.direction.y
    dz = ray.direction.z
    
    if type(object) is Sphere:
        xc = object.x
        yc = object.y
        zc = object.z
        radius = object.radius
        
        a = dx*dx + dy*dy + dz*dz
        b = 2*((dx*(x0-xc)) + (dy*(y0-yc)) + (dz*(z0-zc)))
        c = (x0-xc)*(x0-xc) + (y0-yc)*(y0-yc) + (z0-zc)*(z0-zc) - radius*radius
        discrim = b*b - 4*a*c

        roots = []
        
        if (discrim < 0):
            return None
        elif (discrim == 0):
            roots.append(((b*-1)/(2*a)))
            return roots
        elif (discrim > 0):
            roots.append(((b*-1) + sqrt(discrim))/(2*a))
            roots.append(((b*-1) - sqrt(discrim))/(2*a))
            return roots
    
    
    
    
    

# should remain empty for this assignment
def draw():
    pass