
# Leetcode: Circular Array Loop     :BLOG:Amusing:

---

Circular Array Loop  

---

Similar Problems:  

-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring),  [#game](https://code.dennyzhang.com/tag/game),  [#backtracking](https://code.dennyzhang.com/tag/backtracking)

---

You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.  

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.  

Example 2: Given the array [-1, 2], there is no loop.  

Note: The given array is guaranteed to contain no element "0".  

Can you do it in O(n) time complexity and O(1) space complexity?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/circular-array-loop)  

Credits To: [leetcode.com](https://leetcode.com/problems/circular-array-loop/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/circular-array-loop
    ## Basic Ideas: Loop from left to right
    ##        We mark dead end as 0
    ##        For each node, we keep going.
    ##        It stops, when they go into different directions or hit a dead end
    ##        If true, backtracking and mark all previous nodes as dead end
    ##        If we visit ourself again, it's loop
    ##
    ## Note: The loop don't have to start with the first element
    ##
    ## Sample Data: [1, -1] can't be a valid loop. 
    ##      Yes, it has 2 elements. But it should have only one direction. "forward" or "backward"
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def circularArrayLoop(self, nums):
    	"""
    	:type nums: List[int]
    	:rtype: bool
    	"""
    	length = len(nums)
    	if length == 0: return False
    
    	for i in range(length):
    	    is_forward = 1 if nums[i]>0 else -1
    	    nums[i] = nums[i]%length
    	    if is_forward == -1 and nums[i] != 0:
    		nums[i] -= length
    
    	for i in range(length):
    	    # skip the checked dead ends
    	    if nums[i] == 0: continue
    	    is_forward = 1 if nums[i]>0 else -1
    	    prev, k = nums[i], (i+nums[i])%length
    
    	    while k!=i and nums[k]!=0 and nums[k]*is_forward>0:
    		prev, k = nums[k], (k+nums[k])%length
    	    if k==i: return True
    	    # backtrack and mark nodes as dead end
    	    prev = -prev
    	    while True:
    		nums[k] = 0
    		prev, k = -nums[prev], (k+prev)%length
    		if k==i: break
    	    nums[i] = 0
    	return False
