# Função que calcula o IMC (Índice de Massa Corporal)
def calcular_imc(massa, altura):
    imc = massa / (altura ** 2)  # Fórmula do IMC: peso / (altura²)
    return imc

# Função que imprime a tabela de classificação do IMC
def tabela_imc():
    print("\nClassificação do IMC:")
    print("Menor que 18,5      → Magreza")
    print("Entre 18,5 e 24,9   → Normal")
    print("Entre 25,0 e 29,9   → Sobrepeso")
    print("Entre 30,0 e 39,9   → Obesidade")
    print("Maior que 40,0      → Obesidade Grave\n")

# Função que recebe o IMC e retorna a classificação correspondente
def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc <= 24.9:
        return "Normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 39.9:
        return "Obesidade"
    else:
        return "Obesidade Grave"

# Função que garante que o usuário digite um valor válido
def verificar_valor(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor > 0:
                return valor
            else:
                print("Entrada Inválida. O valor inserido deve ser maior que zero.\n")
        except ValueError:
            print("Entrada Inválida. O valor deve ser um numero.\n")

# Programa principal
print("####################Calculadora de IMC####################")
print("\nDescubra seu IMC")

massa = verificar_valor("Peso (em kg):")
altura = verificar_valor("Altura (em m):")
imc = calcular_imc(massa, altura)
classificacao = classificar_imc(imc)

# Exibe a tabela completa de classificação
tabela_imc()

print(f"\nO seu IMC é de {imc:.2f} e se classifica como {classificacao}.\n")