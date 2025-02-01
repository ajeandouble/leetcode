class DLList:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_head, self.dummy_tail = DLList(-1, -1), DLList(-1, -1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def _remove_node(self, node: DLList):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node.next
        node_next.prev = node.prev
        self.size -= 1

    def _add_node_left(self, node: DLList):
        head = self.dummy_head.next
        head.prev = node
        node.next = head
        node.prev = self.dummy_head
        self.dummy_head.next = node
        self.size += 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node.next
            node_next.prev = node.prev
            self.size -= 1
            head = self.dummy_head.next
            head.prev = node
            node.next = head
            node.prev = self.dummy_head
            self.dummy_head.next = node
            self.size += 1
            return val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._remove_node(node)
            self._add_node_left(node)
        else:
            new_node = DLList(key, val)
            if self.size >= self.capacity:
                dummy_tail_prev = self.dummy_tail.prev
                node = dummy_tail_prev
                node_prev = node.prev
                node_next = node.next
                node_prev.next = node.next
                node_next.prev = node.prev
                self.size -= 1
                del self.cache[dummy_tail_prev.key]
            head = self.dummy_head.next
            node = new_node
            head.prev = node
            node.next = head
            node.prev = self.dummy_head
            self.dummy_head.next = node
            self.size += 1
            self.cache[key] = new_node


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
print(lRUCache.cache)
assert lRUCache.get(2) == -1
