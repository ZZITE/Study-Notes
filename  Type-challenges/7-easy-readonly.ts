// 无需使用内置的Readonly<T>泛型即可。

// 构造一个类型，并将T的所有属性设置为只读，这意味着无法重新分配所构造类型的属性。

// 例如
namespace easyReadonly {
	interface Todo {
		title: string;
		description: string;
	}

	const todo: MyReadonly<Todo> = {
		title: 'Hey',
		description: 'foobar',
	};

	// todo.title = 'Hello'; // Error: cannot reassign a readonly property
  // todo.description = 'barFoo'; // Error: cannot reassign a readonly property
  
// answer 
	type MyReadonly<T> = { readonly [k in keyof T]: T[k] };
}
