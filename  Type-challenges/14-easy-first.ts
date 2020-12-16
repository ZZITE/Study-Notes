// 实现一个通用First<T>，它接受一个数组T并返回它的第一个元素的类型。

import { NotAny } from './utils';

// 例如

namespace easyFirst {
	type arr1 = ['a', 'b', 'c'];
	type arr2 = [3, 2, 1];

	type head1 = First<arr1>; // expected to be 'a'
	type head2 = First<arr2>; // expected to be 3

	// answer
  type First<T extends any[]> = '0' extends keyof T ? T[0] : never;
  
  // 需要判断数组是否为空 类似的方式还有 
  // T['length'] extends 0 ? never : T[0]   
  // T[0] extends never ?  never : T[0]

  // 看到一个比较好的写法，利用Ts的推断 infer
  // type First<T extends any[]> = T extends [infer X, ...infer Y] ? X : never ;
}
