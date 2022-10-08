#Cajero
X=int(input("Cuanto dinero quieres retirar: "))
Billetes_de_10k=0
Billetes_de_2k=0
Monedas_de_100=0
Billetes_de_10k=X//10000
Billetes_de_10k_dia=0
Monedas_de_100_dia=0
Billetes_de_2k_dia=0
variable_para_2k=Billetes_de_10k*10000
Billetes_de_2k=(X-variable_para_2k)//2000
Variable_para_monedas=(Billetes_de_10k)*10000+(Billetes_de_2k)*2000
Monedas_de_100=(X-Variable_para_monedas)//100

print("Billetes de $10.000" ,Billetes_de_10k)
print("Billetes de $2.000",Billetes_de_2k)
print("Monedas de $100",Monedas_de_100)

while X!=0:
    X=int(input("Cuanto dinero quieres retirar: "))
    Billetes_de_10k_dia=Billetes_de_10k+Billetes_de_10k
    Billetes_de_2k_dia=Billetes_de_2k +Billetes_de_2k
    Monedas_de_100_dia=Monedas_de_100 + Monedas_de_100
    Billetes_de_10k=X//10000
    variable_para_2k=Billetes_de_10k*10000
    Billetes_de_2k=(X-variable_para_2k)//2000
    Variable_para_monedas=(Billetes_de_10k)*10000+(Billetes_de_2k)*2000
    Monedas_de_100=(X-Variable_para_monedas)//100
    print("Billetes de $10.000" ,Billetes_de_10k)
    print("Billetes de $2.000",Billetes_de_2k)
    print("Monedas de $100",Monedas_de_100)
print("Billetes de $10.000 usados en el dia" ,Billetes_de_10k_dia)
print("Billetes de $2.000 usados en el dia" ,Billetes_de_2k_dia)
print("Monedas de 100 usadas en el dia",Monedas_de_100_dia)