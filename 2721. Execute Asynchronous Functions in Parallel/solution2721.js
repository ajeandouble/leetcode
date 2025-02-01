/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
		const t = new Date();
    const promises = functions.map(fn => {
        return new Promise(async function (res, rej) {
            try {
                const ret = await fn();
                resolved.push(ret);
            } catch(err) {

            }
        });
    })
};

const promise = promiseAll([() => new Promise(res => res(42))])
/**
 * promise.then(console.log); // [42]
 */