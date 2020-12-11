// Two Sum

// 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
// 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

// 示例:
// 给定 nums = [2, 7, 11, 15], target = 9
// 因为 nums[0] + nums[1] = 2 + 7 = 9
// 所以返回 [0, 1]

// 直接的暴力双循环
// 时间复杂度：O(N^2)
// 空间复杂度：O(1)

const twoSum = function (nums: number[], target: number) {
	for (let i = 0; i < nums.length; i++) {
		for (let j = i + 1; j < nums.length; j++) {
			if (nums[i] + nums[j] === target) {
				return [i, j];
			}
		}
	}
};

// 2. hashMap
// 时间复杂度: O(N)
// 空间复杂度: O(N)

const twoSum2 = function (nums: number[], target: number) {
	let result = [];
	let map = new Map();
	for (let i = 0; i < nums.length; i++) {
		map.set(nums[i], i);
	}
	for (let i = 0; i < nums.length; i++) {
		let anotherOne = target - nums[i];
		if (map.has(anotherOne) && map.get(anotherOne) !== i) {
			result.push(i);
			result.push(map.get(anotherOne));
			break;
		}
	}
	return result;
};
