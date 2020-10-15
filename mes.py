'''Me va a pedir el numero del mes'''
def mes():
    abreviaMes="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    numeroMes=input("Introduce mes: ")
    pos=(numeroMes-1)*3
    print("El mes es: ", abreviaMes[pos:pos+2])
mes()
