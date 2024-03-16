from collections import deque
from matplotlib import pyplot as plt

from task4 import array_to_tree, draw_tree, Node


def depth_first_traversal(root):
    if root is None:
        return []
    stack = [root]
    visited = set()
    traversal_order = []
    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return traversal_order


def breadth_first_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    visited = set()
    traversal_order = []
    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            traversal_order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return traversal_order


def color_traversal(traversal_order: list[Node]):
    colors = ['#{:02x}{:02x}{:02x}'.format(
        255 - i * (180 // len(traversal_order)),
        255 - i * (180 // len(traversal_order)),
        255 - i * (180 // len(traversal_order)),
    )
        for i in range(len(traversal_order))]
    for i, (node, color) in enumerate(zip(traversal_order, colors)):
        node.color = color
        node.val = i


if __name__ == '__main__':
    # Приклад масиву для перетворення у купу та побудови дерева
    nums = [4, 10, 3, 5, 1]
    root = array_to_tree(nums)

    # Обхід у глибину
    depth_first = depth_first_traversal(root)
    color_traversal(depth_first)
    draw_tree(root)

    # Обхід у ширину
    breadth_first = breadth_first_traversal(root)
    color_traversal(breadth_first)
    draw_tree(root)
