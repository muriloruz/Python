
linha = input()
vet = list(linha)
a = ord('A')
p = ord('P')
z = ord('Z')
for i in range(len(vet)):
    vet[i] = ord(vet[i])
    for j in range(65,80):
        if vet[0] == j and vet[1] == j and 48 <= vet[2] <= 57:
            print("AAAAAAAAA")
            break
        elif 48 <= vet[i] <= 57:
            print("BBBBBBBBB")
            break
        elif vet[0] == 65 or vet[0] == 80 and vet[i+1].isdigit() and vet[1].isdigit():
            print("CCCCCCCCCCCCCC")
            break
