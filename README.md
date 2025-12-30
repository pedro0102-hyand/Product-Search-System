# 🌳 Sistema de Gerenciamento de Produtos com BST e AVL Tree


Sistema de gerenciamento de produtos implementado com **Binary Search Trees (BST)** e **AVL Trees** (árvores auto-balanceadas), demonstrando as diferenças de performance entre estruturas balanceadas e não balanceadas.


## 🎯 Visão Geral

Este projeto implementa um sistema completo de gerenciamento de produtos utilizando árvores binárias de busca, com duas variações:

- **BST Tradicional**: Árvore binária de busca sem balanceamento automático
- **AVL Tree**: Árvore binária de busca auto-balanceada com rotações

O sistema permite **inserção**, **busca**, **remoção** e **filtragem** de produtos, demonstrando as vantagens do balanceamento automático em cenários de alta carga.

## 🌲 Estruturas de Dados

### Binary Search Tree (BST)

Árvore binária onde cada nó segue a propriedade:
- **Subárvore esquerda**: todos os valores menores que o nó atual
- **Subárvore direita**: todos os valores maiores que o nó atual

**Complexidade:**
- Melhor caso: O(log n)
- Pior caso: O(n) - quando degenera em lista encadeada

### AVL Tree

Árvore BST com balanceamento automático através de **rotações**:
- Mantém fator de balanceamento entre -1 e +1
- **Fator de balanceamento** = altura_direita - altura_esquerda

**Tipos de rotações:**
- **RR (Right-Right)**: Rotação simples à esquerda
- **LL (Left-Left)**: Rotação simples à direita
- **RL (Right-Left)**: Rotação dupla (direita + esquerda)
- **LR (Left-Right)**: Rotação dupla (esquerda + direita)

**Complexidade garantida:**
- Todas as operações: O(log n)

## ✨ Funcionalidades

### Operações Básicas
- ✅ **Inserção** de produtos com ID único
- ✅ **Busca** eficiente por ID
- ✅ **Remoção** de produtos
- ✅ **Atualização** de dados (sobrescrita por ID)

### Travessias
- 🔍 **DFS (Depth-First Search)**: Travessia em profundidade usando pilha
- 🌊 **BFS (Breadth-First Search)**: Travessia em largura usando fila

### Filtragem Avançada
- 📦 Filtro por **categoria**
- 💰 Filtro por **preço máximo**
- ⭐ Filtro por **avaliação mínima**
- 🔗 Filtros combinados

### Visualização
- 📊 Geração de imagens das árvores (BST e AVL)
- 📈 Comparação visual de altura e balanceamento

## 🚀 Instalação

### Pré-requisitos

```bash
Python 3.8+
pip (gerenciador de pacotes Python)
```

# Instale as dependências
pip install matplotlib pytest
```

## 💻 Uso

### Exemplo Básico - BST

```python
from src.bst import BinarySearchTree

# Criar árvore
bst = BinarySearchTree()

# Inserir produtos
bst.insert(10, {"name": "Notebook", "price": 2500})
bst.insert(5, {"name": "Mouse", "price": 50})
bst.insert(15, {"name": "Teclado", "price": 150})

# Buscar produto
node = bst.search(10)
print(node.data)  # {'name': 'Notebook', 'price': 2500}

# Remover produto
bst.delete(5)
```

### Exemplo Básico - AVL

```python
from src.avl_tree import AVLTree

# Criar árvore AVL
avl = AVLTree()

# Inserção ordenada (pior caso para BST)
for i in range(1, 100):
    avl.insert(i, f"Produto {i}")

# AVL mantém balanceamento automaticamente
print(f"Altura: {avl.get_height()}")  # ~7 (log₂(100))
print(f"Balanceada: {avl.is_balanced()}")  # True
```

### Filtragem de Produtos

```python
from src.bst import BinarySearchTree
from src.filters import filter_products
from src.dataset import generate_products

# Gerar dataset
products = generate_products(1000)

# Inserir na árvore
bst = BinarySearchTree()
for product in products:
    bst.insert(product["id"], product)

# Filtrar: Eletrônicos até R$ 500 com rating >= 4.0
results = filter_products(
    bst.root,
    category="Eletrônicos",
    max_price=500.0,
    min_rating=4.0
)

print(f"Encontrados: {len(results)} produtos")
for p in results[:5]:
    print(f"- {p['name']}: R$ {p['price']} (⭐ {p['rating']})")
```

### Execução dos Scripts

```bash
# Exemplo básico
python main.py

# Comparação completa BST vs AVL
python aux/main_comparison.py

# Visualizar BST
python aux/visualize_tree.py

# Visualizar AVL
python aux/visualize_avl.py
```

## 🧪 Testes

### Executar Todos os Testes

```bash
pytest
```

### Executar Testes Específicos

```bash
# Testar apenas BST
pytest tests/test_bst.py -v

# Testar apenas AVL
pytest tests/test_avl.py -v

# Testar travessias
pytest tests/test_dfs.py tests/test_bfs.py -v

# Testar filtros
pytest tests/test_filters.py -v
```

### Cobertura de Testes

```bash
pytest --cov=src --cov-report=html
```

## 📊 Performance

### Comparação de Complexidade

| Operação | BST (Melhor) | BST (Pior) | AVL (Sempre) |
|----------|--------------|------------|--------------|
| Inserção | O(log n)     | O(n)       | O(log n)     |
| Busca    | O(log n)     | O(n)       | O(log n)     |
| Remoção  | O(log n)     | O(n)       | O(log n)     |
| Espaço   | O(n)         | O(n)       | O(n)         |


### Quando Usar Cada Estrutura?

**Use BST quando:**
- Dados são inseridos aleatoriamente
- Memória é crítica (sem overhead de altura)
- Atualizações são raras

**Use AVL quando:**
- Ordem de inserção é imprevisível
- Buscas são frequentes
- Precisa garantir O(log n) sempre
- Dados podem chegar ordenados



## 📝 Notas Importantes

### Limitações da BST
- ⚠️ **RecursionError**: Python tem limite de ~1000 recursões. BST degenerada pode estourar stack.
- ⚠️ **Performance imprevisível**: Depende da ordem de inserção.
- ⚠️ **Pior caso comum**: Dados ordenados são comuns em sistemas reais.


⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!