Array.prototype.snail = function (rowsCount, colsCount) {
	if (rowsCount * colsCount !== this.length) return [];
	let copiedArray = [];
	for (let i = 0; i < this.length / rowsCount; ++i) {
		let s = this.slice(i * rowsCount, i * rowsCount + rowsCount);
		if (i % 2 === 1)
			s = s.reverse();
		copiedArray = [...copiedArray, ...s];
	}
	const newArr = Array(rowsCount);
	for (let row = 0; row < rowsCount; ++row) newArr[row] = Array(colsCount);

	let i = 0;
	for (let i = 0; i < colsCount; ++i) {
		for (let j = 0; j < rowsCount; ++j) {
			newArr[j][i] = copiedArray[i * rowsCount + j];
		}
		// newArr[i] = [...newArr].reverse(newArr[i]);
	}
	return newArr;
};

nums = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15];

let ans = nums.snail(5, 4);
console.log(ans);
