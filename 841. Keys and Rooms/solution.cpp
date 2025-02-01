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


void print_queue(std::queue<int> q)
{
  while (!q.empty())
  {
    std::cout << q.front() << " ";
    q.pop();
  }
  std::cout << std::endl;
}

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        queue<int> q;
        vector<bool> visited(rooms.size(), false);
        q.push(0);

        while (q.size())
        {
            int size = q.size();
            int current_room = q.front();
			visited[current_room] = true;
            q.pop();
            for (int next_visitable: rooms[current_room]) {
                if (!visited[next_visitable]) q.push(next_visitable);
            }
        }
		for (int v: visited) cout << v << endl;
        return true;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> rooms = {{1,3}, {3,0,1}, {2}, {0}};
    s.canVisitAllRooms(rooms);
}
