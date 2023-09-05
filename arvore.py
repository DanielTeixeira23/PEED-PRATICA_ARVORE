class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)            
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)  

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_raiz(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            print('Raiz:', self.raiz.valor, end=' ')   

    def altura_da_arvore(self):
        if self.raiz is None:
            return 0
        else:
            return self.altura_arvore(self.raiz) - 1

    def altura_arvore(self, no):
        if no is None:
            return 0
        else:
            return max(self.altura_arvore(no.esquerda), self.altura_arvore(no.direita)) + 1

    def mostrar_nos_internos(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_nos_internos_recursivo(self.raiz)

    def mostrar_nos_internos_recursivo(self, no):
        if no is not None:
            if no.esquerda is not None or no.direita is not None:
                print(no.valor, end=' ')
            self.mostrar_nos_internos_recursivo(no.esquerda)
            self.mostrar_nos_internos_recursivo(no.direita)

    def mostrar_as_folhas(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_as_folhas_recursivo(self.raiz)

    def mostrar_as_folhas_recursivo(self, no):
        if no is not None:
            if no.esquerda is None and no.direita is None:
                print(no.valor, end=' ')
            self.mostrar_as_folhas_recursivo(no.esquerda)
            self.mostrar_as_folhas_recursivo(no.direita)
            
    def procurar_nos(self, valor):
        if self.raiz is None:
            return False
        else:
            return self.procurar_nos_na_arvore(self.raiz, valor)
    
    def procurar_nos_na_arvore(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if self.procurar_nos_na_arvore(no.esquerda, valor):
            return True
        if self.procurar_nos_na_arvore(no.direita, valor):
            return True
        
def menu():
    a = ArvoreBinaria()
    
    while True:
        print()
        print("-" * 85)
        print("\t\tMenu")
        print("1. Inserir valores na árvore")
        print("2. Mostrar a raiz da árvore")
        print("3. Mostrar a altura da árvore")
        print("4. Mostrar os nós internos ")
        print("5. Mostrar os nós folhas")
        print("6. Procurar valores na árvore")
        print("7. Sair do programa")
        print()
        print("-" * 85)
        op = input("Escolha uma opção: ")
        
        if op == '1':
            num_values = int(input('Quantos valores deseja inserir? '))
            for j in range(num_values):
                num = int(input(f'Digite o {j+1}º valor: '))
                a.inserir_em_nivel(num)
            print('Valores inseridos com sucesso.')
            a.mostrar_pre_ordem()
        elif op == '2':
            a.mostrar_raiz()
        elif op == '3':
            print('Altura:', a.altura_da_arvore())
        elif op == '4':
            print('Nós Internos:')
            a.mostrar_nos_internos()
        elif op == '5':
            print('Nós Folhas:')
            a.mostrar_as_folhas()
        elif op == '6':
            num_verificar = int(input('Informe um número para verificar se ele está presente na árvore: '))
            if a.procurar_nos(num_verificar):
                print('Número presente na árvore')
            else:
                print('Número não está presente na árvore!')
        elif op == '7':
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()