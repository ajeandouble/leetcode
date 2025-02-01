#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <queue>

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

using namespace	std;

class Solution {
public:
   public:
	int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
		int	n = grid.size() - 1;
		if (grid[0][0] == 1 || grid[n][n] == 1)
			return -1;
		cout << "n=" << n << endl;
		vector<vector<int>> moves = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 0}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
		queue<vector<int>> que;
		que.push({0, 0, 1});
		while (!que.empty())
		{
			vector <int> front = que.front();
			que.pop();
			if (front[0] == n && front[1] == n)
				return front[2];
			for (vector<int> move: moves)
			{
				int x = front[0] + move[0], y = front[1] + move[1];
				if (0 <= x && x <= n && 0 <= y && y <= n && grid[x][y] == 0)
				{
					grid[x][y] = 1; // mark visited
					que.push({x, y, front[2] + 1});
					// cout << "what" << endl;
				}
			}
		}
		que.push({0, 0, 1});
		return -1;
	}
};

int	main()
{
	vector<vector<int>> grid = {{0, 0}, {0, 0}};
	Solution s;
	cout << s.shortestPathBinaryMatrix(grid) << endl;

}