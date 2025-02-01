#include "../solution.hpp"

void	traverse_bfs(TreeNode *root)
{
	if (root == nullptr)
		return ;
	
	queue<TreeNode *> q;
	vector<TreeNode *> values;
	q.push(root);
	values.push_back(root);

	while (!q.empty())
	{
		TreeNode *node = q.front();
		q.pop();

		if (node->left != nullptr)
		{
			q.push(node->left);
			values.push_back(node->left);
		}

		if(node->right != nullptr)
		{
			q.push(node->right);
			values.push_back(node->right);
		}
	}

	
	for (const TreeNode * node: values)
	{
		cout << node->val << ' ';
	}
	// print_vector(values);
}


TreeNode	*find_bfs(TreeNode *root, int value)
{
	if (root == nullptr)
		return nullptr;
	
	queue<TreeNode *> q;
	q.push(root);

	while (!q.empty())
	{
		TreeNode *node = q.front();
		if (node->val == value)
			return node;
		q.pop();

		if (node->left != nullptr)
		{
			q.push(node->left);
		}

		if(node->right != nullptr)
		{
			q.push(node->right);
		}
	}
	return nullptr;
}


TreeNode	*find_parent(TreeNode *root, int value)
{
	if (root == nullptr)
		return nullptr;
	
	queue<TreeNode *> q;
	q.push(root);

	while (!q.empty())
	{
		TreeNode *node = q.front();
		q.pop();

		if (node->left != nullptr)
		{
			if (node->left->val == value)
				return node;
			q.push(node->left);
		}

		if(node->right != nullptr)
		{
			if (node->right->val == value)
				return node;
			q.push(node->right);
		}
	}
	return nullptr;
}


TreeNode	*find_node(TreeNode *root, int value)
{
	cout << "\t" << value << endl << flush;
	if (root == nullptr)
		return nullptr;
	else if (root->val == value)
		return root;
	
	queue<TreeNode *> q;
	q.push(root);

	while (!q.empty())
	{
		TreeNode *node = q.front();
		q.pop();

		if (node->left != nullptr)
		{
			if (node->left->val == value)
				return node->left;
			q.push(node->left);
		}

		if(node->right != nullptr)
		{
			if (node->right->val == value)
				return node->right;
			q.push(node->right);
		}
	}
	return nullptr;
}

TreeNode	*deleteNode(TreeNode *root, int value)
{
	static int i = 0;
	cout << i++ << "::\t";
	if (root == nullptr)
		return nullptr;
	TreeNode *node = find_node(root, value);
	TreeNode *parent = find_parent(root, value);

	cout << "\t" << value << "\t" << node << endl;
	cout << "\t" << parent << endl;
	if (node == nullptr)
		return nullptr;
	if (parent != nullptr)
	{
		// leaf node
		if (node->left == nullptr && node->right == nullptr)
		{
			cout << "yo " << parent->val << "" << endl;
			if (parent->left == node)
			{
				cout << "no";
				parent->left = nullptr;
			}
			else
			{
				cout << "yu";
				parent->right = nullptr;
			}
			cout << "leaf?";
			delete node;
			return nullptr;
		}

		else if ((node->left != nullptr && node->right == nullptr)
			|| (node->left == nullptr && node->right != nullptr))
		{
			if (parent->left == node)
				parent->left = node->left != nullptr ? node->left : node->right;
			return nullptr;
		}

		else
		{
			node->val = node->right->val;
			node->right = deleteNode(node->right, node->right->val);
		}

	}
	else
	{
		if (node->right == nullptr && node->left == nullptr)
		{
			delete node;
			return nullptr;
		}
		else if ((node->left != nullptr && node->right == nullptr)
			|| (node->left == nullptr && node->right != nullptr))
		{
			TreeNode *tmp;
			if (node->left != nullptr)
				tmp = node->left;
			else
				tmp = node->right;
			delete node;
			return tmp;
		}
		else
		{
			cout << "recursion" << node->right << endl;
			node->val = node->right->val;
			node->right = deleteNode(node->right, node->right->val);
		}
	}
	
	return node;
}

int	main()
{
	TreeNode *root = new TreeNode(1);
	TreeNode *n_2 = new TreeNode(2);
	TreeNode *n_3 = new TreeNode(3);
	TreeNode *n_4 = new TreeNode(4);
	TreeNode *n_6 = new TreeNode(6);
	TreeNode *n_7 = new TreeNode(7);
	TreeNode *n_9 = new TreeNode(9);
	TreeNode *n_10 = new TreeNode(10);

	root->left = n_2;
	root->right = n_3;
	n_2->left = n_4;
	n_2->right = n_6;
	n_3->left = n_7;
	n_3->right = n_9;
	n_4->left = n_10;

	traverse_bfs(root);
	cout << endl << find_bfs(root, 12) << endl;
	cout << find_bfs(root, 10)->val << endl;
	deleteNode(root, 1);
	deleteNode(root, 7);

	cout << "-------\n";
	TreeNode *found = find_bfs(root, 1);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 2);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 3);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 4);	
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 6);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 7);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 9);
	cout << (found != nullptr ? found->val : -1) << endl;
	found = find_bfs(root, 10);
	cout << (found != nullptr ? found->val : -1) << endl;
	print2D(root);
}