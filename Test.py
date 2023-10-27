on= True 
def pedir_unidades():
    unidades=input(f"¿De que a que unidad quieres cambiar?(separadas por una coma): ")
    unidades.split(",")
    uinicial=unidades [0]
    ufinal=unidades[1]


while on:
    print(f"¿Que tipo de unidad quieres convertir?")
    print("1. Divisas")
    print("2. Longitud")
    print ("3. Masa")
    print( "4. Tiempo")
    print("5. Velocidad")
    print( "6. Temperatura")
    print("7. Acabar con el programa")
    conversion= input(f"")

    if conversion== 1:
        pedir_unidades()

    if conversion==2:
        pedir_unidades()

    if conversion==3:
        pedir_unidades()

    if conversion==4:
        pedir_unidades()

    if conversion==5:
        pedir_unidades()

    if conversion==6:
        pedir_unidades()

    if conversion==7:
        break

print(f"Gracias por utilizar nuestros servicios")