import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store the color of the node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, pos=(x, y), layer=layer, color=node.color)
        if node.left is not None:
            graph.add_edge(node.val, node.left.val)
            l = 1 / layer
            add_edges(graph, node.left, pos, x-l, y-1, layer+1)
        if node.right is not None:
            graph.add_edge(node.val, node.right.val)
            r = 1 / layer
            add_edges(graph, node.right, pos, x+r, y-1, layer+1)
    return graph

def draw_tree(tree_root):
    graph = nx.DiGraph()
    pos = {}
    tree = add_edges(graph, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'), with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def in_order_traversal(node, colors, counter):
    if node:
        in_order_traversal(node.left, colors, counter)
        node.color = colors[counter[0] % len(colors)]
        counter[0] += 1
        in_order_traversal(node.right, colors, counter)

def pre_order_traversal(node, colors, counter):
    if node:
        node.color = colors[counter[0] % len(colors)]
        counter[0] += 1
        pre_order_traversal(node.left, colors, counter)
        pre_order_traversal(node.right, colors, counter)

# Example usage
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# In-Order Traversal Visualization
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#c4e17f"]
counter = [0]
in_order_traversal(root, colors, counter)
draw_tree(root)

# Pre-Order Traversal Visualization
counter = [0]
pre_order_traversal(root, colors, counter)
draw_tree(root)
