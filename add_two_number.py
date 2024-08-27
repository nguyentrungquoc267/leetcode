class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.l1 = None
        self.l2 = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(out)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def input(self):
        l1_str = input("Nhập các phần tử của chuỗi liền nhau không dấu cách cho l1: ")
        l2_str = input("Nhập các phần tử của chuỗi liền nhau không dấu cách cho l2: ")
        
        # Chuyển đổi chuỗi thành danh sách liên kết
        self.l1 = self.create_linked_list(l1_str)
        self.l2 = self.create_linked_list(l2_str)
    
    def create_linked_list(self, num_str):
        # Tạo danh sách liên kết từ chuỗi số
        dummy = ListNode(0)
        current = dummy
        for char in num_str:
            current.next = ListNode(int(char))
            current = current.next
        return dummy.next

def main():
    solution = Solution()
    solution.input()
    result = solution.addTwoNumbers(solution.l1, solution.l2)

    # In kết quả
    while result:
        print(result.val, end="")
        result = result.next
    print()

if __name__ == "__main__":
    main()

    