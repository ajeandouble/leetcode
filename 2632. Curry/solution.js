/**
 * @param {Function} fn
 * @return {Function}
 */

var curry = function (fn) {
	let len = fn.length;
	const savedArgs = [];
	return function curried(...args) {
		// console.log(`len=${len}`)
		len -= args.length;
		savedArgs.push(...args);
		// console.log(`len-args=${len} args=${args} savedArgs=${savedArgs}`)
		if (len > 0) {
			// console.log('return curried')
			return curried;
		}
		else {
			// console.log('yo')
			return fn(...savedArgs);
		}
	};
};

function sum(a, b) {
	return a + b;
}
const csum = curry(sum);
// console.log(csum(1)(2)); // 3
