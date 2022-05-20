'''
Operadores lógicos

    and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
    or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se cumplen.
    not ( no): invierte el valor de una variable, dando el valor contrario al de la variable evaluada.

'''

estudia = True
trabaja = False

print(estudia and trabaja) 
print(estudia or trabaja)
print(not estudia)
print(not trabaja)
print(estudia and not trabaja)
print(estudia or not trabaja)
print(not estudia and not trabaja)
