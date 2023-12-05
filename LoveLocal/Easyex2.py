class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return [None]
    
    result = []
    
    for i in range(len(nums)):
        left_subtrees = sortedArrayToBST(nums[:i])
        right_subtrees = sortedArrayToBST(nums[i+1:])
        
        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(nums[i])
                root.left = left
                root.right = right
                result.append(root)
    
    return result

def printTree(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    

    while result and result[-1] is None:
        result.pop()
    
    return result

nums = [1, 3]
trees = sortedArrayToBST(nums)

for tree in trees:
    output = printTree(tree)
    print(output)
