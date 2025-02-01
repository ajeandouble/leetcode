class KthLargest {
	_elements: number[];
	_k: number;
	constructor(k: number, nums: number[]) {
		this._elements = [];
		this._k = k;
		for (let n of nums) {
			this.add(n);
		}
	}

	add(val: number): number {
		let i = this._elements.length;
		this._elements.push(val);

		console.log('val:', val, this._elements);
		while (i > 0) {
			const parentIndex = Math.floor((i - 1) / 2);
			console.log(`i=${i}\telements[${parentIndex}] === ${this._elements[parentIndex]}`)
			if (val <= this._elements[parentIndex]) {
				const swap = this._elements[i];
				this._elements[i] = this._elements[parentIndex];
				this._elements[parentIndex] = swap;
				console.log('\t', this._elements);
			}
			i = parentIndex;
		}
		console.log(this._elements, '\n--------');
		return this._elements[this._elements.length - this._k];
	}
}

let kth = new KthLargest(3, [4, 5, 8, 2]);
console.log('\t-> ', kth.add(3));
console.log('\t-> ', kth.add(5));
console.log('\t-> ', kth.add(10));
console.log('\t-> ', kth.add(9));
console.log('\t-> ', kth.add(4));
