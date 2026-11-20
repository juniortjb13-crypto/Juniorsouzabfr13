
import csv
import json
import matplotlib.pyplot as plt

from fila import FilaAtendimento
from arvore import ArvoreBusca


def carregar_dados():
    """Carrega os dados dos clientes a partir do CSV."""
    clientes = []

    try:
        with open("clientes.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            clientes = list(leitor)
    except FileNotFoundError:
        return []

    return clientes


def calcular_media_clientes(clientes):
    """Calcula a média geral das notas."""
    if not clientes:
        return 0

    notas = [int(cliente["nota"]) for cliente in clientes]
    return round(sum(notas) / len(notas), 2)


def calcular_kpis(clientes):
    """Classifica os clientes por nível de satisfação."""
    satisfeitos = 0
    regulares = 0
    insatisfeitos = 0

    for cliente in clientes:
        nota = int(cliente["nota"])

        if nota >= 4:
            satisfeitos += 1
        elif nota == 3:
            regulares += 1
        else:
            insatisfeitos += 1

    return satisfeitos, regulares, insatisfeitos


def calcular_media_por_mes(clientes):
    """Calcula a média de satisfação de cada mês."""
    notas_mensais = {}

    for cliente in clientes:
        mes = cliente["data"][:7]
        nota = int(cliente["nota"])

        if mes not in notas_mensais:
            notas_mensais[mes] = []

        notas_mensais[mes].append(nota)

    medias = {}

    for mes, notas in sorted(notas_mensais.items()):
        medias[mes] = round(sum(notas) / len(notas), 2)

    return medias


def salvar_relatorio(dados):
    """Salva os indicadores no arquivo JSON."""
    with open("relatorio.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def obter_indicadores():
    """Disponibiliza os indicadores para a interface gráfica."""
    clientes = carregar_dados()

    satisfeitos, regulares, insatisfeitos = calcular_kpis(clientes)
    medias_mensais = calcular_media_por_mes(clientes)

    media = calcular_media_clientes(clientes)

    return {
        "total_clientes": len(clientes),
        "media_satisfacao": media,
        "satisfeitos": satisfeitos,
        "regulares": regulares,
        "insatisfeitos": insatisfeitos,
        "media_mensal": medias_mensais
    }


def gerar_graficos():
    """Gera os gráficos de satisfação dos clientes."""
    dados = obter_indicadores()

    categorias = ["Satisfeitos", "Regulares", "Insatisfeitos"]

    quantidades = [
        dados["satisfeitos"],
        dados["regulares"],
        dados["insatisfeitos"]
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, quantidades)
    plt.title("Satisfação dos Clientes")
    plt.xlabel("Categorias")
    plt.ylabel("Quantidade de Clientes")
    plt.tight_layout()
    plt.savefig("grafico_satisfacao.png")
    plt.close()

    meses = list(dados["media_mensal"].keys())
    valores = list(dados["media_mensal"].values())

    plt.figure(figsize=(8, 5))
    plt.plot(meses, valores, marker="o", linewidth=2, label="Média mensal")
    plt.axhline(y=3, linestyle="--", label="Meta de satisfação")
    plt.title("Evolução da Satisfação Mensal")
    plt.xlabel("Mês")
    plt.ylabel("Média de Satisfação")
    plt.ylim(0, 5)
    plt.grid(True)
    plt.legend()

    for i, valor in enumerate(valores):
        plt.text(i, valor + 0.1, str(valor), ha="center")

    plt.tight_layout()
    plt.savefig("grafico_mensal.png")
    plt.close()


def processar_estruturas():
    """Demonstra o uso da fila e da árvore binária."""
    clientes = carregar_dados()

    fila = FilaAtendimento()

    for cliente in clientes:
        fila.adicionar(cliente["nome"])

    arvore_notas = ArvoreBusca()

    for cliente in clientes:
        arvore_notas.inserir(int(cliente["nota"]))

    return {
        "clientes_na_fila": fila.tamanho(),
        "total_atendidos": fila.total_atendidos(),
        "arvore_notas": arvore_notas
    }


def executar_dashboard():
    """Executa o dashboard no terminal e salva o relatório."""
    print("=== DASHBOARD CONECTAMAIS ===")

    clientes = carregar_dados()
    indicadores = obter_indicadores()

    estruturas = processar_estruturas()

    print("Quantidade de clientes:", indicadores["total_clientes"])
    print("Média de satisfação:", indicadores["media_satisfacao"])
    print("Satisfeitos:", indicadores["satisfeitos"])
    print("Regulares:", indicadores["regulares"])
    print("Insatisfeitos:", indicadores["insatisfeitos"])
    print("Média mensal:", indicadores["media_mensal"])

    print("Clientes na fila:", estruturas["clientes_na_fila"])

    salvar_relatorio(indicadores)
    gerar_graficos()

    print("Relatório salvo com sucesso!")
    print("Gráficos gerados com sucesso!")


if __name__ == "__main__":
    executar_dashboard()


import csv
import json
import matplotlib.pyplot as plt

from fila import FilaAtendimento
from arvore import ArvoreBusca


def carregar_dados():
    """Carrega os dados dos clientes a partir do CSV."""
    clientes = []

    try:
        with open("clientes.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            clientes = list(leitor)
    except FileNotFoundError:
        return []

    return clientes


def calcular_media_clientes(clientes):
    """Calcula a média geral das notas."""
    if not clientes:
        return 0

    notas = [int(cliente["nota"]) for cliente in clientes]
    return round(sum(notas) / len(notas), 2)


def calcular_kpis(clientes):
    """Classifica os clientes por nível de satisfação."""
    satisfeitos = 0
    regulares = 0
    insatisfeitos = 0

    for cliente in clientes:
        nota = int(cliente["nota"])

        if nota >= 4:
            satisfeitos += 1
        elif nota == 3:
            regulares += 1
        else:
            insatisfeitos += 1

    return satisfeitos, regulares, insatisfeitos


def calcular_media_por_mes(clientes):
    """Calcula a média de satisfação de cada mês."""
    notas_mensais = {}

    for cliente in clientes:
        mes = cliente["data"][:7]
        nota = int(cliente["nota"])

        if mes not in notas_mensais:
            notas_mensais[mes] = []

        notas_mensais[mes].append(nota)

    medias = {}

    for mes, notas in sorted(notas_mensais.items()):
        medias[mes] = round(sum(notas) / len(notas), 2)

    return medias


def salvar_relatorio(dados):
    """Salva os indicadores no arquivo JSON."""
    with open("relatorio.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def obter_indicadores():
    """Disponibiliza os indicadores para a interface gráfica."""
    clientes = carregar_dados()

    satisfeitos, regulares, insatisfeitos = calcular_kpis(clientes)
    medias_mensais = calcular_media_por_mes(clientes)

    media = calcular_media_clientes(clientes)

    return {
        "total_clientes": len(clientes),
        "media_satisfacao": media,
        "satisfeitos": satisfeitos,
        "regulares": regulares,
        "insatisfeitos": insatisfeitos,
        "media_mensal": medias_mensais
    }


def gerar_graficos():
    """Gera os gráficos de satisfação dos clientes."""
    dados = obter_indicadores()

    categorias = ["Satisfeitos", "Regulares", "Insatisfeitos"]

    quantidades = [
        dados["satisfeitos"],
        dados["regulares"],
        dados["insatisfeitos"]
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, quantidades)
    plt.title("Satisfação dos Clientes")
    plt.xlabel("Categorias")
    plt.ylabel("Quantidade de Clientes")
    plt.tight_layout()
    plt.savefig("grafico_satisfacao.png")
    plt.close()

    meses = list(dados["media_mensal"].keys())
    valores = list(dados["media_mensal"].values())

    plt.figure(figsize=(8, 5))
    plt.plot(meses, valores, marker="o", linewidth=2, label="Média mensal")
    plt.axhline(y=3, linestyle="--", label="Meta de satisfação")
    plt.title("Evolução da Satisfação Mensal")
    plt.xlabel("Mês")
    plt.ylabel("Média de Satisfação")
    plt.ylim(0, 5)
    plt.grid(True)
    plt.legend()

    for i, valor in enumerate(valores):
        plt.text(i, valor + 0.1, str(valor), ha="center")

    plt.tight_layout()
    plt.savefig("grafico_mensal.png")
    plt.close()


def processar_estruturas():
    """Demonstra o uso da fila e da árvore binária."""
    clientes = carregar_dados()

    fila = FilaAtendimento()

    for cliente in clientes:
        fila.adicionar(cliente["nome"])

    arvore_notas = ArvoreBusca()

    for cliente in clientes:
        arvore_notas.inserir(int(cliente["nota"]))

    return {
        "clientes_na_fila": fila.tamanho(),
        "total_atendidos": fila.total_atendidos(),
        "arvore_notas": arvore_notas
    }


def executar_dashboard():
    """Executa o dashboard no terminal e salva o relatório."""
    print("=== DASHBOARD CONECTAMAIS ===")

    clientes = carregar_dados()
    indicadores = obter_indicadores()

    estruturas = processar_estruturas()

    print("Quantidade de clientes:", indicadores["total_clientes"])
    print("Média de satisfação:", indicadores["media_satisfacao"])
    print("Satisfeitos:", indicadores["satisfeitos"])
    print("Regulares:", indicadores["regulares"])
    print("Insatisfeitos:", indicadores["insatisfeitos"])
    print("Média mensal:", indicadores["media_mensal"])

    print("Clientes na fila:", estruturas["clientes_na_fila"])

    salvar_relatorio(indicadores)
    gerar_graficos()

    print("Relatório salvo com sucesso!")
    print("Gráficos gerados com sucesso!")


if __name__ == "__main__":
    executar_dashboard()
