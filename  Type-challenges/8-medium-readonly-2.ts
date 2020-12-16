namespace mediumReadonly {
	//   实现一个通用MyReadonly<T, K>，它带有两种类型的参数T和K。

	// K指定应设置为Readonly的T的属性集。如果未提供K，则应使所有属性都变为只读，就像普通的Readonly<T>一样。

	// 例如

	interface Todo {
		title: string;
		description: string;
		completed: boolean;
	}

	const todo: MyReadonly<Todo> = {
		title: 'Hey',
		description: 'foobar',
		completed: false,
	};

	// todo.title = 'Hello'; // Error: cannot reassign a readonly property
	// todo.description = 'barFoo'; // Error: cannot reassign a readonly property
	// todo.completed = true; // OK

  // answer
	type MyReadonly<T, K extends keyof T = keyof T> = {
		readonly [P in K]: T[P];
	} &
		T;
}
