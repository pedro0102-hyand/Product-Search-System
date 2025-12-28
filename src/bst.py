from src.node import Node

class BinarySearchTree:

    def __init__(self):
        self.root = None # Árvore está inicialmente vazia quando criada
    
    def insert(self, key, data):
        self.root = self._insert_recursive(self.root, key, data)
    
    def _insert_recursive(self, node, key, data):

        if node is None:
            return Node(key, data)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, data)
        
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, data)
        
        return node  # CORREÇÃO: retorna o nó em vez de None
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):

        if node is None or node.key == key: # retorna caso o vertice encontrado seja o escolhido
            return node
        
        if key < node.key: #vasculhar a arvore buscando o valor de acordo com o tamanho da chave
            return self._search_recursive(node.left, key)
        
        return self._search_recursive(node.right, key)
    

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):

        if node is None:
            return node
        
        if key < node.key :
            node.left = self._delete_recursive(node.left, key)
        
        elif key > node.key :
            node.right = self._delete_recursive(node.right, key)
        
        else:

            # caso onde o nó possui um filho ou nenhum filho

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # nó com dois filhos
            # encontrando o sucessor
            sucessor = self._min_value_node(node.right) # menor subárvore a direita

            # copia os dados do sucessor para o vértice
            node.key = sucessor.key
            node.data = sucessor.data

            # removendo o sucessor da subárvore a direita
            node.right = self._delete_recursive(node.right, sucessor.key)

        return node
    
    def _min_value_node(self, node):

        current = node
        while current.left is None :
            current = current.left
        return current




