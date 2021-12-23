# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        Runtime: 96 ms, faster than 89.49% of Python3             online submissions for Reorder List.

        先找到列表中间位置，
        之后把后半段倒序，逐个从头插入前半部分
        """
        if head is None or head.next is None or head.next.next is None:
            # 0,1,2 elements in list
            return
        
        one_step_p = head
        two_step_p = head.next

        while two_step_p.next and two_step_p.next.next:
            two_step_p = two_step_p.next.next
            one_step_p = one_step_p.next
        if two_step_p.next is not None:   # odd number elements
            one_step_p = one_step_p.next   # get middle element
            
        # print(one_step_p.val, two_step_p.val)

        def reverse_list(head):
            if head is None or head.next is None:
                return head
            p = head
            last_p = None
            while p.next is not None:
                tmp = p.next
                p.next = last_p
                last_p = p
                p = tmp
            r_head = p
            p.next = last_p
            return r_head

        rev_last_half_head = reverse_list(one_step_p.next)
        p = rev_last_half_head
        # while p is not None:
        #     print(p.val, end=' ')
        #     p=p.next

        one_step_p.next = None

        p = head
        
        while True:
            q = rev_last_half_head
            if q is None:
                break

            tmp = p.next
            p.next = q
            rev_last_half_head = q.next # move rev list head
            q.next = tmp
            p = tmp

        
    def __reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        算法超时
        """
        if head is None:
            return head
        
        def get_last(head):
            if head is None:
                return head
            before_last = None
            p = head
            
            while p.next is not None:
                before_last = p
                p = p.next  
            if before_last is not None:
                before_last.next = None
            return p
        
        cur_p = head 
    
        while True:
            # 每次取最后一个插入
            last_p = get_last(head)
            tmp = cur_p.next
            cur_p.next = last_pquit
            last_p.next = tmp
            cur_p = tmp
            
            if cur_p is None or cur_p.next is None:
                break
        