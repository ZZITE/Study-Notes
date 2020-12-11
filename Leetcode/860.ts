// Lemonade Change

// 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
// 顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
// 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
// 注意，一开始你手头没有任何零钱。
// 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

// 示例 1：
// 输入：[5,5,5,10,20]
// 输出：true

// 示例 2：
// 输入：[5,5,10]
// 输出：true

// 示例 3：
// 输入：[10,10]
// 输出：false

const lemonadeChange = (bills: number[]) => {
	let n5 = 0;
	let n10 = 0;
	let i = -1;
	while ((++i, i < bills.length)) {
		if (bills[i] === 5) {
			n5++;
		} else if (bills[i] === 10) {
			n5--;
			n10++;
		} else {
			if (n10 > 0) {
				n10--;
				n5--;
			} else {
				n5 -= 3;
			}
		}
		if (n5 < 0) {
			return false;
		}
	}
	return true;
};
