/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

var topKFrequent = function(nums, k) {
	m = new Map();
	for (let n of nums) {
		for (let n of nums) {
	if (m.has(n)) {
			m.set(n, m.get(n) + 1);
		}
		else {
			m.set(n, 1);
		}
		}

	}
	// for (let n of m) {
	// 	console.log(n);
	// }
	return Array.from(m).sort((a, b) => a[1] - b[1]).slice(0, k).map(item => item[0])
}

// console.log(topKFrequent([1,1,1,2,2,3], 2)); // [1,2]
console.log(topKFrequent([4,1,-1,2,-1,2,3], 2)); // [-1,2]