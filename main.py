
print("=== CONECTAMAIS | SISTEMA DE COLETA DE DADOS ===")

from cadastro import cadastrar_cliente, salvar_cliente
from metricas import classificar_satisfacao, calcular_media


notas = []

while True:
    # Cadastra e valida os dados
    cliente = cadastrar_cliente()

    # Salva os dados no arquivo clientes.csv
    salvar_cliente(cliente)

    # Guarda a nota para calcular as estatísticas
    nota = cliente["nota"]
    notas.append(nota)

    print("\nCadastro concluído!")
    print(classificar_satisfacao(nota))

    continuar = input("\nDeseja cadastrar outro cliente? (s/n): ").strip().lower()

    if continuar != "s":
        break


# Apresenta o resumo estatístico
if notas:
    media = calcular_media(notas)

    print("\n=== RESUMO DAS AVALIAÇÕES ===")
    print("Total de avaliações realizadas:", len(notas))
    print("Média de satisfação:", media)

    if media >= 4:
        print("Avaliação geral: clientes satisfeitos.")
    elif media >= 3:
        print("Avaliação geral: satisfação regular.")
    else:
        print("Avaliação geral: clientes insatisfeitos.")

print("\nSistema encerrado.")
