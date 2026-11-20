class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)
    def buscar(self, valor):
        atual = self.raiz

        while atual is not None:
            if atual.valor == valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False


arvore = ArvoreBusca()

arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print("Árvore criada com sucesso!")
print("Buscar 7:", arvore.buscar(7))
print("Buscar 20:", arvore.buscar(20))
print("\n--- ANÁLISE DE COMPLEXIDADE ---")
print("Inserção na árvore: O(log n) em média")
print("Busca na árvore: O(log n) em média")
print("Pior caso: O(n)")
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)
    def buscar(self, valor):
        atual = self.raiz

        while atual is not None:
            if atual.valor == valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False


arvore = ArvoreBusca()

arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

print("Árvore criada com sucesso!")
print("Buscar 7:", arvore.buscar(7))
print("Buscar 20:", arvore.buscar(20))
print("\n--- ANÁLISE DE COMPLEXIDADE ---")
print("Inserção na árvore: O(log n) em média")
print("Busca na árvore: O(log n) em média")
print("Pior caso: O(n)")