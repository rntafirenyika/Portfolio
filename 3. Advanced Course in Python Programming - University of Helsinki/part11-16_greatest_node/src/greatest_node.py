class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

# Takes the root node of a binary tree as its argument.
# Returns the node with the greatest value within the tree.
def greatest_node(root: Node):
    g_node = root.value

    if root.left_child is not None:
        left_max = greatest_node(root.left_child)
        if left_max > g_node:
            g_node = left_max

    if root.right_child is not None:
        right_max = greatest_node(root.right_child)
        if  right_max > g_node:
            g_node = right_max

    return g_node
     
if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))