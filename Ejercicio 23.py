h=0
m=0
s=int(input("Digite la cantidad de segundos"))
ms=s//60
while ms>0:
    m+=1
    ms-=1
    ss=m*60
    st=s-ss
    if m>=60:
        h+=1
        m=0
    if ms==0:
        break
print("Hora",h,":",m,":",st)




        
