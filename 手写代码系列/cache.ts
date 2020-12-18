// 缓存函数
// 缓存函数是将函数的计算结果缓存起来，当下次以同样的参数调用该函数时，
// 直接返回已缓存的结果，而无需再次执行函数。这是一种常见的以空间换时间的性能优化手段。

// 在项目里和一些开源仓库的代码里都有很好的应用

function memorize(fn: Function) {
	const cache = Object.create(null);
	return (...args) => {
		const _args = JSON.stringify(args);
		return cache[_args] || (cache[_args] = fn.apply(this, args));
	};
}

const complexCalc = (a: number, b: number) => {
	console.log('do something');
	return a + b;
};

let memoCalc = memorize(complexCalc);
console.log(memoCalc(2, 3));
console.log(memoCalc(2, 3)); // 从缓存中取值，不再进行计算

// 附上 VUE源码里的cache
/**
 * Create a cached version of a pure function.
 */
// export function cached<F: Function> (fn: F): F {
//   const cache = Object.create(null)
//   return (function cachedFn (str: string) {
//     const hit = cache[str]
//     return hit || (cache[str] = fn(str))
//   }: any)
// }
