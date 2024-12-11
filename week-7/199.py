# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If root is None, return empty list
        if not root:
            return []
        
        # Initialize result and queue
        result = []
        queue = deque([root])
        
        # BFS traversal
        while queue:
            level_size = len(queue)
            
            # Iterate through current level
            for i in range(level_size):
                node = queue.popleft()
                
                # If it's the last node in the level, add to result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add child nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result