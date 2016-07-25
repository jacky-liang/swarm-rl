import numpy as np

from util import cartesian_to_polar, polar_to_cartesian

class SwarmAgent:

    def __init__(self, cartesian):
        self.cartesian = cartesian
        
    @property
    def cartesian(self):
        return self._cartesian.copy()
        
    @position.setter
    def cartesian(self, pos):
        if len(pos) != 2:
            raise Exception("Bad cartesian argument {0}".format(pos))
        if type(pos) in (list, tuple):
            pos = np.array(pos)
        self._cartesian = pos
    
    @property
    def polar(self, origin=np.zeros(3)):
        return cartesian_to_polar(self.cartesian, origin)
        
    @polar.setter:
    def polar(self, pol):
        if len(pol) != 2:
            raise Exception("Bad polar argument {0}".format(pol))
        if type(pol) in (list, tuple):
            pol = np.array(pol)
        if not 0 <= pol[1] < 2 * np.pi:
            raise Exception("Bad angle for polar argument {0}".format(pol))
            
        self.cartesian = polar_to_cartesian(pol)