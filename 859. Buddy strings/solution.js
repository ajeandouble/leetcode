var buddyStrings = function (s, goal) {
	if (s.length !== goal.length) return false;
	console.log('-----');
	if (s == goal && new Set(s).size < s.length) {
		return true;
	}
	console.log(new Set(s).size, new Set(s), s.length);
	console.log('______');
	let count = 0;
	let indices = [];
	for (let i = 0; i < s.length; ++i) {
		if (s[i] !== goal[i]) {
			if (count >= 2) return false;
			++count;
			indices.push(i);
		}
	}
	let a = indices[0];
	let b = indices[1];
	if (s[a]  === undefined || s[b] === undefined)
		return false;
	console.log(`s[a]=${s[a]} s[b]=${s[b]}, count, `);
	if (s[a] !== goal[b] || s[b] !== goal[a]) {
		return false;
	}
	return true;
};
let ans = buddyStrings('ab', 'ab');
console.log(ans);
ans = buddyStrings("ab", "ba");
console.log(ans);
ans = buddyStrings("aa", "aa");
console.log(ans);
