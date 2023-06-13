def esBisiesto(a):
    if a%100 != 0:
        if a % 4 == 0:
            b = True
        else:
            b = False

    else:
        if a % 400 == 0:
            b = True
        else:
            b = False

    return b

######
aa = int(input("Ingrese año"))

print("Es bisiesto: ", esBisiesto(aa))
