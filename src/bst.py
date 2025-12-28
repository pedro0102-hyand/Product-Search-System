from src.node import Node

class BynarySearchTree:

    def __init__(self):
        self.root = None # Árvore está inicialmente vazia quando criada
    
    def insert(self, key, data):
        self.root = self._insert_recursive(self.root, key, data)
    
    def _insert_recursive(self, node, key, data):

        if node is None:
            return Node(key, data)
        
        if key < node.key :
            node.left = self._insert_recursive(node.left, key, data)
        
        elif key > node.key :
            node.right = self._insert_recursive(node.right, key, data)
        
        return None
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):

        if node is None or node.key == key : # retorna caso o vertice encontrado seja o escolhido
            return node
        
        if key < node.key : #vasculhar a arvore buscando o valor de acordo com o tamanho da chave
            return self._search_recursive(node.left, key)
        
        return self._search_recursive(node.right, key)

        
