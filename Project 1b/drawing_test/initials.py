# In the routine below, you should draw your initials in perspective

# Pranshav Thakkar

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective(90, 100, -100)
    #gtOrtho(-100, 100, -100, 100, -2, -2)
    gtPushMatrix()
    #gtTranslate(0, 0, -10)
    gtRotateX(30)
    gtBeginShape()
    
    gtVertex(-0.5, 0.0, 1.0)
    gtVertex(-0.5, 1.0, 1.0)
    
    gtVertex(-0.5, 1.0, 1.0)
    gtVertex(0.0, 1.0, 1.0)
    
    gtVertex(0.0, 1.0, 1.0)
    gtVertex(0.0, 0.5, 1.0)
    
    gtVertex(-0.5, 0.5, 1.0)
    gtVertex(0.0, 0.5, 1.0)
    
    gtVertex(0.15, 1.0, 1.0)
    gtVertex(0.85, 1.0, 1.0)
    
    gtVertex(0.5, 1.0, 1.0)
    gtVertex(0.5, 0.0, 1.0)
    
    gtEndShape()
    gtPopMatrix()