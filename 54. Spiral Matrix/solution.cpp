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
	vector<int> v;
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
	if (len == 0)
		cout << "     * * * * * * *  *   *    *     *      *";
	cout << endl;
	cout << reset;
}

class Solution
{
public:
	vector<int> spiralOrder(vector<vector<int>> &matrix)
	{
		int m = matrix.size();
		int n = matrix[0].size();
		int total = m * n;
		int begin_row = 0, end_row = m - 1;
		int begin_col = 0, end_col = n - 1;
		vector<int> ans;
		for (int count = 0; count <= total; ++count)
		{
			for (int col = begin_col; col <= end_col; ++col)
			{
				ans.push_back(matrix[begin_row][col]);
				++count;
			}
			begin_row++;
			for (int row = begin_row; row <= end_row; row++)
			{
				ans.push_back(matrix[row][end_col]);
				++count;
			}
			end_col--;
			for (int col = end_col; col >= begin_col; --col)
			{
				ans.push_back(matrix[end_row][col]);
				++count;
			}
			end_row--;
			for (int row = end_row; row >= begin_row; --row)
			{
				ans.push_back(matrix[row][begin_col]);
				++count;
			}
			print_vector(ans);
			begin_col++;
		}
		return ans;
	}
};

int main()
{
	Solution s;
	vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
	s.spiralOrder(matrix);
}