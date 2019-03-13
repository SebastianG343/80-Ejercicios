s=int(input("Digite la cantidad de segundos"))
m=60
h=3600
if s==h:
    print(s,"equivale a 1 hora")
if s<h:
    x=s/m
    xd=s/h
    print(s,"equivale a:",xd,"de hora",x,"minutos")
if s>h and s<7200:
    x=s/m
    xd=s/h
    print(s,"equivalen a:",xd,"de hora",x,"minutos")
if s>7200:
    x=s/m
    xd=s/h
    print(s,"equivalen a;",xd,"de horas",x,"minutos")











