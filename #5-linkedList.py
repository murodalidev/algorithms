Node (tugun) obyekti | linked list tugunlardan tashkil topadi
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    nodes = []

    def print_nodes(self):
        """Node larni chop etish"""
        temp = self.head
        while temp:
            self.nodes.append(temp.data)
            # print(temp.data)
            temp = temp.next
        return f'Nodes list: {self.nodes}'

    def add_head(self, node):
        """List boshiga tugun qo'shish"""
        new_node = Node(node)
        new_node.next = self.head
        self.head = new_node
        return f'To add head: {new_node.data}'

    def add_into(self, prev_node, node):
        """List o'rtasiga tugun qo'shish"""
        if prev_node is None:
            return 'Previous node is not found'
        new_node = Node(node)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return f'To add into: {new_node.data}'
    
    def add_last(self, node):
        """List o'rtasiga tugun qo'shish"""
        new_node = Node(node)
        if self.head is None:
            # agar list bo'sh bolsa listni boshiga qoshamiz 
            self.head = new_node
        else:
            last = self.head    # tasavur qilamiz 1 ta elementi bor deb
            while last.next:
                last = last.next
            last.next = new_node
        return f'To add last: {new_node.data}'
    
    def delete_node(self, node):
        """Listdan node ni ochirib tashlash"""
        # list ni boshini uslab olamiz
        temp = self.head
        if temp and temp.data == node:
            self.head = temp.next
            temp = None
            return f'Successfully deleted, it was fist node that is -> {node}'
        elif temp is None:
            return f'Empty list'
        else:
            while temp:
                if temp.data == node:
                    break
                prev = temp
                temp = temp.next
        # Node ni list dan  o'chirish
        prev.next = temp.next
        temp = None
        return f'Successfully deleted -> {node}'
        

lst = LinkedList()

node1 = Node(data='Dushanba')
lst.head = node1
print('1: ', lst.head.data)

node2 = Node('Seshanba')
lst.head.next = node2
print('2: ', lst.head.next.data)

node3 = Node('Chorshanba')
node2.next = node3
print('3: ', lst.head.next.next.data)

print(lst.add_head('Boshiga qoshilgan kun'))
print(lst.add_into(node2, 'O\'rtasiga qoshilgan kun'))
print(lst.add_last('Oxiriga qoshilgan kun'))
print(lst.delete_node('Seshanba'))
print(lst.print_nodes())




"""Big O | Compare between linked list and array"""
"""
    #  |   Array   | linked list |
  read | O(n) = 1  |   O(n) = n  |
   add | O(n) = n  |   O(n) = 1  |
delete | O(n) = n  |   O(n) = 1  |
"""