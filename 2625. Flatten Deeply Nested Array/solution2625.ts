type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number): MultiDimensionalArray {
	if (n <= 0)
		return arr;
	const newArr: MultiDimensionalArray[] = [];

    function _flatten(value: MultiDimensionalArray[] | any, n: number): any {
		console.log(`n=${n} value=${value}`)
		if (n <= 0) {
			newArr.push(value);
			console.log(`${value} newArr=${newArr}`)
			return ;
		}
		if (typeof(value) == 'number') {
			newArr.push(value);
			return ;
		}
		// Array
		for (let item of value) {
			var result = _flatten(item, n - 1);
			console.log(`result=${result} newArr=${newArr}`)
		}
    }
	_flatten(arr, n);
	return newArr;
};

const arr = [1,2,3, [3,4, [5,6, [7]]]];
const ans = flat(arr,1);
console.log(ans[3][2]);
