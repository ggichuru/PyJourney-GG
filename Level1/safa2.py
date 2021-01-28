import numpy as np

def getX():
    coeff = [1,2,-4]
    maximum = max(np.roots(coeff))
    print(int(maximum))
getX()