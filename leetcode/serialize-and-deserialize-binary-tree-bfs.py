# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, ret, cache):
            if not root:
                cache.append('')
                return False
            ret += cache
            ret.append(str(root.val))
            return True

        if not root:
            return ''
        queue = list([root])
        ret = list()
        cache = list()
        while queue:
            node = queue.pop(0)
            if helper(node, ret, cache):
                cache = list()
            if node:
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(ret)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        def helper(i):
            if i>=len(segs) or not segs[i]:
                return None
            return TreeNode(int(segs[i]))


        segs = data.split(',')
        root = TreeNode(int(segs[0]))
        queue = list([root])
        offsets = 1
        while queue:
            node = queue.pop(0)
            if node:
                node.left = helper(offsets)
                queue.append(node.left)
                offsets += 1
                node.right = helper(offsets)
                queue.append(node.right)
                offsets += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))