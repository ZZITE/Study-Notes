// 给定两个字符串 s 和 t，它们只包含小写字母。

// 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

// 请找出在 t 中被添加的字母。

// 示例 1：

// 输入：s = "abcd", t = "abcde"
// 输出："e"
// 解释：'e' 是那个被添加的字母。
// 示例 2：

// 输入：s = "", t = "y"
// 输出："y"

// 这道题解法很多，第一直觉通过遍历第二个字符串，删除在第一个中找到的项，留下的就是不同
// 但是看到题解觉得自己写的太垃圾了，就不放上来了
// 下面放几个比较好的解法
const findTheDifference = function (s: string, t: string) {
	let i = -1,
		r = 0;
	while (++i < s.length) r ^= s.charCodeAt(i) ^ t.charCodeAt(i);
	return String.fromCharCode(r ^ t.charCodeAt(i));
};

const findTheDifference2 = function (s: string, t: string) {
	for (let i = 0; i < s.length; i++) t = t.replace(s[i], '');
	return t;
};

// 竟然直接相加找奇数，太坏啦！
const findTheDifference3 = function (s: string, t: string) {
	let r = s.concat(t);
	let str = 'abcdefghijklmnopqrstuvwxyz';
	for (let i = 0; i < str.length; i++) {
		let c = str.charAt(i);
		let re = new RegExp(c, 'g');
		let arr = r.match(re);
		if (arr && arr.length % 2 == 1) {
			return c;
		}
	}
};
