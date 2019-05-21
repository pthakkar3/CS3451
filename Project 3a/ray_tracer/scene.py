class Scene(object):
    
    backgrnd = None
    lightz = []
    objects = []
    surfaces = []
    k = 0.0
    
    def __init__(self, backgrnd, lightz, objects, surfaces, k):
        self.backgrnd = backgrnd
        self.lightz = lightz
        self.objects = objects
        self.surfaces = surfaces
        self.k = k
        