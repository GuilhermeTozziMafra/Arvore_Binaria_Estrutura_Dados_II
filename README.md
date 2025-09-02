# Arvore_Binaria_Estrutura_Dados_II
### Turma: CC6M
### Integrantes: David Helmer Candido
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Atividade de Laboratório - Explorando Árvores Binárias com Manipulação Dinâmica e Classificação Estrutural**
### *Objetivos:*
### - Implementar uma estrutura de árvore binária com operações de inserção e classificação automática.
### - Criar algoritmos para identificar e classificar a árvore como:
### > **Perfeita** <
### > **Completa** <
### > **Regular** <
### > **Balanceada** <
### > **Desbalanceada** <
### - Praticar lógica recursiva e estrutura de dados em Python.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## **Descrição da Atividade**
### Você criará um pequeno **sistema interativo** em Pyhton que permitirá ao usuário:

1. Inserir valores em uma árvore binária (não necessariamente de busca).
2. Visualizar as travessias **in-order**, **pré-ordem**, **pós-ordem** e **nível por nível**.
3. **Classificar dinamicamente** a árvore com base nasdefinições:
  - **Perfeita**
  - **Completa**
  - **Regular**
  - **Balanceada**
  - **Desbalanceada**

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Requisitos do Sistema**
### 1. **Classe** node **e** BinaryTree
### Implemente as duas classes principais: 
```
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert_level_order(self, data): #Inserção automática por nível 
  # A ser implementada
  pass

  def inorder (self, node):
    # A ser implementada
    pass

  def preorder (self, mode):
    # A ser implementada
    pass

  def postorder (self, node):
    # A ser implementada
    pass

  def level_order(self):
    # A ser implementada
    pass

  def is_perfect (self):
    # Retorne True se a árvore for completa
    pass

  def is_regular (self):
    # Retorna True se a árvore for completa
    pass

  def is_coomplete (self):
  # Retorna True se todos os nós tiverem 0 ou 2 filhos pss
    
