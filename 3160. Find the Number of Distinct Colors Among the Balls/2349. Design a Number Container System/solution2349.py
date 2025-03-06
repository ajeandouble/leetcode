from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        self.indexes = defaultdict(int)  # number at idx
        self.numbers = defaultdict(list)  # idxs at number

    def change(self, index: int, number: int) -> None:
        prev_num_at_idx = self.indexes[index]
        if prev_num_at_idx:
            prev_idxs = self.numbers[prev_num_at_idx]
            self.numbers[prev_num_at_idx] = [x for x in prev_idxs if x != index]
        self.indexes[index] = number
        heapq.heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if not self.numbers[number]:
            return -1
        return self.numbers[number][0]


# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
input = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
output = [None]
for action in input[1:]:
    if len(action) == 1:
        out = obj.find(action[0])
    elif len(action) == 2:
        out = obj.change(action[0], action[1])
    else:
        raise ValueError
    output.append(out)
print(output)
