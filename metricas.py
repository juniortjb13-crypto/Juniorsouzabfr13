def classificar_satisfacao(nota):
    """Classifica a satisfação do cliente com base na nota."""
    if nota >= 4:
        return "Cliente satisfeito."
    elif nota == 3:
        return "Cliente com satisfação regular."
    else:
        return "Cliente insatisfeito."
def calcular_media(notas, casas=2):
    """Calcula a média com base nas notas."""
    media = sum(notas) / len(notas)
    return round(media, casas)