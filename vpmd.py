
def vpmd(vi, dCD):
    g = 9.8

    #maximum height reached
    d = round((vi**2)/(2*g),4)
    print(f'A. Maximum Height Reached: {d}m')

    #time of flight of the object to reach a position opposite to its origin;
    tAC = round((2*vi)/g,4)
    print(f'B. Time of flight of the object to reach opposite of its origin: {tAC}s')

    #total time of flight; and
    discriminant = (vi**2+(2*g*dCD))**0.5
    num = round((-vi) + discriminant,4)
    tCD = round(num / g,4)
   # a = 0.5*g
    #b = vi
    #c = -dCD

    #d = b**2 - 4*a*c

    #rootOne = round((-b + (d**0.5)) / (2*a),4)
    #rootTwo = round((-b + (d**0.5)) / (2*a),4)

    #if rootOne > 0:
    #    tCD = rootOne
    #elif rootTwo > 0:
    #    tCD = rootTwo
    #else: print("Complex Roots:")

    print("C. Total Time of Flight: ")
    #print(f' a = {a}, \n b = {b}, \n c = {c}')
    print(f'tCD = {tCD}s')

    Total = tAC + tCD
    print(f'Total time of flight = {Total}s')

    #end velocity
    vfCD = round(vi + (g*tCD),4)
    print(f'D. End Velocity: {vfCD}m/s downward')

