var decodeMessage = function (key, message) {
	const subst = {};
	let count = 0;
	for (let k of key) {
		if (!(k in subst) && k !== ' ') {
			subst[k] = String.fromCharCode(97 + count++);
		}
	}
	let ans = '';
	for (let m of message) {
		if (m !== ' ') ans += subst[m];
		else ans += m;
	}
	return ans;
};

key = 'the quick brown fox jumps over the lazy dog';
msg = 'vkbs bs t suepuv';
// console.log(decodeMessage(key, msg));

var equalFrequency = function (word) {
	let frequencies = Array(26).fill(0);
	for (let w of word) {
		frequencies[w.charCodeAt(0) - 97]++;
	}
	m = {};
	for (let f of frequencies) {
		if (f in m) {
			m[f]++;
		}
		else m[f] = 1;
	}
	delete m[0]
	console.log(m, word)
	if (1 in m && Object.keys(m).length === 1)
		return true;
	if (Object.keys(m)[0][1] && Object.keys(m)[0][1])
		return true;
	if (Object.keys(m).length === 2 && Object.values(m).every(v => v === 1))
		return true;
	max_key = Math.max(...Object.keys(m).map(item => Number(item[0])));
	min_key = Math.min(...Object.keys(m).map(item => Number(item[0])));
	max_val = Math.max(...Object.values(m).map(item => Number(item)));
	min_val = Math.min(...Object.values(m).map(item => Number(item)));

	return Math.abs(max_key - min_key) === 1 && Math.abs(max_val - min_val) === 1;
	console.log(max_key, min_key, max_val, min_val, '<---');
	return 'fuck';
};

console.log(equalFrequency('aca')); // true
console.log(equalFrequency('abcc')); // true
console.log(equalFrequency('aazz')); // false
console.log(equalFrequency('bac')); // true
console.log(equalFrequency('bbac')); // true
console.log(equalFrequency('bbaccc')); // true
console.log(equalFrequency('aabcd')); // true
console.log(equalFrequency('ddaccb')); //

