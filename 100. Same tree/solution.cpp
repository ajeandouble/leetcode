#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <unistd.h>

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
    void dfs(TreeNode *tree, vector<int> &v)
    {
		if (tree == nullptr)
		{
			v.push_back(INT_MIN);
			return ;
		}
        v.push_back(tree->val);
		dfs(tree->left, v);
		dfs(tree->right, v);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        dfs(p, vp); cout << endl;
        dfs(q, vq); cout << endl;
        if (vp.size() != vq.size())
            return false;
        for (size_t i = 0; i < vp.size(); ++i)
        {
            if (vp[i] != vq[i])
                return false;
        }
        return true;
    }
    vector<int> vp;
    vector<int> vq;
};

int	main()
{
	Solution s;
	// TreeNode *p_c = new TreeNode(3);
	TreeNode *p_a = new TreeNode(2);
	// TreeNode *p_b = new TreeNode(2);
	TreeNode *rootp = new TreeNode(1, p_a, nullptr);

	// TreeNode *q_a = new TreeNode(1);
	TreeNode *q_b = new TreeNode(2);
	TreeNode *rootq = new TreeNode(1, nullptr, q_b);

	cout << s.isSameTree(rootp, rootq) << endl;
}