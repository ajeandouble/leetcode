/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function* (arr) {
	const inOrderArray = [];

	function _dfs(arr) {
		for (let elem of arr) {
			if (typeof elem === 'number') {
				inOrderArray.push(elem);
			}
			else
				_dfs(elem);
		}
	}
	_dfs(arr);
	for (let elem of inOrderArray) {
		yield elem;
	}
};

const gen = inorderTraversal([[[6]], [1, 3], []]);
console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
