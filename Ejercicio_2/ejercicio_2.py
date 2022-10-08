#Ejercicio 2
print("---------------------------------------")
print("-----Inversor de numeros Naturales-----")
print("---------------------------------------")
#input
N_invertido=0
N=int(input("Introduce el numero a invertir: "))
Numero=N
#processing
if N>0:
    while N!=0:
        i=N%10
        N=N//10
        N_invertido=(N_invertido+i)*10
else:
    print("El numero ingresado debe ser positivo")
print("el Numero", Numero, " invertido es :" ,N_invertido//10  )
