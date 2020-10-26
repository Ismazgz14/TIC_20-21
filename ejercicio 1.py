'''
1. Escriba una función llamda "multiplicación"
que reciba como argumento cuatro numeros reales
distintos de cero y que vuelva su producto
'''

def multiplicacion():
    acumuladora=1
    print "Introduce un número:"
    for cont in range(1,5):
        print "NUMERO", cont  
        numero=input()
        acumuladora=acumuladora*numero
    print "PRODUCTO=", acumuladora 

multiplicacion()
