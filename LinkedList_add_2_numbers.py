class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


l1= ListNode(5)
l2= ListNode(6)
l3= ListNode(4)
l1.next = l2
l2.next = l3

l4= ListNode(2)
l5= ListNode(4)
l6= ListNode(3)
l4.next = l5
l5.next = l6

l7= ListNode(l1.val + l4.val)
l8= ListNode(l2.val + l5.val)
l9= ListNode(l3.val + l6.val)
l7.next = l8
l8.next = l9
# if l1+l4 > 9 ==== add 1 to next
print(l7.val, l8.val, l9.val)
