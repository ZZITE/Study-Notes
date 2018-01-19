## leetcode刷题与部分有趣的js题

* 760.Find Anagram Mappings

给定两个A和B的列表，B是A的一个字母组。B是A的一个字母组，意味着B是通过随机化A中元素的顺序而制成的。
我们希望找到一个从A到B的索引映射P.映射P [i] = j意味着A中的第i个元素出现在索引为j的B中。
这些列表A和B可能包含重复项。如果有多个答案，则输出它们中的任何一个。
ex: 
```
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
```
We should return
```
[1, 4, 3, 2, 0]
```
解:
```
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var anagramMappings = function (A, B) {
    let res = [ ];
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
```
更优解: 
```
var anagramMappings = function(A, B) {
    var r = [];
    A.forEach(item => r.push(B.indexOf(item)));
    return r;
};
```
思路：最后利用对象存储数值和下标，匹配A中的数字来解决。查看solution发现使用forEach可以快速解决问题。

* 关于 (a == 1 && a == 2 && a == 3)可能位true吗

解:
```
const a = {
    i: 1,
    valueOf: function () {
        return a.i ++;
    }
}
if (a == 1 && a == 2 && a == 3) {
    console.log('yes');
}
```
思路： 因为判断中使用的是“==”，当两个参数类型不同时会先进行类型转换。在上面的代码中，左边为对象右边为数字，在比较==两边的数据时，会先调用左边对象的valueOf方法将a进行转换，这里重写了对象a的valueOf方法实现每次调用都返回上一次加一的值。
但实际开发基本不会使用==，且ts的应用也时隐式转换的出现场景变的更少了。