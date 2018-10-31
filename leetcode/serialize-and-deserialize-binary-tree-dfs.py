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
        if not root:
            return ''
        def helper(node, ret):
            if not node:
                return ret.append('')
            ret.append(str(node.val))
            helper(node.left, ret)
            helper(node.right, ret)
            return ret
        ret = helper(root, list())
        print(ret)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        def helper(i):
            if not segs[i] or i >= len(segs):
                return None, 1
            root = TreeNode(int(segs[i]))
            offsets = 1
            root.left, offset = helper(i+offsets)
            offsets += offset
            root.right, offset = helper(i+offsets)
            offsets += offset
            return root, offsets
        segs = data.split(',')
        return helper(0)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))