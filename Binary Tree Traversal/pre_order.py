def pre_order(node):
    if node:
        result = [node.data]
        left = pre_order(node.left)
        right = pre_order(node.right)
        result.extend(left)
        result.extend(right)
        return result
    return []

def in_order(node):
    if node:
        result = []
        left = in_order(node.left)
        right = in_order(node.right)
        result.extend(left)
        result.append(node.data)
        result.extend(right)
        return result
    return []

def post_order(node):
    if node:
        result = []
        left = post_order(node.left)
        right = post_order(node.right)
        result.extend(left)
        result.extend(right)
        result.append(node.data)
        return result
    return []
