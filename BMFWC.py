import time

# Stuff for getting time
lastMinute = 0

# Initialization of dotstar params
nLEDs = 18*7 + 5*9 + 4
r = 255
g = 0
b = 0

numberColoring = {0: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        0,0,0,0,0],
                  1: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0],
                  2: [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
                        1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
                        1,1,1,1,1],
                  3: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
                        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1],
                  4: [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                        1,1,1,1,1],
                  5: [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1],
                  6: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1],
                  7: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,
                        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                        0,0,0,0,0],
                  8: [1]*51,
                  9: [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                        1,1,1,1,1]}


""" Function to assign the number coloring to the pixels """
def AssignDotStars(h1, h2, m1, m2, R, G, B, r1, g1, b1):
    # Tens Hour
    if h1:
        R[:18] = [r1]*18
        G[:18] = [g1]*18
        B[:18] = [b1]*18
    # Ones Hour
    R[18:69] = [r1*i for i in numberColoring[h2]]
    G[18:69] = [g1*i for i in numberColoring[h2]]
    B[18:69] = [b1*i for i in numberColoring[h2]]
    # Colons
    R[69:73] = [r1]*4
    G[69:73] = [g1]*4
    B[69:73] = [b1]*4
    # Tens Minute
    R[73:124] = [r1*i for i in numberColoring[m1]]
    G[73:124] = [g1*i for i in numberColoring[m1]]
    B[73:124] = [b1*i for i in numberColoring[m1]]
    # Ones Minute
    R[124:] = [r1*i for i in numberColoring[m2]]
    G[124:] = [g1*i for i in numberColoring[m2]]
    B[124:] = [b1*i for i in numberColoring[m2]]
    return R, G, B


""" Function to fade the coloring """
def FadeColor(r,g,b):
    if(r > 0 and b == 0):
        r -= 1
        g += 1
    if(g > 0 and r == 0):
        g -= 1
        b +=1
    if(b > 0 and g == 0):
        r += 1
        b -= 1
    return r,g,b


""" Main loop that runs forever """
while(True):

    # Init array for DotStars
    R = [0]*nLEDs
    G = [0]*nLEDs
    B = [0]*nLEDs

    # Time Stuff
    currentTime = time.localtime()
    currentHour = currentTime.tm_hour
    currentMinute = currentTime.tm_min
    currentHour = currentHour % 12
    tensDigitHour = currentHour / 10
    onesDigitHour = currentHour % 10
    tensDigitMinute = currentMinute / 10
    onesDigitMinute = currentMinute % 10
    if not onesDigitMinute == lastMinute:
        # Fade the color
        r,g,b = FadeColor(r,g,b)
        # Assign the dotstars
        R, G, B = AssignDotStars(tensDigitHour, onesDigitHour, tensDigitMinute,
                                 onesDigitMinute, R, G, B, r, g, b)
        # Shoot them out to physical modules - still TODO
        print(tensDigitHour, onesDigitHour, tensDigitMinute, onesDigitMinute)
        lastMinute = onesDigitMinute

    time.sleep(30)

