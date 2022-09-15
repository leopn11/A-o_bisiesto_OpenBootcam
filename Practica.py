def bisiesto(año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False

año = 2024

print("El,",año,"¿puede ser un año bisiesto?", bisiesto(año))

año = 2022
print("El,",año,"¿puede ser un año bisiesto?", bisiesto(año))

año = 2028
print("El,",año,"¿puede ser un año bisiesto?", bisiesto(año))

año = 2032
print("El,",año,"¿puede ser un año bisiesto?", bisiesto(año))

año = 2005
print("El,",año,"¿puede ser un año bisiesto?", bisiesto(año))