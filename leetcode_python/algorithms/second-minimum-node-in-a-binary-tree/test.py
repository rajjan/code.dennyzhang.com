#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
##    ,-----------
##    | Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
##    | 
##    | Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
##    | 
##    | If no such second minimum value exists, output -1 instead.
##    | 
##    | Example 1:
##    | Input: 
##    |     2
##    |    / \
##    |   2   5
##    |      / \
##    |     5   7
##    | 
##    | Output: 5
##    | Explanation: The smallest value is 2, the second smallest value is 5.
##    | Example 2:
##    | Input: 
##    |     2
##    |    / \
##    |   2   2
##    | 
##    | Output: -1
##    | Explanation: The smallest value is 2, but there isn't any second smallest value.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Idea: pre-order DFS
        return self._findSecondMinimumValue(root, root.val)

    def _findSecondMinimumValue(self, root, firstMininumValue):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            if root.val > firstMininumValue:
                return root.val
            else:
                return -1

        if root.val > firstMininumValue:
            return root.val
        else:
            left_ret, right_ret, ret = -1, -1, -1
            if root.left:
                left_ret = self._findSecondMinimumValue(root.left, firstMininumValue)
            if root.right:
                right_ret = self._findSecondMinimumValue(root.right, firstMininumValue)
            if left_ret == -1 or right_ret == -1:
                ret = max(left_ret, right_ret)
            else:
                ret = min(left_ret, right_ret)
            return ret
