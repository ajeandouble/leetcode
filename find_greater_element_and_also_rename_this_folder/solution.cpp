#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>
#include <queue>
#include <stack>

using namespace	std;

const string	red("\033[4;31m");
const string	green("\033[0;32m");
const string	yellow("\033[0;35m");
const string	blue("\033[0;34m");
const string	reset("\033[0m");

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


template <typename T>
void	print_vector(vector<T> &v, string name = "", vector<T> highlight={})
{
	if (name.size())
		cout << name << ":\t";
	size_t	len = v.size();
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

template<typename T>
void	print_stack(string name, stack<T> s, vector<int> highlight={})
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
	int	len = v.size();
	for (int i = len - 1; i >= 0; --i)
	{
		if (i == 0)
			cout << yellow << v[i] << '\t' << reset;
		else
			cout << v[i] << "\t";
	}
	if (len == 0)
		cout << "     * * * * * * *  *   *    *     *      *";
	cout << endl;
	cout << reset;
}

class Solution {
public:
   public:
	vector<int> find_greater_elements(vector<int> &input) {

		int len = input.size();
		vector<int> ans(len, -1);
		stack<int>	s;
		s.push(0);
		print_stack("stack", s, {0});
		for (int i = 1; i < len; ++i)
		{
			cout << "[ " << i << " ] " << endl;
			print_vector(input, "input", {s.top(), i});
			while (!s.empty() && input[s.top()] <= input[i])
			{
				ans[s.top()] = input[i];
				print_vector(input, green+"input"+reset, {s.top(), i});
				print_vector(ans, "ans");
				s.pop();
				print_stack("stack", s);
			}
			s.push(i);
			print_stack("stack", s, {s.top()});
		}
		return ans;
	}
};

int	main()
{
	vector<int> input = {6, 4, 3, 8, 7, 12, 15, 16, 2, 1, 5, 11, 13, 9};
	print_vector(input, "input");
	Solution s;
	vector<int> ans = s.find_greater_elements(input);
	print_vector(ans, "output");
	return 0;
}
