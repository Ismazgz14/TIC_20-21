'''
1. Escriba una funci�n llamda "multiplicaci�n"
que reciba como argumento cuatro numeros reales
distintos de cero y que vuelva su producto
'''

def multiplicacion():
    acumuladora=1
    print "Introduce un n�mero:"
    for cont in range(1,5):
        print "NUMERO", cont  
        numero=input()
        acumuladora=acumuladora*numero
    print "PRODUCTO=", acumuladora 

multiplicacion()
