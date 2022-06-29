import math
a=int(input("kaçıncı asal:"))
liste=[]
for i in range(2,a**2):
    
    b=0
    c=math.ceil(i**(1/2))+1
    if i==2:
        c=0
    for x in range(2,c):


        if i%x==0:
            b=b+1
            break
    if b==0:
        liste.append(i)
    if len(liste)==a:
        break

print(liste[a-1])
