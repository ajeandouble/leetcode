function chunk(arr: any[], size: number): any[][] {
    const newArr = [];
    // if (size > arr.length) {
    //     return arr.splice(0, size);
    // }
	const splicedArray = [...arr];
    for (let i = 0; i < arr.length / size; ++i) {
		newArr.push(splicedArray.splice(0, size));
    }
    if (splicedArray.length)
        newArr.push(splicedArray);
	// console.log(arr)
    return newArr;
};

console.log(chunk([1,2,3,4,5], 1));