def fatorar(i):
    if i == 1:
        print(f'{i}! =', end=' ')
        return 1
    else:
        print(f"{i}!", end='')
        return fatorar(int(i)-1)*int(i)



def main():
    a = input("Type a number to be fatored: ")
    try:
        int(a)
        b=fatorar(a)
        print(b)
    except Exception as e:
        print(f'\033[31m{str(e)}\033[0m')
        print("An error has occurred\n\033[32mTry again:\033[0m")
        main()



main()