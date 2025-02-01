var promisePool = async function (fns, n, p) {
	return new Promise((res) => {
		let i = 0;
		let inProgress = 0;

		function callback() {
			console.log(callback.name, p);
			if (i === fns.length && inProgress === 0) {
				res();
			}
			while (i < fns.length && inProgress < n) {
				console.log(`i=${i} inProgress=${inProgress}`, p);
				fns[i++]().then(() => {
					inProgress--;
					console.log(`then\ti=${i} inProgress=${inProgress}`, p);
					callback();
				});
				inProgress++;
			}
		}
		callback();
	});
};

const fns1 = [
	() =>
		new Promise((res) => {
			setTimeout(() => {
				console.log('P1');
				res();
			}, 300);
		}),
	() =>
		new Promise((res) => {
			setTimeout(() => {
				console.log('P2');
				res();
			}, 400);
		}),
	() =>
		new Promise((res) => {
			setTimeout(() => {
				console.log('P3');
				res();
			}, 200);
		}),
];
promisePool(fns1, 2, 'p1');
console.log('-----');

const fns2 = [
	() => new Promise((res) => setTimeout(res, 300)),
	() => new Promise((res) => setTimeout(res, 400)),
	() => new Promise((res) => setTimeout(res, 200)),
];
// promisePool(fns1, 1, 'p2');
