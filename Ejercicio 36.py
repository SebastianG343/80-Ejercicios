d=int(input("Digite la distancia a recorrer"))
dd=int(input("Digite los dias de estancia"))
p=d*5000
pd=p*15/100
pdd=p-pd
if d>1000 and dd>7:
    print("Precio con descuento incluido:",pdd)
else:
    print("El precio a pagar es:",p)
       
