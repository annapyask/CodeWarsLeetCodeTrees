class Solution:
    def minimal(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root, key: int):
        if not root:
            return root
        
        cur = None
        current = root

        while current and current.val != key:
            cur = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        if not current:
            return root

        if not current.left or not current.right:
            if not current.left:
                child = current.right
            else:
                child = current.left

            if not cur:
                return child

            if cur.left == current:
                cur.left = child
            else:
                cur.right = child
        else:
            next_ = self.minimal(current.right)
            current.val = next_.val
            current.right = self.deleteNode(current.right, next_.val)
        return root
