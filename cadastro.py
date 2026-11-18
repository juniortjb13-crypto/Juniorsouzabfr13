
from datetime import date


def cadastrar_cliente():
    """Coleta e valida os dados de uma avaliação."""

    print("\n=== NOVO CADASTRO ===")

    # Validação do nome
    while True:
        nome = input("Nome do cliente: ").strip()

        if nome:
            break

        print("O nome não pode ficar vazio.")

    # Validação da idade
    while True:
        try:
            idade = int(input("Idade do cliente: "))

            if idade > 0:
                break

            print("A idade deve ser maior que zero.")

        except ValueError:
            print("Digite uma idade válida.")

    # Validação da cidade
    while True:
        cidade = input("Cidade: ").strip()

        if cidade:
            break

        print("A cidade não pode ficar vazia.")

    # Validação da nota
    while True:
        try:
            nota = int(input("Satisfação (1 a 5): "))

            if 1 <= nota <= 5:
                break

            print("A nota deve estar entre 1 e 5.")

        except ValueError:
            print("Digite um número inteiro.")

    data_avaliacao = date.today().isoformat()

    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "nota": nota,
        "data": data_avaliacao
    }


import csv
import os


def salvar_cliente(cliente):
    """Salva um novo cliente no arquivo CSV."""

    arquivo_existe = os.path.exists("clientes.csv")

    with open("clientes.csv", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0, os.SEEK_END)

        tamanho = arquivo.tell()

        if tamanho > 0:
            arquivo.seek(tamanho - 1)
            ultimo_caractere = arquivo.read(1)

            if ultimo_caractere != "\n":
                arquivo.write("\n")

        campos = ["nome", "idade", "cidade", "nota", "data"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if tamanho == 0:
            escritor.writeheader()

        escritor.writerow(cliente)

    print("Cadastro salvo com sucesso!")