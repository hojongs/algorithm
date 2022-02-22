from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_tree_node_as_list(root: TreeNode) -> List[int]:
    m = dict()
    queue = [(root, 0)]
    # iterative way to traverse tree
    while len(queue) > 0:
        node, depth = queue.pop()
        m.setdefault(depth, [])
        if node is None:
            m[depth].append(None)
        else:
            m[depth].append(node.val)
            queue.insert(0, (node.left, depth + 1))
            queue.insert(0, (node.right, depth + 1))
    result = []
    for k in sorted(m.keys()):
        result += m[k]
    return result


# print(
#     convert_tree_node_as_list(
#         TreeNode(
#             1,
#             TreeNode(
#                 2,
#                 right=TreeNode(4)
#             ),
#             TreeNode(3),
#         )
#     )
# )
