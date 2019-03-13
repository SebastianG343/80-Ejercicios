v=int(input("¿Cuanto es el precio de la venta?"))
iva=v*0.19
if v>150000:
    d=v*5/100
    dsc=d-v
    print("IVA:",iva,"descuento:",dsc)
else:
    print("IVA:",iva)
    


        
        

        
