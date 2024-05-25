n = input()
cont = 0
i=2
for i in range(2,int(n)):
    
    if int(n)%i==0:
        cont+=1
if(cont==1):
    print('sim')
else:
    print('nao')