// Valid Parentheses

// 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

// 有效字符串需满足：

// 左括号必须用相同类型的右括号闭合。
// 左括号必须以正确的顺序闭合。
// 注意空字符串可被认为是有效字符串。

// 示例 1:

// 输入: "()"
// 输出: true
// 示例 2:

// 输入: "()[]{}"
// 输出: true

const isValid = (s: string) => {
	const stack = [];
	const mapper = {
		'{': '}',
		'[': ']',
		'(': ')',
	};
	for (let i of s) {
		const v = i;
		if (['{', '[', '('].indexOf(v) > -1) {
			stack.push(v);
		} else {
			const peak = stack.pop();
			if (v !== mapper[peak]) {
				return false;
			}
		}
	}
	return stack.length === 0;
};
