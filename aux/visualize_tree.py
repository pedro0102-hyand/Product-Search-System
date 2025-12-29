import os
import sys
import matplotlib.pyplot as plt

# Adiciona o diretório pai ao path para localizar 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bst import BinarySearchTree
from src.dataset import generate_products

def plot_tree(node, x, y, dx, ax):
    """
    Desenha a árvore recursivamente usando matplotlib.
    """
    if node:
        # Desenha o círculo do nó
        ax.add_patch(plt.Circle((x, y), 0.3, color='skyblue', ec='black', zorder=3))
        
        # Texto do nó (ID e Categoria)
        label = f"ID: {node.key}\n{node.data.get('category')[:10]}"
        ax.text(x, y, label, ha='center', va='center', fontsize=7, fontweight='bold', zorder=4)

        # Desenha a aresta para o filho à esquerda
        if node.left:
            ax.plot([x, x - dx], [y, y - 1], color='black', lw=1, zorder=2)
            plot_tree(node.left, x - dx, y - 1, dx / 1.8, ax)

        # Desenha a aresta para o filho à direita
        if node.right:
            ax.plot([x, x + dx], [y, y - 1], color='black', lw=1, zorder=2)
            plot_tree(node.right, x + dx, y - 1, dx / 1.8, ax)

def save_tree_matplotlib(bst, filename="product_tree.png"):
    if not bst.root:
        print("A árvore está vazia.")
        return

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Inicia o desenho a partir da raiz
    # Parâmetros: nó, x_inicial, y_inicial, espaçamento_horizontal_inicial, eixo
    plot_tree(bst.root, 0, 0, 5, ax)

    # Ajusta os limites do gráfico automaticamente
    ax.autoscale_view()
    
    # Garante que a pasta img existe
    os.makedirs('img', exist_ok=True)
    
    output_path = os.path.join('img', filename)
    plt.title(f"Visualização da BST - {filename}", fontsize=15)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ Imagem gerada com Matplotlib em: {output_path}")

if __name__ == "__main__":
    # Reproduzindo a configuração do seu main.py
    DATASET_SIZE = 15
    products = generate_products(DATASET_SIZE) #
    
    bst = BinarySearchTree() #
    for product in products:
        bst.insert(product["id"], product) #
    
    save_tree_matplotlib(bst)