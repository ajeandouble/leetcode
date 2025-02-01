from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation

class Solution:
    def __init__(self):
        self.G = nx.DiGraph()
        self.edges = []
        self.pos = {}
        self.node_count = 0

    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        part = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def dfs(i, node_name, x, y):
            nonlocal part
            if i >= len(s):
                ans.append(part.copy())
                return

            child_count = 0
            for j in range(i, N):
                if is_palindrome(s[i: j + 1]):
                    new_node_name = f"{node_name}_{child_count}"
                    self.G.add_edge(node_name, new_node_name, label=s[i: j + 1])
                    self.edges.append((node_name, new_node_name))
                    new_x, new_y = x + child_count, y - 1
                    self.pos[new_node_name] = (new_x, new_y)
                    part.append(s[i: j + 1])
                    dfs(j + 1, new_node_name, new_x, new_y)
                    part.pop()
                    import time
                    time.sleep(0.5)
                    child_count += 1

        self.pos["root"] = (0, 0)
        dfs(0, "root", 0, 0)
        return ans

def update(num, solution, ax):
    ax.clear()
    if num >= len(solution.edges):
        return
    edge = solution.edges[num]
    solution.G.remove_edge(*edge)
    labels = nx.get_edge_attributes(solution.G, 'label')
    nx.draw(solution.G, pos=solution.pos, labels=labels, with_labels=False, node_color='lightblue', font_weight='bold', node_size=700, font_size=18, ax=ax, edgecolors='k')
    nx.draw_networkx_edge_labels(solution.G, pos=solution.pos, edge_labels=labels, ax=ax)
    solution.G.add_edge(*edge)

if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    ans = solution.partition(s)

    fig, ax = plt.subplots(figsize=(10, 10))
    ani = animation.FuncAnimation(fig, update, frames=len(solution.edges), fargs=(solution, ax), repeat=False)
    plt.show()
