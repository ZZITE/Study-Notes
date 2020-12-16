// 无需使用内置的Pick<T, K>泛型即可。

// 通过从K中选择属性T来构造类型

// 例如

namespace easyPick {
	interface Todo {
		title: string;
		description: string;
		completed: boolean;
	}

	type TodoPreview = MyPick<Todo, 'title' | 'completed'>;

	const todo: TodoPreview = {
		title: 'Clean room',
		completed: false,
	};

	// answer
	type MyPick<T, K extends keyof T> = { [key in K]: T[key] };
	// K属于T的子集，继承后约束，再遍历K，在T中取到对应的type
}
