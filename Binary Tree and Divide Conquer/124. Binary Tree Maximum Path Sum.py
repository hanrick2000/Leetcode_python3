题目：
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6


#05/01/2020
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
brute force
find all paths in the tree
time?? space: O(1)

optimize
use divide and conquer
1. definition
maxPathSum(root)
2. rules
use gloable variable to record the max sum -> self.max_sum
compare (self.max_sum, left + root, right + root, root, left + right + root) to get a max sum for curt root -> new self.max_sum
3. return 
max(left + root, right + root, root, 0)
4. base case
not root, return 0

time: O(n), space: O(1)
'''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_sum = -float('inf')
        self.helper(root)
        
        return self.max_sum
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.max_sum = max(self.max_sum, left + root.val, right + root.val, root.val, left + right + root.val)
        
        return max(left + root.val, right + root.val, root.val, 0)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
code:
Version 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        #在root这个点得到最大值,与5个值做比较
        #1. 与self.res自己做比较
        #2. 与左边+root做比较,即左边线
        #3. 与右边+root做比较,即右边线
        #4. 与全部做比较,即从左边线到右边线的所有和
        #5. 与root自己比较,因为存在左右两条边线的值都为负数的情况,这样返回root的值才是当前最大
        self.res = max(self.res, left + right + root.val, left + root.val, right + root.val, root.val)
        
        #返回值相当于又要往上走,因此只用返回一条边线即可,因为存在左右两条边线的值都为负数的情况,因此还得与root自己比较
        return max(left + root.val, right + root.val, root.val)
       
       
       
       
       
       
       
       
Version 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        
        self.helper(root)
        
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left_max = self.helper(root.left)
        right_max = self.helper(root.right)
        
        
        self.res = max(self.res, left_max + right_max + root.val)
        
        curt = max(left_max, right_max) + root.val
        
        return max(curt, 0)
