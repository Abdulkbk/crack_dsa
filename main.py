from src.lists.rotated_list import count_rotations, count_rotations2
from src.tree.BinaryTree import TreeNode


def main():
    # case = [4, 5, 1, 2, 3]
    # result = count_rotations(nums=case)
    # result2 = count_rotations2(nums=case)
    # print(result)
    # print(result2)
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode(1).parse_tuple(tree_tuple)

    tree.display_keys()

    # tree.


if __name__ == "__main__":
    main()
