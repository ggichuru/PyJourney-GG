        ## Using DIRECT FORMULAR
import math

def getX(a,b,c):
    discriminant = b*b - 4*a*c
    sqroot = math.sqrt(abs(discriminant))

    if discriminant > 0:
        print('The greatest root is: ')
        x = (-b+sqroot)/(2*a)
        y = (-b-sqroot)/(2*a)
        maximum = max(x,y)
        print(int(maximum))

    elif discriminant == 0:
        print(-b/(2*a))
    else:
        x1 = (-b/(2*a), ' + i', sqroot)
        y1 = (-b/(2*a), ' - i', sqroot)
        maxi = max(x1,y1)
        print(maxi)

a = 1
b = 2
c = -4

if a == 0:
    print('Incorrect equation')
else:
    getX(a,b,c)