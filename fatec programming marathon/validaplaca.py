p = input()
antiga = ['A','N','N','N','N','N']
numerica = ['N','N','N','N','N','N','N']
aa99 = ['L','L','N','N','N','N']
aaa99 = ['L','L','L','N','N','N','N']
mercosul = ['L','L','L','N','L','N','N']

a = ord('A')
z = ord('Z')

zero = ord('0')
nove = ord('9')
invalido = False

ant = True
num = True
aa9 = True
aaa = True
mer = True

if len(p) > 7 or len(p) == 0:
    invalido = True 

for l in range(len(p)):
    if invalido==False:
        if ant:
            if len(p) < 2 or len(p) > 6:
                ant = False
            elif antiga[l] == 'A' and (p[l] != 'A' and p[l] != 'P'):
                ant = False
            elif antiga[l] == 'N' and (ord(p[l]) < zero or ord(p[l]) > nove):
                ant = False
        if num:
            if len(p) > 7:
                num = False
            elif (ord(p[l]) < zero or ord(p[l]) > nove):
                num = False
        if aa9:
            if len(p) != 6:
                aa9 = False
            elif (ord(p[l]) < a or ord(p[l]) > z) and aa99[l]=='L':
                aa9 = False
            elif aa99[l] == 'N' and (ord(p[l]) < zero or ord(p[l]) > nove):
                aa9 = False
        if aaa:
            if len(p) != 7:
                aaa = False
            elif (ord(p[l]) < a or ord(p[l]) > z) and aaa99[l]=='L':
                aaa = False
            elif aaa99[l] == 'N' and (ord(p[l]) < zero or ord(p[l]) > nove):
                aaa = False
        if mer:
            if len(p) != 7:
                mer = False
            elif (ord(p[l]) < a or ord(p[l]) > z) and mercosul[l]=='L':
                mer = False
            elif mercosul[l] == 'N' and (ord(p[l]) < zero or ord(p[l]) > nove):
                mer = False

if invalido:
    print('Placa invalida')
elif ant:
    print('Placa muito antiga')
elif num:
    print('Placa numerica')
elif aa9:
    print('Placa AA-9999')
elif aaa:
    print('Placa AAA-9999')
elif mer:
    print('Placa Mercosul')
else:
    print('Placa invalida')