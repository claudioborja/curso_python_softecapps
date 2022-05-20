edad = int(input("Introduce tu edad: "))
if(edad >= 18):
    print("Eres mayor de edad")
    if(edad >= 65):
        print("Puedes Jubilarte")
    else:
        print("No puedes jubilarte")
else:
    print("Eres menor de edad")
    