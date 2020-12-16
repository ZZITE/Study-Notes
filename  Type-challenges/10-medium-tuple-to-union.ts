namespace mediumTupleRToUnion {
	//   实现泛型TupleToUnion<T>，它覆盖元组的值与其值联合。

	// 例如

	type Arr = ['1', '2', '3'];

	const a: TupleToUnion<Arr> = '1'; // expected to be '1' | '2' | '3'

	// answer
	type TupleToUnion<T extends ArrayLike<any>> = T[number];
}
