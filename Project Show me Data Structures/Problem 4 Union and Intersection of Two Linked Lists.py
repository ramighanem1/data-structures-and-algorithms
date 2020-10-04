class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def get_list(self):
        list_item=[]
        node = self.head
        while node:
            list_item.append(node.value)
            node = node.next

        return list_item

def union(llist_1, llist_2):
    # Your Solution Here
    llist_11=llist_1.get_list()
    llist_22= llist_2.get_list()
    merged_list = list(set(llist_11+llist_22))
    union_llist=LinkedList()
    for i in merged_list:
        union_llist.append(i)
    return union_llist
            
            
    
    
    

def intersection(llist_1, llist_2):
    llist_11=llist_1.get_list()
    llist_22= llist_2.get_list()
    merged_list = [value for value in llist_11 if value in llist_22]
    merged_list=list(set(merged_list))
    
    intersection_llist=LinkedList()
    for i in merged_list:
        intersection_llist.append(i)
    return intersection_llist

    
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))





