from src.avl_node import AVLNode


class AVLTree:
    
    def __init__(self):
        self.root = None
    
    def rotate_right(self, z):
      
        y = z.left
        T3 = y.right
        
        # Realizar rotação
        y.right = z
        z.left = T3
        
        # Atualizar alturas
        z.update_height()
        y.update_height()
        
        return y
    
    def rotate_left(self, z):
      
        y = z.right
        T2 = y.left
        
        # Realizar rotação
        y.left = z
        z.right = T2
        
        # Atualizar alturas
        z.update_height()
        y.update_height()
        
        return y
    

    def insert(self, key, data):

        self.root = self._insert_recursive(self.root, key, data)
    
    def _insert_recursive(self, node, key, data):
        # 1. Inserção normal de BST
        if node is None:
            return AVLNode(key, data)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, data)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, data)
        else:
            # Chave duplicada - atualiza os dados
            node.data = data
            return node
        
        # 2. Atualizar altura do nó ancestral
        node.update_height()
        
        # 3. Obter fator de balanceamento
        balance = node.get_balance()
        
        # 4. Se desbalanceado, executar rotações
        
        # Caso Right-Right (RR): direita pesada, inseriu à direita
        if balance > 1 and key > node.right.key:
            return self.rotate_left(node)
        
        # Caso Left-Left (LL): esquerda pesada, inseriu à esquerda
        if balance < -1 and key < node.left.key:
            return self.rotate_right(node)
        
        # Caso Right-Left (RL): direita pesada, mas inseriu à esquerda da direita
        if balance > 1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        # Caso Left-Right (LR): esquerda pesada, mas inseriu à direita da esquerda
        if balance < -1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        return node
    

    def search(self, key):

        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        
        return self._search_recursive(node.right, key)
    
    
    def delete(self, key):

        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        # 1. Remoção normal de BST
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Nó encontrado - remover
            
            # Caso 1: Nó com um filho ou sem filhos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Caso 2: Nó com dois filhos
            # Encontrar o sucessor (menor da subárvore direita)
            successor = self._min_value_node(node.right)
            
            # Copiar dados do sucessor
            node.key = successor.key
            node.data = successor.data
            
            # Remover o sucessor
            node.right = self._delete_recursive(node.right, successor.key)
        
        # 2. Atualizar altura
        node.update_height()
        
        # 3. Obter fator de balanceamento
        balance = node.get_balance()
        
        # 4. Rebalancear se necessário
        
        # Caso Right-Right: direita pesada
        if balance > 1 and node.right.get_balance() >= 0:
            return self.rotate_left(node)
        
        # Caso Right-Left: direita pesada, mas subárvore esquerda mais alta
        if balance > 1 and node.right.get_balance() < 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        # Caso Left-Left: esquerda pesada
        if balance < -1 and node.left.get_balance() <= 0:
            return self.rotate_right(node)
        
        # Caso Left-Right: esquerda pesada, mas subárvore direita mais alta
        if balance < -1 and node.left.get_balance() > 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        return node
    
    def _min_value_node(self, node):

        current = node
        while current.left is not None:
            current = current.left
        return current

    
    def get_height(self):

        return self.root.height if self.root else 0
    
    def is_balanced(self):

        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        
        balance = abs(node.get_balance())
        
        if balance > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))