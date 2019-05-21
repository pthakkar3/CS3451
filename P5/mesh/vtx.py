class Vtx(object):
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __eq__(self, other):
        # print("eqqualssss")
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return self.x + self.y + self.z
    
    def __cmp__(self):
        return object.__cmp__(self)