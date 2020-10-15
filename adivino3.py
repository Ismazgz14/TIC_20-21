'''
Dime un numero al azar entre 1 y 10 y lo adivino
'''
import random
def adivino3():
    maxn=10
    numero =random.randint(1,maxn)
    intento=input("Intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande" 
        if intento<numero:
             print "Demasiado pequeño"
        intento=input("Intentalo: ")    
    print "Ahora has acertado"
    
adivino3()
