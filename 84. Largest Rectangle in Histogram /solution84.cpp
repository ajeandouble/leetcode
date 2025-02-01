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
			cout << reset << yellow << v[i] << '\t' << reset;
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
    int largestRectangleArea(vector<int>& heights) {
        int maxArea = 0;
        stack<int> st;
        st.push(0);
        size_t len = heights.size();
        vector<int> left_dis(1, 0);
		print_vector(left_dis, "left_dis");
				print_stack(st, "..stack");
        for (unsigned int i = 1; i < len; ++i)
        {
			cout << to_string(i)  + " - " + to_string(heights[i]) + " ---" << endl;
            while (!st.empty() && heights[st.top()] > heights[i])
            {
                st.pop();
				print_stack(st, + " lstack");
            }
            if ( st.empty())
            { 
                left_dis.push_back(0);
            }
            else
            {
                left_dis.push_back(st.top() + 1);
            }
			print_vector(left_dis, "left_dis");
            st.push(i);
			print_stack(st, "e.stack");
			cout << "----" << endl;
        }
		st = stack<int>();
		st.push(len - 1);
		vector<int>right_dis(len, len - 1);
		for (int i = len - 2; i >= 0; --i)
		{  
		print_vector(right_dis);
			while (!st.empty() && heights[st.top()] >= heights[i])
            {
                st.pop();
				print_stack(st, + " lstack");
			}
			if ( st.empty())
			{ 
				right_dis[i] = len - 1;
			}
			else
			{
				cout << "seguefault" << st.top() - 1 << "aa" << endl ;
				right_dis[i] = st.top() - 1;
			}
			st.push(i);
			cout << "seguefault" << st.top() - 1 << "aa" << endl ;
		}
		cout << "seguefault" << st.top() - 1 << "aa" << flush << endl ;
		print_vector(right_dis);
        for (unsigned int i = 0; i < len; ++i)
        {
            maxArea = max((right_dis[i] - left_dis[i] + 1) * heights[i], maxArea);
        }
        return maxArea;
    }
};

int	main()
{
	vector<int> input = {2,1,5,6,2,3};
	print_vector(input, "[input]");
	Solution s;
	int ans = s.largestRectangleArea(input);
	cout << "[" << ans << "]" << endl;
	return 0;
}
