# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL 
# 
# This problem is from LeetCode https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
#

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        amount = 0
        lastNode = None
        while(node):
            amount += 1
            if not node.next:
                lastNode = node
            node = node.next
            
        if not head or k % amount is 0:
            return head
            
        node = head
        newHead = head
        iteration = 1
        while(node):
            if iteration is amount - (k % amount):
                newHead = node.next
                node.next = None
                lastNode.next = head
                break
            node = node.next
            iteration += 1
        
        return newHead
