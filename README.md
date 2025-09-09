# Arvore_Binaria_Estrutura_Dados_II
### Turma: CC6M
### Integrantes: David Helmer Candido
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Respostas às Perguntas

## 1. O que muda na estrutura da árvore quando inserimos os valores em ordem crescente?

Quando inserimos valores em uma árvore binária usando o método `insert_level_order` (inserção por nível), a ordem de inserção crescente (por exemplo, 1, 2, 3, 4, 5, 6) não afeta a estrutura da árvore da mesma forma que afetaria uma Árvore Binária de Busca (BST). 

No método `insert_level_order`, os nós são adicionados no primeiro espaço disponível, da esquerda para a direita, nível por nível. Isso significa que a árvore sempre tentará manter uma estrutura o mais completa possível, preenchendo os níveis sequencialmente. Independentemente da ordem dos valores, o primeiro valor será a raiz, o segundo será o filho esquerdo da raiz, o terceiro o filho direito da raiz, e assim por diante, preenchendo os nós de cima para baixo e da esquerda para a direita. 

Portanto, a inserção em ordem crescente resultará em uma árvore que se assemelha a uma árvore binária completa, onde os nós são preenchidos de forma sistemática, sem se preocupar com a propriedade de ordenação (valores menores à esquerda, maiores à direita) que é característica de uma BST.

## 2. Por que a árvore resultante não é perfeita?

Uma árvore binária perfeita é aquela em que todos os níveis estão completamente preenchidos. Isso significa que, para uma árvore de altura `h`, o número total de nós deve ser `2^h - 1`. 

No exemplo dado, inserimos os valores `[1, 2, 3, 4, 5, 6]`. Vamos analisar a estrutura resultante:

- **Nível 0:** 1 (raiz)
- **Nível 1:** 2 (filho esquerdo de 1), 3 (filho direito de 1)
- **Nível 2:** 4 (filho esquerdo de 2), 5 (filho direito de 2), 6 (filho esquerdo de 3)

Para que esta árvore fosse perfeita, o Nível 2 precisaria ter todos os seus nós preenchidos. O nó 3 deveria ter um filho direito (o sétimo nó da árvore). Como inserimos apenas 6 valores, o último nó (o filho direito de 3) está faltando. 

Consequentemente, a árvore não é perfeita porque o último nível (Nível 2) não está completamente preenchido. Ela é uma árvore completa, pois todos os níveis estão preenchidos, exceto o último, que está preenchido da esquerda para a direita, mas não é perfeita por não ter todos os seus níveis totalmente cheios.




# Análise de Complexidade de Tempo e Espaço do `main.py`

## Complexidade de Tempo

A complexidade de tempo é uma medida de quanto tempo um algoritmo leva para ser executado em função do tamanho da entrada. Para uma árvore binária com `N` nós e altura `H`:

*   **`insert_level_order(data)`**: O método de inserção por nível utiliza uma travessia em largura (BFS) para encontrar o próximo local disponível. No pior caso, ele pode visitar todos os `N` nós da árvore para encontrar o local de inserção. Portanto, a complexidade de tempo é **O(N)**.

*   **`inorder(node)`, `preorder(node)`, `postorder(node)`**: As travessias recursivas (em ordem, pré-ordem, pós-ordem) visitam cada nó da árvore exatamente uma vez. Assim, a complexidade de tempo para cada uma é **O(N)**.

*   **`level_order()`**: A travessia em ordem de nível também visita cada nó da árvore exatamente uma vez, utilizando uma fila. A complexidade de tempo é **O(N)**.

*   **`_get_height(node)`**: Este método recursivo visita cada nó na subárvore para determinar a altura. No pior caso (árvore desbalanceada), ele pode visitar todos os `N` nós. A complexidade de tempo é **O(N)**.

*   **`_get_node_count(node)`**: Similar ao `_get_height`, este método visita cada nó para contá-los. A complexidade de tempo é **O(N)**.

*   **`is_perfect()`**: Depende de `_get_height` e `_get_node_count`, ambos O(N). Portanto, a complexidade é **O(N)**.

*   **`is_complete()`**: Utiliza uma travessia em largura que visita cada nó uma vez. A complexidade de tempo é **O(N)**.

*   **`is_regular()`**: Utiliza uma travessia em largura que visita cada nó uma vez. A complexidade de tempo é **O(N)**.

*   **`is_balanced()`**: A função auxiliar `_check_balance` visita cada nó da árvore uma vez. Para cada nó, ela realiza operações constantes. Portanto, a complexidade de tempo é **O(N)**.

*   **`is_unbalanced()`**: Simplesmente chama `is_balanced()`, então a complexidade é **O(N)**.

*   **`print_tree(node)`**: Este método recursivo visita cada nó da árvore para imprimi-lo. A complexidade de tempo é **O(N)**.

## Complexidade de Espaço

A complexidade de espaço é uma medida da quantidade de memória que um algoritmo utiliza em função do tamanho da entrada. Para uma árvore binária com `N` nós e altura `H`:

*   **`Node` e `BinaryTree` classes**: O espaço ocupado para armazenar a árvore é proporcional ao número de nós. Cada nó armazena `data`, `left` e `right`. Portanto, a complexidade de espaço para a estrutura da árvore é **O(N)**.

*   **`insert_level_order(data)`**: O `deque` (fila) pode armazenar até `W` nós no pior caso, onde `W` é a largura máxima da árvore. No pior caso (árvore completa), `W` pode ser `N/2`. Portanto, a complexidade de espaço auxiliar é **O(N)**.

*   **`inorder(node)`, `preorder(node)`, `postorder(node)`**: As travessias recursivas usam a pilha de chamadas do sistema. No pior caso (árvore desbalanceada, como uma lista encadeada), a profundidade da recursão pode ser `H`. No pior caso, `H` pode ser `N`. Portanto, a complexidade de espaço auxiliar é **O(H)**, que pode ser **O(N)** no pior caso.

*   **`level_order()`**: O `deque` (fila) pode armazenar até `W` nós no pior caso, onde `W` é a largura máxima da árvore. No pior caso (árvore completa), `W` pode ser `N/2`. Portanto, a complexidade de espaço auxiliar é **O(N)**.

*   **`_get_height(node)`**, **`_get_node_count(node)`**, **`is_perfect()`**, **`is_balanced()`**, **`print_tree(node)`**: Estes métodos recursivos também usam a pilha de chamadas. No pior caso, a profundidade da recursão pode ser `H`. Portanto, a complexidade de espaço auxiliar é **O(H)**, que pode ser **O(N)** no pior caso.

*   **`is_complete()`**, **`is_regular()`**: Utilizam um `deque` que pode armazenar até `W` nós. A complexidade de espaço auxiliar é **O(N)**.

Em resumo, a maioria das operações tem uma complexidade de tempo e espaço de **O(N)** no pior caso, onde `N` é o número de nós na árvore. Isso ocorre porque, em muitos casos, é necessário visitar ou armazenar uma porção significativa da árvore para realizar a operação.
