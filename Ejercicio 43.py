n1=int(input("Digite un numero n1"))
n2=int(input("Digite un numero n2"))
n3=int(input("Digite un numero n3"))
if n3>n2>n1:
       print("Esta incrementando")
if n1>n2>n3:
       print("Esta disminuyendo")
if n1>n3>n2 or n2>n1>n3 or n2>n3>n1 or n3>n1>n2:
       print("Ni incrementa ni disminuye")
