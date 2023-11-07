""" Binary Tree Implementation"""


class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def parse_tuple(self, data):
        if isinstance(data, tuple) and len(data) == 3:
            self = TreeNode(data[1])
            self.left = self.parse_tuple(data[0])
            self.right = self.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return self

    # Display the keys of each node
    def display_keys(self, space="\t", level=0):
        # if the Node is empty
        if self is None:
            print(space * level + "{}")
            return

        # if the self is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # if thr node has children
        self.display_keys(space, level + 1)  # type: ignore
        print(space * level + str(self.key))
        self.display_keys(space, level + 1)  # type: ignore

    # Traversal of a Tree

    def traversal_inorder(self):
        if self is None:
            return []
        return (
            TreeNode.traversal_inorder(self.left)  # type: ignore
            + [self.key]
            + TreeNode.traversal_inorder(self.right)  # type: ignore
        )

    def traversal_preorder(self):
        if self is None:
            return []
        return (
            [TreeNode.key]  # type: ignore
            + TreeNode.traversal_preorder(self.left)  # type: ignore
            + TreeNode.traversal_preorder(self.right)  # type: ignore
        )

    # Height or Depth of a Tree
    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))  # type: ignore

    # Number of nodes
    def tree_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)  # type: ignore
