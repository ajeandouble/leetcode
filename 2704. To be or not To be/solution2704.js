var expect = function (a) {
	return {
		toBe: (b) => {
			if (a === b) return true;
			else throw new Error('Not Equal');
		},
		notToBe: (b) => {
			if (a !== b) return true;
			else throw new Error('Equal');
		},
	};
};
