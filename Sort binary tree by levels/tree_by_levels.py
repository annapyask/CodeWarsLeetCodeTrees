def tree_by_levels(node):
    if not node:
        return []
    all_nodes = [node]
    lst = []
    while all_nodes:
        current = all_nodes.pop(0)
        if current:
            all_nodes.append(current.left)
            all_nodes.append(current.right)
            lst.append(current.value)
    return lst
