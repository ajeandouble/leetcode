var flat = function (arr, n) {
	if (n <= 0 || arr.every((elem) => typeof elem == 'number'))
		return arr;

	function _flatten(value, n) {
		console.log(`_flatten n=${n}, value=${value}`);
		if (n <= 0 || value.every((elem) => typeof elem == 'number')) {
			return value;
		}
		const newArr = [];
		for (let item of value) {
			console.log(`n=${n}, item=${item}`);
			if (typeof item == 'number') {
				newArr.push(item);
			} else {
				newArr.push(..._flatten(item, n - 1));
			}
		}
		return newArr;
	}
	return _flatten(arr, n);
};

const arr = [1, 2, 3, [4, 5, [6, 7, [8]]]];
const ans = flat(arr, 3);
console.log(ans);
