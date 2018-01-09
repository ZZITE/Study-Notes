### 字符串的扩展

* ES6为字符串添加了遍历器接口，使得字符串可以被for...of循环遍历
```javascript
for (let codePoint of 'foo') {
  console.log(codePoint);
}
```

* 过去通常使用indexOf的方法来判断一个字符串是否包含在另一个字符串中,ES6又提供了三种方法
  
  * includes() : 返回布尔值，表示是否找到了参数字符串。
  * startsWith() : 返回布尔值，表示参数字符串是否在原字符串的头部。
  * endsWith(): 返回布尔值，表示参数字符串是否出现在原字符串的尾部。

三种方法都支持第二个参数，用来指定开始搜索的位置。
```javascript
let s = 'Hello world!';
s.startsWith('world', 6) // true
s.endsWith('Hello', 5) // true
s.includes('Hello', 6) // false
```
其中endsWith的第二个参数表示针对前n个字符，其他两个则表示从第n个字符串开始直到结束。

* repeat()
repeat()方法返回一个新的字符串，表示将原字符串重复n次。
参数是小数时将被取整，负数或者infinity会报错。NAN、0-1之间的小数等同于0。参数为字符串将先转化为数字。

* padStart(), padEnd()
ES6引入了字符串补全长度的功能，如果某个字符串不够指定的长度，会在头部或者尾部补全。
```javascript
'x'.padStart(5, 'ab') // 'ababx'
'x'.padStart(4, 'ab') // 'abax'
'x'.padEnd(5, 'ab') // 'xabab'
'x'.padEnd(4, 'ab') // 'xaba'
```
其中第一个参数用来指定字符串的最小长度，第二个参数用来补全字符串。

常见的用途是为数值补全指定位数或提示字符串格式
```javascript
'1'.padStart(10, '0') // "0000000001"
'12'.padStart(10, 'YYYY-MM-DD') // "YYYY-MM-12"
```

* 模版字符串

ES6引入了模版字符串用来解决过往输出模版的不便。模版字符串是增强版的字符串，用反引号 ` ` ` 标识。它可以当做普通的字符串使用，也可以用来定义多行字符串，或者在字符串中嵌入变量。
```javascript
// 普通字符串
`In JavaScript '\n' is a line-feed.`

// 多行字符串
`In JavaScript this is
 not legal.`

console.log(`string text line 1
string text line 2`);

// 字符串中嵌入变量
let name = "Bob", time = "today";
`Hello ${name}, how are you ${time}?`
```
多行字符串的空格换行都可以被保留在输出中。模板字符串中嵌入变量，需要将变量名写在${}之中。${}之中可以放入任意的js表达式，引用对象甚至调用函数等。

* 标签模版

