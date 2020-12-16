namespace mediumDeepReadonly {
	//   实现一个通用的DeepReadonly<T>，它将对象的每个参数及其子对象递归地设为只读。

	// 您可以假设在此挑战中我们仅处理对象。数组，函数，类等都无需考虑。但是，您仍然可以通过覆盖尽可能多的不同案例来挑战自己。

	// 例如

	type X = {
		x: {
			a: 1;
			b: 'hi';
		};
		y: 'hey';
	};

	type Expected = {
		readonly x: {
			readonly a: 1;
			readonly b: 'hi';
		};
		readonly y: 'hey';
	};

	const todo: DeepReadonly<X> = {
    x: {
			a: 1,
			b: 'hi',
		},
		y: 'hey',
  }; // should be same as `Expected`

  // todo.y = '1';
  // todo.x.a = 2;

  // answer
	type DeepReadonly<T> = {
		readonly [K in keyof T]: T[K] extends Object ? DeepReadonly<T[K]> : T[K];
  };
  
  // 很容易想到递归解决，但是翻找答案的时候发现同样是递归，有一个更漂亮的写法，like:
  // type DeepReadonly<T> = keyof T extends never
  // ? T
  // : { readonly [k in keyof T]: DeepReadonly<T[k]> };
}
