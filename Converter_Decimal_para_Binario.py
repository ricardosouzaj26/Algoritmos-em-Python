def converter_decimal_para_binario(numero):

    if numero < 2:  # Caso base: 0 ou 1
        return str(numero)
    else:
        # Chamada recursiva para os bits mais significativos
        return converter_decimal_para_binario(numero // 2) + str(numero % 2)

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro decimal: "))
            if numero < 0:
                print("\nPor favor, digite um número inteiro não negativo.\n")
                continue
            break
        except ValueError:
            print("\nEntrada inválida. Digite um número inteiro válido.\n")

    binario = converter_decimal_para_binario(numero)
    print(f"O número {numero} em binário é: {binario}")

# Executa o programa apenas se for chamado diretamente
if __name__ == "__main__":
    main()