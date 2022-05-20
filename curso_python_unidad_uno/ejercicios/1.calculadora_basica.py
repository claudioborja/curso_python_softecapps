'''
Calculadora básica
'''
numero_uno = float(input('Ingrese el primer número: '))
numero_dos = float(input('Ingrese el segundo número: '))
operacion = input('Ingrese la operación a realizar: ')

if(operacion == '+'):
    print(numero_uno + numero_dos)
elif(operacion == '-'):
    print(numero_uno - numero_dos)
elif(operacion == '*'):
    print(numero_uno * numero_dos)
elif(operacion == '/'):
    print(numero_uno / numero_dos)
