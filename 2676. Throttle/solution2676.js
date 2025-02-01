/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
	let savedArgs = undefined;
	let locked = false;
	return function (...args) {
		function cb() {
			savedArgs = args;
			if (!locked) {
				setTimeout(() => {
					fn(savedArgs);
					locked = false;
					savedArgs = undefined;
					cb();
				}, t);
			}
		}
		cb();
	};
};

const throttled = throttle(console.log, 1000);
throttled('log'); // logged immediately.
throttled('log'); // logged at t=100ms.
