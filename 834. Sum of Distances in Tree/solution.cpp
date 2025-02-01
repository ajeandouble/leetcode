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
	vector<vector<int>> graph;
	vector<int>	count;
	vector<int>	ans_subtree;

	int	root_depths_sum = 0;
	void	dfs1(int curr, int par, vector<vector<int>> &graph) {
		for (auto child: graph[curr]) {
			if (child == par)
				continue ;
			dfs1(child, curr, graph);
			count[curr] += count[child];
			ans_subtree[curr] += ans_subtree[child] + count[child];
		}
		count[curr] += 1;
	}

	void	dfs2(int curr, int par, vector<vector<int>> &graph, int n) {
		for (auto child: graph[curr]) {
			if (child == par)
				continue ;
			ans_subtree[child] = ans_subtree[curr] - count[child] - count[child] + n;
			dfs2(child, curr, graph, n);
		}
	}

    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
		graph.resize(n);
		count.resize(n, 0);
		ans_subtree.resize(n, 0);

		for (int i = 0; i < edges.size(); ++i) {
 			this->graph[edges[i][1]].push_back(edges[i][0]);
			this->graph[edges[i][0]].push_back(edges[i][1]);
		}
		dfs1(0, -42, graph);
		print_vector(count, "First one\t", {});
		print_vector(ans_subtree, "Ans subtree\t", {});
		dfs2(0, -42, graph, n);
		print_vector(ans_subtree, "", {});
		return ans_subtree;
    }
};

class Solution2 {
public:
    vector<vector<int>> v;
    vector<int> counter, res;

    void dfs(int i, int p = -1) {
        for(auto u : v[i]) {
            if(u == p) continue;
            dfs(u, i);
            counter[i] += counter[u];
            res[i] += res[u] + counter[u];
        }
        counter[i] += 1;
    }

    void dfs2(int i, int n, int p = -1) {
        for(auto u : v[i]) {
            if(u == p) continue;
            res[u] = res[i] - counter[u] + n - counter[u];
            dfs2(u, n, i);
        }
    }

    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        v.resize(n);
        for(int i = 0; i < n - 1; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            v[a].push_back(b);
            v[b].push_back(a);
        }
        res.resize(n);
        counter.resize(n);
        dfs(0);
        dfs2(0, n);
        return res;
    }
};


int	main()
{
	Solution	s;
	vector<vector<int>> edges = {{0,1},{0,2},{2,3},{2,4},{2,5}};

	vector<int> ans1 = s.sumOfDistancesInTree(6, edges);

	cout << "-------" << endl;
	Solution2 s2;
	vector<int> ans2 = s2.sumOfDistancesInTree(6, edges);
	print_vector(ans1, "", {});
}