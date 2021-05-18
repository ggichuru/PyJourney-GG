def check_speed_limit(speed):
    if speed > 70:
        limit = speed - 70
        demerit = limit // 5
        print("Your demerit points are: ", demerit)

        if demerit > 12:
            print("Your license suspended")

    else:
        print('OK')

    

speed = int(input("Enter speed: "))
check_speed_limit(speed)