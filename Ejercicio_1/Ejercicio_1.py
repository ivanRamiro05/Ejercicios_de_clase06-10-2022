print("-------------------------------------")
print("----------SUMA DE DIGITOS------------")
print("-------------------------------------")
#INPUT 

N=int(input("Ingresa un numero positivo : "))
suma_de_digitos= 0
#processing
if N>0:
    while N!=0:
        i=N%10
        N=N//10
        suma_de_digitos = suma_de_digitos + i
else:
    print("tu numero debe ser positivo")
print( suma_de_digitos ) 
