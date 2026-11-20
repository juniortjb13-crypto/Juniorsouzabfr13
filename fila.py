class FilaAtendimento:
    def __init__(self):
        self.fila = []
        self.atendidos = 0

    def adicionar(self, cliente):
        self.fila.append(cliente)

    def atender(self):
        if len(self.fila) > 0:
            cliente = self.fila.pop(0)
            self.atendidos += 1
            return cliente
        return None

    def tamanho(self):
        return len(self.fila)
    def vazia(self):
        return len(self.fila) == 0
    def proximo(self):
        if len(self.fila) > 0:
           return self.fila[0]
        return None    

    def total_atendidos(self):
        return self.atendidos


if __name__ == "__main__":
    fila = FilaAtendimento()
    print("A fila está vazia?", fila.vazia())
    
    

    fila.adicionar("Carlos")
    fila.adicionar("Mariana")
    fila.adicionar("João")
    fila.atender()
    fila.atender()
    print("A fila está vazia?", fila.vazia())

    print("Tamanho da fila:", fila.tamanho())
    print("Próximo cliente:", fila.proximo())
    print("Cliente atendido:", fila.atender())
    print("Tamanho da fila após atendimento:", fila.tamanho())
    print("Total de atendimentos:", fila.total_atendidos())
    print("A fila está vazia agora?", fila.vazia())