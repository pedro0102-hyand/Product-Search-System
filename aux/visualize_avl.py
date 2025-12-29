import os
import sys
import matplotlib.pyplot as plt

# Adiciona o diretório raiz ao path para encontrar o pacote src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.avl_tree import AVLTree
from src.dataset import generate_products

def plot_avl_node(node, x, y, dx, ax):
    """
    Desenha a árvore AVL recursivamente.
    """
    if node:
        # Fator de balanceamento para exibir no nó
        balance = node.get_balance()
        
        # Cor do nó: Verde claro para AVL
        ax.add_patch(plt.Circle((x, y), 0.35, color='#98fb98', ec='black', zorder=3))
        
        # Texto: ID do Produto e Fator de Balanceamento (B)
        label = f"ID: {node.key}\nB: {balance:+d}"
        ax.text(x, y, label, ha='center', va='center', fontsize=6, fontweight='bold', zorder=4)

        # Filho à esquerda
        if node.left:
            ax.plot([x, x - dx], [y, y - 1], color='#555555', lw=1.5, zorder=2)
            plot_avl_node(node.left, x - dx, y - 1, dx / 2, ax)

        # Filho à direita
        if node.right:
            ax.plot([x, x + dx], [y, y - 1], color='#555555', lw=1.5, zorder=2)
            plot_avl_node(node.right, x + dx, y - 1, dx / 2, ax)

def save_avl_image(avl, filename="avl_tree.png"):
    if not avl.root:
        print("A árvore AVL está vazia.")
        return

    # Aumentamos o tamanho da figura para árvores balanceadas que tendem a ser largas
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_aspect('equal')
    ax.axis('off')

    # Inicia o desenho (espaçamento horizontal inicial maior para AVL)
    plot_avl_node(avl.root, 0, 0, 10, ax)

    ax.autoscale_view()
    
    os.makedirs('img', exist_ok=True)
    output_path = os.path.join('img', filename)
    
    plt.title(f"Visualização AVL Tree (Auto-Balanceada)\nAltura Real: {avl.get_height()} | Status: {'Balanceada' if avl.is_balanced() else 'Desbalanceada'}", 
              fontsize=14, pad=20)
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Imagem da AVL gerada com sucesso em: {output_path}")

if __name__ == "__main__":
    # Usamos um tamanho de 25 produtos para garantir uma visualização nítida
    # mas que demonstre bem as rotações da AVL
    DATASET_SIZE = 25 
    products = generate_products(DATASET_SIZE)
    
    avl = AVLTree()
    for product in products:
        avl.insert(product["id"], product)
    
    save_avl_image(avl)