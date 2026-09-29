print("=== SISTEMA DE COLETA DE DADOS ===")
continuar = "s"
while continuar == "s":
    # Coleta os dados do cliente
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    cidade = input("Digite a cidade: ")
    satisfacao = int(input("De 1 a 5, qual sua satisfação com o atendimento? "))

    print("\nDados coletados:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print("Satisfação:", satisfacao)
       # Verifica se o cliente é maior ou menor de idade
    if idade >= 18:
       print("Cliente maior de idade.")
    else:
       print("Cliente menor de idade.")
       
       # Avalia o nível de satisfação do cliente
    if satisfacao >= 4:
       print("Cliente satisfeito.")
    elif satisfacao == 3:
       print("Cliente com satisfação regular.")
    else:
       print("Cliente insatisfeito.")
       
       # Pergunta se o usuário deseja cadastrar outro cliente
    continuar = input("Deseja cadastrar outro cliente? (s/n): ")