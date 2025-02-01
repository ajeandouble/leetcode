#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <queue>
#include <stack>

using namespace std;

const string red("\033[4;31m");
const string green("\033[0;32m");
const string yellow("\033[0;35m");
const string blue("\033[0;34m");
const string reset("\033[0m");

struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

template <typename T>
void print_vector(vector<T> &v, string name = "", vector<T> highlight = {-1})
{
	if (name.size())
		cout << name << ":\t";
	size_t len = v.size();
	vector<string> colours = {red, green};
	int colours_index = 0;
	for (size_t i = 0; i < len; ++i)
	{
		string hi = "";
		if (count(highlight.begin(), highlight.end(), i) > 0)
			hi = colours[colours_index++ % colours.size()];
		cout << hi << v[i] << reset;
		if (i != len - 1)
			cout << '\t';
	}
	cout << endl;
}

template <typename T>
void print_stack(stack<T> s, string name = "", vector<int> highlight = {-1})
{
	cout << blue;
	if (name.size())
		cout << name << ":\t";
	vector<T> v;
	while (!s.empty())
	{
		v.push_back(s.top());
		s.pop();
	}
	int len = v.size();
	for (int i = len - 1; i >= 0; --i)
	{
		if (i == 0)
			cout << reset << yellow << v[i] << '\t' << reset;
		else
			cout << v[i] << "\t";
	}

	cout << endl;
	cout << reset;
}

class Solution
{
public:
	bool	reachable(vector<int> &heights, int bricks, int ladders, int end)
	{
		vector<int> diffs;
		for (int i = 1; i <= end; ++i)
		{
			diffs.push_back(heights[i] - heights[i - 1]);
		}
		sort(diffs.begin(), diffs.end(), greater<int>());
		print_vector(diffs);
		for (int i = ladders; i < end; ++i)
		{
			if (bricks < diffs[i]) return false;
			bricks -= diffs[i];
		}
		return true;
	}

	int furthestBuilding(vector<int> &heights, int bricks, int ladders)
	{
		int left = 0, right = heights.size() - 1;
		int ans = 0;
		reachable(heights, bricks, ladders, 1);
		while (left <= right)
		{
			int mid = left + (right - mid) / 2;
			if (reachable(heights, bricks, ladders, mid))
			{
				ans = mid;
				left = mid + 1;
			}
			else
				right = mid - 1;
		}
		return ans;
	}
};

int main()
{
	Solution s;

	vector<int> heights = {4,2,7,6,9,14,12};

	cout << s.furthestBuilding(heights, 5, 1);
	return 0;
}
