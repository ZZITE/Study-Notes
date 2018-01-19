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

模版字符串可以跟在一个函数后面，用于处理m这个模版字符串。这被称为标签模版功能。后面跟上的模版字符可以看作是函数的参数，如果模版字符中有变量，则会先对模版字符串进行处理成多个参数再调用。

```
let a = 5;
let b = 10;

tag`Hello ${ a + b } world ${ a * b }`;
// 等同于
tag(['Hello ', ' world ', ''], 15, 50);
```
模版字符串的一个应用就是过滤字符串，防止用户的恶意输入。 
```
let message =
  SaferHTML`<p>${sender} has sent you a message.</p>`;

function SaferHTML(templateData) {
  let s = templateData[0];
  for (let i = 1; i < arguments.length; i++) {
    let arg = String(arguments[i]);

    // Escape special characters in the substitution.
    s += arg.replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");

    // Don't escape special characters in the template.
    s += templateData[i];
  }
  return s;
}
```
上面的代码中sender是由用户输入，标签模版对它进行了处理，对特殊字符都进行了转义。

ES6还为原声生的字符串提供了一个raw方法,String.raw方法，往往用来充当模板字符串的处理函数，返回一个斜杠都被转义（即斜杠前面再加一个斜杠）的字符串，对应于替换变量后的模板字符串。
```
String.raw`Hi\n${2+3}!`;
// "Hi\\n5!"

String.raw`Hi\u000A!`;
// 'Hi\\u000A!'
```

### 数值的扩展

* 二进制和八进制的表示法

ES6 提供了二进制和八进制数值的新的写法，分别用前缀0b（或0B）和0o（或0O）表示。
```
0b111110111 === 503 // true
0o767 === 503 // true
```
将它们转化为十进制需要使用Number()方法。

* 新的方法
  * Number.isFinite() : 判断一个数值是否有限，参数非数值一律返回false,与isFinite()方法不同的是不会将其他类型的值转化为数值，而是直接返回false
  * Number.isNaN() : 判断参数结果是否为NAN，只有为NAN时返回true，其余一律返回false
  * Number.parseInt(), Number.parseFloat() 将全局的praseInt(),parseFloat()方法移植到Number上，这样做的好处是减少了全局使用，更加符合模块化。
  * Number.isInteger() : 用于判断一个数值是否为整数，对于非数值类型都返回false，Number.isInteger(1.0)返回true因为js内部整数和浮点数采用同样的存储方式。
需要注意的是，Number.isInteger(3.0000000000000002)这样的数虽然不是整数但依然会返回true,这是因为JavaScript 采用 IEEE 754 标准，数值存储为64位双精度格式，数值精度最多可以达到 53 个二进制位（1 个隐藏位与 52 个有效位）。如果数值的精度超过这个限度，第54位及后面的位就会被丢弃。类似的情况还有，如果一个数值的绝对值小于Number.MIN_VALUE（5E-324），即小于 JavaScript 能够分辨的最小值，会被自动转为 0。这时，Number.isInteger也会误判。因此如果对数据精度的要求较高，不建议使用Number.isInteger()判断一个数值是否为整数。
* Number.EPSILON() : 表示1与大于1的最小浮点数的差，对于64位浮点数来说相当于2的-52次方，Math.pow(2, -52)。它是js所能表达的最小数，小与这个数的值通常没有意义。引入一个这么小的量的目的，在于为浮点数计算，设置一个误差范围。我们知道浮点数计算是不精确的。
```
function withinErrorMargin (left, right) {
  return Math.abs(left - right) < Number.EPSILON * Math.pow(2, 2);
}

0.1 + 0.2 === 0.3 // false
withinErrorMargin(0.1 + 0.2, 0.3) // true

1.1 + 1.3 === 2.4 // false
withinErrorMargin(1.1 + 1.3, 2.4) // true
```
* 安全整数和 Number.isSafeInteger(): js中存在可以表达的整数上下限，为-2^53到2^53之间（不含两个端点）。超过这个范围则无法精准表达。
```
Math.pow(2, 53) // 9007199254740992

9007199254740992  // 9007199254740992
9007199254740993  // 9007199254740992

Math.pow(2, 53) === Math.pow(2, 53) + 1
// true
```
ES6 引入了Number.MAX_SAFE_INTEGER和Number.MIN_SAFE_INTEGER这两个常量，用来表示这个范围的上下限。

Number.isSafeInteger()则是用来判断一个整数是否落在这个范围内。

需要注意的是，在验证运算结果是否位安全整数的时候，应该先对参数运算的每个值进行验证，否则可能出现结果不准确的情况。
```
Number.isSafeInteger(9007199254740993 - 990)
// true
9007199254740993 - 990
// 返回结果 9007199254740002
// 正确答案应该是 9007199254740003
```
由于参与计算的被减数本身不属于安全数，在这里他会被当作9007199254740992存储，故而计算结果不准确。
* Math.trunc() : 用于将一个数的小数部分去除，只保留整数部分。
```
Math.trunc(4.9) // 4
Math.trunc(-4.1) // -4

// 对于非数字类型，内部先使用Number方法先进行转换
Math.trunc('123.456') // 123
Math.trunc(true) //1
Math.trunc(false) // 0
Math.trunc(null) // 0

//对于空值和无法转化的值，返回NAN
Math.trunc(NaN);      // NaN
Math.trunc('foo');    // NaN
Math.trunc();         // NaN
Math.trunc(undefined) // NaN
```

* Math.sign() : 用于判断一个数为正数、负数、还是零。它有5个返回值:
```
Math.sign(-5) // -1
Math.sign(5) // +1
Math.sign(0) // +0
Math.sign(-0) // -0
Math.sign(NaN) // NaN
```
如果参数是非数值，会自动转为数值。对于那些无法转为数值的值，会返回NaN。

