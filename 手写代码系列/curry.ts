// 函数 柯里化的实现

// 实现原理就是当柯里化后的函数接收到足够的参数后，就会开始执行原函数。
// 而如果接收到的参数不足的话，就会返回一个新的函数，用来接收余下的参数。

function curry(func: Function) {
	return function curried(...args) {
		// 通过函数的length属性，来获取函数的形参个数
		if (args.length >= func.length) {
			return func.apply(this, args);
		} else {
			return function (...args2) {
				return curried.apply(this, args.concat(args2));
			};
		}
	};
}

const test = (a: number, b: number) => a + b;
const testCurry = curry(test);
console.log(testCurry(1));
console.log(testCurry(3)(2));
