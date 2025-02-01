class MyNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev, self.next = prev, next

    def __repr__(self):
        return f"[{str(id(self.prev))[-2:] if self.prev else 'x'} <- |{self.val} ({str(id(self))[-2:]})| -> {str(id(self.next))[-2:] if self.next else 'x'}]"

    def __str__(self):
        return f"[{str(id(self.prev))[-2:] if self.prev else 'x'} <- |{self.val} ({str(id(self))[-2:]})| -> {str(id(self.next))[-2:] if self.next else 'x'}]"


class MyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index <= self.size // 2:
            node = self.head
            for _ in range(index):
                node = node.next
            return node.val
        else:
            node = self.tail
            for _ in range(self.size - index -1):
                node = node.prev
            return node.val

    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = MyNode(val)
        else:
            prev_head = self.head
            new_head = MyNode(val, None, prev_head)
            prev_head.prev = new_head
            self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = MyNode(val)
        else:
            prev_tail = self.tail
            new_tail = MyNode(val, prev_tail, None)
            prev_tail.next = new_tail
            self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        newNode = MyNode(val)
        next_node = self.head
        if index <= self.size // 2:
            for _ in range(index):
                next_node = next_node.next
        else:
            next_node = self.tail
            for _ in range(self.size - index -1):
                next_node = next_node.prev
        prev_node = next_node.prev
        prev_node.next = newNode
        next_node.prev = newNode
        newNode.next = next_node
        newNode.prev = prev_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = self.tail = 0
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = new_head
        elif index == self.size - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            deleted_node = self.head
            for _ in range(index):
                deleted_node = deleted_node.next
            prev_node = deleted_node.prev
            next_node = deleted_node.next
            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

        self.size -= 1
        # raise NotImplemented

    def __repr__(self):
        nodeList = []
        node = self.head
        while node:
            nodeList.append(str(node))
            node = node.next
        return " ==> ".join(nodeList) + f"\t (size={self.size})"


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

funcs = {
    "MyLinkedList": lambda x: x,
    "addAtHead": obj.addAtHead,
    "addAtTail": obj.addAtTail,
    "addAtIndex": obj.addAtIndex,
    "deleteAtIndex": obj.deleteAtIndex,
    'get': obj.get
}
calls = [
    "MyLinkedList",
    "addAtHead",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "addAtTail",
    "get",
]


args = [[], [1], [3], [4], [5], [6], [7], [8], [9], [10], [11]]


for i in range(1, len(calls)):
    funcs[calls[i]](*args[i])
    print(f"{calls[i]}({','.join([str(a) for a in args[i]])})\n", obj, '\t\t\t', obj.head, obj.tail)
print(obj.get(6))
