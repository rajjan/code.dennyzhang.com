
# Leetcode: Evaluate Reverse Polish Notation     :BLOG:Basic:

---

Evaluate Reverse Polish Notation  

---

Similar Problems:  

-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)

---

Evaluate the value of an arithmetic expression in Reverse Polish Notation.  

Valid operators are +, -, \*, /. Each operand may be an integer or another expression.  

Some examples:  
  ["2", "1", "<del>", "3", "\*"] -> ((2 + 1) \* 3) -> 9  
  ["4", "13", "5", "/", "</del>"] -> (4 + (13 / 5)) -> 6  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/evaluate-reverse-polish-notation)  

Credits To: [leetcode.com](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/evaluate-reverse-polish-notation
    ## Basic Ideas: Use stack
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def evalRPN(self, tokens):
    	"""
    	:type tokens: List[str]
    	:rtype: int
    	"""
    	length = len(tokens)
    	if length == 0:
    	    return None
    
    	stack = []
    	for token in tokens:
    	    if token not in '+-*/':
    		stack.append(int(token))
    	    else:
    		num2 = int(stack.pop())
    		num1 = int(stack.pop())
    		if token == '+':
    		    v = num1+num2
    		if token == '-':
    		    v = num1-num2
    		if token == '*':
    		    v = num1*num2
    		if token == '/':
    		    if num1*num2 < 0:
    			v = abs(num1)/abs(num2)
    			v = -v
    		    else:
    			v = num1/num2
    		stack.append(v)
    		#print stack[-1]
    	return stack.pop()
    
    # s = Solution()
    # print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) # 22
    # print s.evalRPN(["2", "1", "+", "3", "*"]) # 9
    # print s.evalRPN(["4", "13", "5", "/", "+"]) # 6
    # print s.evalRPN(["18"]) # 18
