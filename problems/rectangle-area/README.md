# Leetcode: Rectangle Area     :BLOG:Medium:


---

Rectangle Area  

---

Similar Problems:  
-   [Meeting Rooms](https://code.dennyzhang.com/meeting-rooms)
-   [Rectangle Overlap](https://code.dennyzhang.com/rectangle-overlap)
-   [Review: Rectangle Problems](https://code.dennyzhang.com/review-rectangle)
-   Tag: [#rectangle](https://code.dennyzhang.com/tag/rectangle)

---

Find the total area covered by two rectilinear rectangles in a 2D plane.  

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.  

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/rectangle_area.png)  

Rectangle Area  
Assume that the total area is never beyond the maximum possible value of int.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/rectangle-area)  

Credits To: [leetcode.com](https://leetcode.com/problems/rectangle-area/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/rectangle-area
    ## Basic Ideas:
    ##     width: min(C,G)-max(A,E)
    ##     height: min(D, H)-max(B,F)
    ##
    ##     If width or height is not positive, they don't overlap
    ##
    ## Complexity: Time O(1), Space O(1)
    class Solution:
        def computeArea(self, A, B, C, D, E, F, G, H):
            """
            :type A: int
            :type B: int
            :type C: int
            :type D: int
            :type E: int
            :type F: int
            :type G: int
            :type H: int
            :rtype: int
            """
            area1 = abs(C-A)*abs(B-D)
            area2 = abs(E-G)*abs(F-H)
            w = min(C,G)-max(A,E)
            h = min(D, H)-max(B,F)
            if w<=0 or h<=0:
                return area1 + area2
            else:
                return area1 + area2 - w*h