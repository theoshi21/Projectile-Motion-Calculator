
def vpm(vi,T):
    g = 9.8

    #maximum height reached
    dAB = round((vi**2)/(2*g),4)
    print(f'A. Maximum Height Reached: {dAB} m')

    #time of flight of the object top reach a position opposite to its origin
    tAC = round((2*vi/g),4)
    print(f'B. Time of flight of the object to reach opposite of its origin:')
    print(f'tAC = {tAC}s')
    tCD = round((T-tAC),4)
    print(f'tCD = Total Time - tAC = {tCD}s')

    #height of the elevation; and
    dCD = round((vi*tCD) + ((g*tCD**2)/2),4)
    print(f'C. Height of the elevation: {dCD}m downward')

    #end velocity
    vfCD = round((vi+(g*tCD)),4)
    print(f'D. End Velocity: {vfCD}m/s downward')

def pm(vi,g):

    t = round((vi / g), 4)
    print(f'Time: {t}s')

    d = round((vi ** 2) / (2 * g))
    print(f'Maximum Height: {round(d, 4)}m')

    Total = float(2) * t
    print(f'Total Time: {round(Total, 4)}s')

    vr = str(vi) + "m/s downward"
    print(f'Returning Velocity: {vr}')
