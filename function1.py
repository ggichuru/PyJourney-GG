def check_driver_speed(speed):
    d = 0
    speed = int(speed)
    if(speed <= 70):
        print("OK")
    elif(speed == 75 and speed % 5 == 0):
        d += ((speed-75)/5) + 1
        print("Demerit points:", d)
    elif(d>=12):
        print("License suspended")

speed = 200
check_driver_speed(80)