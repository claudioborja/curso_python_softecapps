edad = int(input("Introduce tu edad: "))
if(edad >= 18 and edad <= 65):
    print("Eres mayor de edad y puedes jubilarte")
elif(edad >= 18 and edad > 65):
    print("Eres mayor de edad pero no puedes jubilarte")
elif(edad < 18):
    print("Eres menor de edad")