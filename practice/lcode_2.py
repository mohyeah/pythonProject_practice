# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 初始化哑节点和当前节点
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # 遍历链表，直到两个链表都遍历完，且没有进位
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            # 计算当前位的值和进位
            sum_val = val1 + val2 + carry
            carry = sum_val // 10

            # 创建新的节点并赋值
            current.next = ListNode(sum_val % 10)
            current = current.next

            # 移动链表
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 返回结果链表的头部
        return dummy.next