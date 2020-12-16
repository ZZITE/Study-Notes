// 对于给定的元组，您需要创建一个通用的Length，选择元组的长度

namespace easyTupleLength {
	// 例如
	type tesla = ['tesla', 'model 3', 'model X', 'model Y'];
	type spaceX = [
		'FALCON 9',
		'FALCON HEAVY',
		'DRAGON',
		'STARSHIP',
		'HUMAN SPACEFLIGHT'
	];

	type teslaLength = Length<tesla>; // expected 4
  type spaceXLength = Length<spaceX>; // expected 5
  
  // answer
  type Length<T extends ReadonlyArray<any>> = T['length']
}
