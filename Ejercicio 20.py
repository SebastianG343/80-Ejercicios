s=int(input("Digite la cantidad de segundos"))
h=3600
m=60
if s==h:
    print(s,"segundos equivalen a 1 hora")
if s<h:
    x=s/m
    print(s,"equivale a:",x,"minutos")
else:
    if s>h:
        xd=s/h
        print(s,"equivalen a:",xd,"horas")











