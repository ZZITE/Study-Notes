// Find Anagram Mappings

// 给定两个A和B的列表，B是A的一个字母组。B是A的一个字母组，意味着B是通过随机化A中元素的顺序而制成的。
// 我们希望找到一个从A到B的索引映射P.映射P [i] = j意味着A中的第i个元素出现在索引为j的B中。
// 这些列表A和B可能包含重复项。如果有多个答案，则输出它们中的任何一个。
// ex:
// A = [12, 28, 46, 32, 50]
// B = [50, 12, 32, 46, 28]
// We should return
// [1, 4, 3, 2, 0]

const anagramMappings = function (A: number[], B: number[]) {
	let res = [];
	res.length = A.length;
	let m = {};
	for (let i = 0; i < B.length; i++) {
		m[B[i]] = i;
	}
	for (let i in A) {
		res[i] = m[A[i]];
	}
	return res;
};

const anagramMappings2 = function (A: number[], B: number[]) {
	var r = [];
	A.forEach((item) => r.push(B.indexOf(item)));
	return r;
};

// 思路：最后利用对象存储数值和下标，匹配A中的数字来解决。查看solution发现使用forEach可以快速解决问题。
