from numpy import np

def get_cartesian_angle(x, y):
        theta = 0
        if x == 0:
            if y >= 0:
                theta = np.pi / 2.
            else: 
                theta = - np.pi / 2.
        else:
            theta_ref = abs(np.arctan(y/1./x))
            if theta_ref > np.pi/2.:
                theta_ref = np.pi - theta_ref

            if x >= 0 and y >= 0:
                theta = theta_ref
            elif y >= 0 and x < 0:
                theta = np.pi - theta_ref
            elif y < 0 and x < 0:
                theta = np.pi + theta_ref
            else:
                theta = 2*np.pi - theta_ref
                
        return theta

def polar_to_cartesian(pol):
    r, t = pol[0], pol[1]
    coord = r * np.array([np.cos(t), np.sin(t)])
    return coord
    
def cartesian_to_polar(pos):
    r = np.linalg.norm(pos)
    t = get_cartesian_angle(pos[0], pos[1])
    
    return np.array([r, t])