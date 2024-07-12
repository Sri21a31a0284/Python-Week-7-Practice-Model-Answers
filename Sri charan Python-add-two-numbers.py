class Solution:
    def addTwoNumbers(self, list1, list2):
        l1 = list1
        l2 = list2
        carry = 0
        result = ListNode(0)
        temp = result
        
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            temp.next = ListNode(carry % 10)
            temp = temp.next
            carry = carry // 10
        
        if carry == 1:
            temp.next = ListNode(carry)
        
        return result.next
