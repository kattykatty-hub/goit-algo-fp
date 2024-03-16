from utils import LinkedList, Node


class Task1:
    @staticmethod
    def reverse_linked_list(linked_list: LinkedList) -> LinkedList:
        """
        >>> l = LinkedList([3, 2, 1])
        >>> l = Task1.reverse_linked_list(l)
        >>> l.to_list()
        [1, 2, 3]

        """
        prev = None
        current = linked_list.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        linked_list.head = prev
        return linked_list


class Task3:
    @staticmethod
    def merge_two_sorted_linked_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
        """
        >>> l = Task3.merge_two_sorted_linked_lists(LinkedList([1, 3, 5]), LinkedList([2, 3, 4]))
        >>> l.to_list()
        [1, 2, 3, 3, 4, 5]

        >>> l = Task3.merge_two_sorted_linked_lists(LinkedList([1, 3, 5]), LinkedList([]))
        >>> l.to_list()
        [1, 3, 5]

        """
        merged_list = LinkedList()
        cur1 = list1.head
        cur2 = list2.head

        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged_list.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                merged_list.insert_at_end(cur2.data)
                cur2 = cur2.next

        while cur1:
            merged_list.insert_at_end(cur1.data)
            cur1 = cur1.next

        while cur2:
            merged_list.insert_at_end(cur2.data)
            cur2 = cur2.next

        return merged_list


class Task2:
    @staticmethod
    def merge_sort(lst: LinkedList) -> LinkedList:
        """
        >>> Task2.merge_sort(LinkedList([1, 7, 6, 2, 9,-1, 4])).to_list()
        [-1, 1, 2, 4, 6, 7, 9]

        """
        head = lst.head
        if not head or not head.next:
            return lst

        middle = Task2.get_middle(lst)
        next_to_middle = middle.next
        middle.next = None

        l_lst = LinkedList()
        l_lst.head = head

        r_lst = LinkedList()
        r_lst.head = next_to_middle

        left = Task2.merge_sort(l_lst)
        right = Task2.merge_sort(r_lst)

        sorted_list = Task3.merge_two_sorted_linked_lists(left, right)
        return sorted_list

    @staticmethod
    def get_middle(lst: LinkedList) -> Node:
        head = lst.head
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
