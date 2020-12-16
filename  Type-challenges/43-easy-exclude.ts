import { Equal, Expect } from './utils';

namespace easyExclude {
	//   实现内置的Exclude <T，U>
	// 从T中排除可分配给U的那些类型

	const t: MyExclude<'a' | 'b' | 'c', 'a'> = 'b';
	// anwser
	type MyExclude<T, U> = T extends U ? never : T;

	// test
	type cases = [
		Expect<
			Equal<MyExclude<'a' | 'b' | 'c', 'a'>, Exclude<'a' | 'b' | 'c', 'a'>>
		>,
		Expect<
			Equal<
				MyExclude<'a' | 'b' | 'c', 'a' | 'b'>,
				Exclude<'a' | 'b' | 'c', 'a' | 'b'>
			>
		>,
		Expect<
			Equal<
				MyExclude<string | number | (() => void), Function>,
				Exclude<string | number | (() => void), Function>
			>
		>
	];

	// 一开始理解成Omit, 吐血
	// Exclude<Type, ExcludedUnion>
	// Constructs a type by excluding from Type all union members that are assignable to ExcludedUnion.

	// Example
	// type T0 = Exclude<"a" | "b" | "c", "a">;
	//    ^ = type T0 = "b" | "c"
	// type T1 = Exclude<"a" | "b" | "c", "a" | "b">;
	//    ^ = type T1 = "c"
	// type T2 = Exclude<string | number | (() => void), Function>;
	//    ^ = type T2 = string | number
}
