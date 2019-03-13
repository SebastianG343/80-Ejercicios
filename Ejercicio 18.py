import math
x1=int(input("Digite la cordenada x1"))
y1=int(input("Digite la cordenada y1"))
x2=int(input("Digite la cordenada x2"))
y2=int(input("Digite la cordenada y2"))
if y1==y2:
    xt=(x2-x1)
    print("Distancia:",xt)
else:
    lul=(x2-x1)
    lel=(y2-y1)
    xlul=(lul*lul)
    xlel=(lel*lel)
    lil=(xlul+xlel)
    math.sqrt(lil)
    print("Distancia:",lil)


