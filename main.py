import vpm, vpmd

print("***PROJECTILE MOTION CALCULATOR***")

compute = True

while(compute):

    check = True
    while(check):
        calc = input("Types of Projectile Motion (basic, T, m): ")
        print()

        if calc == "basic":
            check = False
            print("Basic Projectile Motion")
            vi = float(input("Initial Velocity: "))
            g = float(input("Gravity: "))
            vpm.pm(vi ,g)
        elif calc == "T":
            check = False
            print("Vertical Projectile Motion")
            vi = float(input("Initial Velocity: "))
            T = float(input("Total Time: "))
            vpm.vpm(vi,T)
        elif calc == "m":
            check = False
            print("Vertical Projectile Motion using Total Elevation")
            vi = float(input("Initial Velocity (Vi): "))
            dCD = float(input("Height of the elevation (dCD): "))
            vpmd.vpmd(vi,dCD)
        else: print("Invalid. Try again.")

    print()

    go = True
    while(go):
        cont = input("Keep computing? (Y/N): ")

        if cont == "Y" or cont == "y":
            print()
            go = False
        elif cont == "N" or cont == "n":
            print("Thank you for projectile motion calculator.")
            compute = False
            break
        else: print("Invalid. Type Y or N")