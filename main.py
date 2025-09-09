import collections

# Definição da classe Node (Nó da Árvore Binária)
# Cada nó contém um valor (data) e referências para seus filhos esquerdo e direito.
class Node:
    def __init__(self, data):
        self.data = data  # Valor armazenado no nó
        self.left = None  # Referência para o filho esquerdo
        self.right = None # Referência para o filho direito

# Definição da classe BinaryTree (Árvore Binária)
# Gerencia a estrutura da árvore, começando pela raiz.
class BinaryTree:
    def __init__(self):
        self.root = None  # A raiz da árvore, inicialmente None (árvore vazia)

    # Método para inserir um novo nó na árvore em ordem de nível (largura).
    # Garante que a árvore permaneça completa durante a inserção.
    def insert_level_order(self, data):
        new_node = Node(data) # Cria um novo nó com o dado fornecido
        if self.root is None: # Se a árvore estiver vazia, o novo nó se torna a raiz
            self.root = new_node
            return

        # Usa uma fila (deque) para realizar a travessia em largura (BFS).
        # Começa com a raiz na fila.
        q = collections.deque([self.root])
        while q:
            temp = q.popleft() # Pega o primeiro nó da fila

            # Tenta inserir o novo nó como filho esquerdo
            if not temp.left:
                temp.left = new_node
                return
            else:
                q.append(temp.left) # Se o filho esquerdo existe, adiciona-o à fila

            # Tenta inserir o novo nó como filho direito
            if not temp.right:
                temp.right = new_node
                return
            else:
                q.append(temp.right) # Se o filho direito existe, adiciona-o à fila

    # Travessia In-Order (Em Ordem): Esquerda -> Raiz -> Direita
    # Visita os nós em ordem crescente de seus valores (para BSTs).
    def inorder(self, node):
        if node: # Se o nó não for None
            self.inorder(node.left)  # Visita recursivamente a subárvore esquerda
            print(node.data, end=" ") # Processa o nó atual (imprime o dado)
            self.inorder(node.right) # Visita recursivamente a subárvore direita

    # Travessia Pre-Order (Pré-Ordem): Raiz -> Esquerda -> Direita
    # Usada para criar uma cópia da árvore ou para prefixar expressões.
    def preorder(self, node):
        if node: # Se o nó não for None
            print(node.data, end=" ") # Processa o nó atual
            self.preorder(node.left)  # Visita recursivamente a subárvore esquerda
            self.preorder(node.right) # Visita recursivamente a subárvore direita

    # Travessia Post-Order (Pós-Ordem): Esquerda -> Direita -> Raiz
    # Usada para deletar a árvore ou para postfixar expressões.
    def postorder(self, node):
        if node: # Se o nó não for None
            self.postorder(node.left)  # Visita recursivamente a subárvore esquerda
            self.postorder(node.right) # Visita recursivamente a subárvore direita
            print(node.data, end=" ") # Processa o nó atual

    # Travessia Level-Order (Ordem de Nível/Largura): Nível por Nível
    # Visita os nós nível por nível, da esquerda para a direita.
    def level_order(self):
        if not self.root: # Se a árvore estiver vazia, não faz nada
            return

        q = collections.deque([self.root]) # Inicia a fila com a raiz
        while q:
            node = q.popleft() # Pega o primeiro nó da fila
            print(node.data, end=" ") # Processa o nó atual

            if node.left: # Se houver filho esquerdo, adiciona-o à fila
                q.append(node.left)
            if node.right: # Se houver filho direito, adiciona-o à fila
                q.append(node.right)

    # Método auxiliar para calcular a altura de um nó (subárvore).
    def _get_height(self, node):
        if not node: # A altura de um nó None é 0
            return 0
        # A altura é 1 + o máximo das alturas das subárvores esquerda e direita
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    # Método auxiliar para contar o número de nós em uma subárvore.
    def _get_node_count(self, node):
        if not node: # O número de nós em um nó None é 0
            return 0
        # O número de nós é 1 (o próprio nó) + a contagem dos nós nas subárvores
        return 1 + self._get_node_count(node.left) + self._get_node_count(node.right)

    # Verifica se a árvore é perfeita.
    # Uma árvore perfeita tem todos os níveis completamente preenchidos.
    def is_perfect(self):
        h = self._get_height(self.root) # Calcula a altura da árvore
        node_count = self._get_node_count(self.root) # Conta o total de nós
        # Uma árvore perfeita com altura h tem 2^h - 1 nós.
        return node_count == (2**h - 1)

    # Verifica se a árvore é completa.
    # Uma árvore completa tem todos os níveis preenchidos, exceto possivelmente o último,
    # e o último nível é preenchido da esquerda para a direita.
    def is_complete(self):
        if not self.root: # Uma árvore vazia é considerada completa
            return True

        q = collections.deque([self.root]) # Inicia a fila com a raiz
        flag = False # Flag para indicar se encontramos um nó não-cheio
        while q:
            temp = q.popleft() # Pega o primeiro nó da fila

            if temp.left: # Se o nó tem filho esquerdo
                if flag: # Se já encontramos um nó não-cheio antes, a árvore não é completa
                    return False
                q.append(temp.left) # Adiciona o filho esquerdo à fila
            else:
                flag = True # Se não tem filho esquerdo, marca a flag (encontrou um nó não-cheio)

            if temp.right: # Se o nó tem filho direito
                if flag: # Se já encontramos um nó não-cheio antes, a árvore não é completa
                    return False
                q.append(temp.right) # Adiciona o filho direito à fila
            else:
                flag = True # Se não tem filho direito, marca a flag
        return True # Se o loop termina, a árvore é completa

    # Verifica se a árvore é regular.
    # Uma árvore regular é aquela em que cada nó tem 0 ou 2 filhos.
    def is_regular(self):
        if not self.root: # Uma árvore vazia é considerada regular
            return True

        q = collections.deque([self.root]) # Inicia a fila com a raiz
        while q:
            node = q.popleft() # Pega o primeiro nó da fila
            
            # Se um nó tem apenas um filho (esquerdo ou direito), não é regular
            if (node.left and not node.right) or (not node.left and node.right):
                return False
            
            if node.left: # Se houver filho esquerdo, adiciona-o à fila
                q.append(node.left)
            if node.right: # Se houver filho direito, adiciona-o à fila
                q.append(node.right)
        return True # Se o loop termina, a árvore é regular

    # Verifica se a árvore é balanceada.
    # Uma árvore balanceada é aquela em que a diferença de altura entre as subárvores
    # esquerda e direita de qualquer nó não é maior que 1.
    def is_balanced(self):
        # Função auxiliar recursiva para verificar o balanceamento e retornar a altura.
        def _check_balance(node):
            if not node: # Um nó None é balanceado e tem altura 0
                return True, 0

            # Verifica recursivamente a subárvore esquerda
            left_balanced, left_height = _check_balance(node.left)
            if not left_balanced: # Se a subárvore esquerda não for balanceada, a árvore não é
                return False, 0

            # Verifica recursivamente a subárvore direita
            right_balanced, right_height = _check_balance(node.right)
            if not right_balanced: # Se a subárvore direita não for balanceada, a árvore não é
                return False, 0

            # Verifica a diferença de altura entre as subárvores
            if abs(left_height - right_height) <= 1:
                # Se balanceado, retorna True e a altura do nó atual
                return True, 1 + max(left_height, right_height)
            else:
                # Se não balanceado, retorna False
                return False, 0

        # Chama a função auxiliar a partir da raiz da árvore
        balanced, _ = _check_balance(self.root)
        return balanced

    # Verifica se a árvore é desbalanceada.
    # É o oposto de is_balanced().
    def is_unbalanced(self):
        return not self.is_balanced()

    # Método para imprimir a estrutura da árvore no terminal de forma visual.
    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            # Imprime o nó atual com indentação baseada no nível
            print("  " * level + prefix + str(node.data))
            # Se o nó tem filhos, chama recursivamente para os filhos
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L-- ") # Imprime o filho esquerdo
                self.print_tree(node.right, level + 1, "R-- ") # Imprime o filho direito

# Bloco principal de execução do código
if __name__ == "__main__":
    tree = BinaryTree() # Cria uma instância da árvore binária
    values = [1, 2, 3, 4, 5, 6] # Valores a serem inseridos na árvore
    for val in values:
        tree.insert_level_order(val) # Insere cada valor na árvore

    print("In-Order:", end=" ") # Imprime o cabeçalho para a travessia In-Order
    tree.inorder(tree.root) # Realiza a travessia In-Order a partir da raiz
    print() # Nova linha para formatação

    print("Pre-Order:", end=" ") # Imprime o cabeçalho para a travessia Pre-Order
    tree.preorder(tree.root) # Realiza a travessia Pre-Order a partir da raiz
    print() # Nova linha para formatação

    print("Post-Order:", end=" ") # Imprime o cabeçalho para a travessia Post-Order
    tree.postorder(tree.root) # Realiza a travessia Post-Order a partir da raiz
    print() # Nova linha para formatação

    print("Level-Order:", end=" ") # Imprime o cabeçalho para a travessia Level-Order
    tree.level_order() # Realiza a travessia Level-Order
    print() # Nova linha para formatação

    print("\nClassificação da árvore:") # Imprime o cabeçalho para a classificação
    print(f"Completa: {tree.is_complete()}") # Verifica e imprime se a árvore é completa
    print(f"Perfeita: {tree.is_perfect()}") # Verifica e imprime se a árvore é perfeita
    print(f"Regular: {tree.is_regular()}") # Verifica e imprime se a árvore é regular
    print(f"Balanceada: {tree.is_balanced()}") # Verifica e imprime se a árvore é balanceada

    print("\nVisualização da Árvore:") # Imprime o cabeçalho para a visualização
    tree.print_tree(tree.root) # Imprime a estrutura visual da árvore
