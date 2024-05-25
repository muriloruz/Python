import requests as rqst


def cnv_dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"

    valor = input("Digite o Valor em U$(dolar):")

    response = rqst.get(url)
    try:
        if response.status_code == 200:
            dados = response.json()
            valorHigh = dados['USDBRL']['high']
            valorLow = dados['USDBRL']['low']
            valor_real = (float(valorHigh)+float(valorLow))/2
            resultado = float(valor_real)*float(valor)
            print(f'U${valor}->R${resultado:.2f}')
        else:
            print(f'erro na resposta = {response.status_code}')
    except Exception as e:
        print(f'\033[31mO erro é {e}\033[0m')
        print("\033[32mVoltando para o main:\033[0m")
        main()


def cnv_real():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"

    valor = input("Digite o Valor em R$(real):")

    response = rqst.get(url)
    try:
        if response.status_code == 200:
            dados = response.json()
            valorHigh = dados['USDBRL']['high']
            valorLow = dados['USDBRL']['low']
            valor_real = (float(valorHigh) + float(valorLow)) / 2
            resultado = float(valor) / float(valor_real)
            print(f'R${valor}->U${resultado:.2f}')
        else:
            print(f'erro na resposta = {response.status_code}')
    except Exception as e:
        print(f'\033[31mO erro é {e}\033[0m')
        print("\033[32mVoltando para o main:\033[0m")
        main()


def main():
    opc = input("Digite \"Real\" para converter real para dolar\nDigite \"Dolar\" para "
                "converter dolar para real\n--->")
    opc = opc.lower()

    if opc == "real":
        cnv_real()
    elif opc == "dolar":
        cnv_dolar()
    else:
        print("\033[31mOpcção incorreta!\033[0m")
        main()


main()