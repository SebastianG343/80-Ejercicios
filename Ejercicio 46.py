n1=int(input("Digite un numero n1"))
n2=int(input("Digite un numero n2"))
n3=int(input("Digite un numero n3"))
if n1==n2 or n1==n3 or n2==n3:
    if n1==n2 and n1==3 or n2==n3 and n1==n3:
        print("Los 3 son iguales")
    else:
        print("Solo hay 2 iguales")
else:
    print("No son iguales")
