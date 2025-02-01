function TreeNode(val, left, right) {
	this.val = val;
	this.left = left;
	this.right = right;
}

// function bfs() {
//   const st =
// }

const root = new TreeNode(
	5,
	new TreeNode(
		8,
		new TreeNode(2, new TreeNode(4), new TreeNode(6)),
		new TreeNode(1)
	),
	new TreeNode(9, new TreeNode(3), new TreeNode(7))
);

function dfs(node) {
	if (!node) return;
	console.log(node.val);
	dfs(node.left);
	dfs(node.right);
}

function bfs(node) {
	const st = [node];
	st.reduce;
	while (st.length) {
		const node = st.shift();
		console.log(node.val);
		if (node.left) st.push(node.left);
		if (node.right) st.push(node.right);
	}
}

var kthLargestLevelSum = function (root, k) {
	--k;
	const visited = {};
	function dfs(node, level) {
		if (!(level in visited)) visited[level] = [];
		visited[level].push(node.val);
		if (node.left) dfs(node.left, level + 1);
		if (node.right) dfs(node.right, level + 1);
	}
	dfs(root, 0);
	const sums = Object.values(visited).map((v) =>
		v.reduce((acc, curr) => acc + curr, 0)
	);
	if (k >= sums.length) {
		return -1;
	}
	sums.sort((a, b) => b - a);
	return sums[k];
};

// dfs(root);
// console.log('----');
// bfs(root);

const ans = kthLargestLevelSum(root, 2);
console.log(ans);
