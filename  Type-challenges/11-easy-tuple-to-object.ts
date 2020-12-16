// 给定数组，转换为对象类型，键/值必须在给定数组中。

// 例如

namespace easyTupleToObject {
	const tuple = ['tesla', 'model 3', 'model X', 'model Y'] as const;

	const result: TupleToObject<typeof tuple> = {
		tesla: 'tesla',
		'model 3': 'model 3',
		'model X': 'model X',
		'model Y': 'model Y',
	}; // expected { tesla: 'tesla', 'model 3': 'model 3', 'model X': 'model X', 'model Y': 'model Y'}

	// answer
	type TupleToObject<T extends ReadonlyArray<any>> = {
		[K in T[number]]: K extends string | number ? K : never;
	};
}
