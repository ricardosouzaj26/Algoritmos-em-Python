def main():

    # Primeira entrada do usuário
    entrada = input("Digite um número (ou 'q' para sair): ")

    # Caso o usuário queira sair sem digitar nenhum número
    if entrada.lower() == "q":
        print("\nNenhum número foi inserido.")
        return

    # Converte entrada para float e inicializa variáveis
    x = float(entrada)
    media_total = x
    maior = x
    menor = x
    contador = 1

    # Loop para receber números adicionais
    while True:
        entrada = input("Digite outro número (ou 'q' para sair): ")
        if entrada.lower() == "q":
            break
        try:
            x = float(entrada)
        except ValueError:
            print("\nEntrada inválida! Digite um número válido.\n")
            continue

        # Atualiza estatísticas
        contador += 1
        media_total += x
        if x > maior:
            maior = x
        if x < menor:
            menor = x

    media = media_total / contador
    print(f"\nDe todos os {contador} números inseridos:")
    print(f"- Média: {media:.2f}")
    print(f"- Maior: {maior:.2f}")
    print(f"- Menor: {menor:.2f}")


# Executa o programa
if __name__ == "__main__":
    main()
