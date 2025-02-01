/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
	if (object === null || ['string', 'number', 'boolean'].includes(typeof object)) {
		switch (typeof object) {
			case 'string':
				return `"${object}"`;
			case 'number':
				return `${object}`
			case 'boolean':
				return `${object}`
			default:
				return 'null';
		}
		return object + '';
	}
	let str = '';
	if (typeof object === 'object' && object instanceof Array) str += '[';
	else if (typeof object === 'object') str += '{';

	let i = 0;
	for (let k of Object.keys(object)) {
		if (typeof object !== 'object' || !(object instanceof Array))
			str += `"${k}":`;
		if (typeof object[k] === 'object' && object[k] !== null) {
			str += jsonStringify(object[k]);
		}else if (typeof object[k] === 'string') {
			escapedQuotes = String(object[k]).replace(/"/g, '\\"');
			str += `"${escapedQuotes}"`;
		} else {
			console.log('a');
			str += '' + object[k];
		}
		console.log('z');
		if (i < Object.keys(object).length - 1) str += ',';
		++i;
	}

	if (typeof object === 'object' && object instanceof Array) str += ']';
	else if (typeof object === 'object') str += '}';
	return str;
};

const obj = {
	a: 42,
	b: null,
	c: "zzz\"",
	d: {a:32, c:24, d: null, e: undefined},
};

let ans = jsonStringify(obj);

console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify(obj)); // JSON.stringify(obj));

console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify(obj)); // JSON.stringify(obj));

ans = jsonStringify(null)
console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify(null)); // JSON.stringify(obj));

ans = jsonStringify("z")
console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify("z")); // JSON.stringify(obj));


ans = jsonStringify(true)
console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify(true)); // JSON.stringify(obj));

ans = jsonStringify(42)
console.log(ans); // JSON.stringify(obj));
console.log(JSON.stringify(42)); // JSON.stringify(obj));

// JSON.stringify(obj);
