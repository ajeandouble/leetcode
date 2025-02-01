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
void	print_vector(vector<T> &v, string name = "", vector<T> highlight={-1})
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
void	print_stack(stack<T> s, string name="", vector<int> highlight={-1})
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
	int	len = v.size();
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

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char>s_stack;
        stack<char>t_stack;
        for (size_t i = 0; i < s.size(); ++i)
        {
			cout << flush << "[" << s[i] << "]" << endl;
			print_stack(s_stack, "S");
            if (s[i] == '#' && !s_stack.empty())
                s_stack.pop();
            else if (s[i] != '#')
                s_stack.push(s[i]);
			print_stack(s_stack, "S"); cout << endl;
        }
		cout << "-----" << endl;
        for (size_t i = 0; i < t.size(); ++i)
        {
			print_stack(t_stack, "T");
            if (t[i] == '#' && !t_stack.empty())
                t_stack.pop();
            else if (t[i] != '#')
                t_stack.push(t[i]);
			print_stack(t_stack, "T");
        }
		print_stack(s_stack);
		print_stack(t_stack);
        while (!s_stack.empty())
        {
            if (t_stack.empty())
                return false;
            if (s_stack.top() != t_stack.top())
                return false;
            s_stack.pop(); t_stack.pop();
        }
        if (!t_stack.empty() || !s_stack.empty())
            return false;
        return true;
    }
};

int	main()
{
	Solution s;

	cout << s.backspaceCompare("y#fo##f", "y#f#o##f") << endl;
}
