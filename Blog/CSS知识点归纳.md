### CSS选择器与常见属性



#### 选择器

* 元素选择器 : 通过HTML标签选择
* 类选择器 : 通过Class选择
* ID选择器 : ID
* 通用选择器 :  *
* 后代选择器 : h1 p {color:red;}
* 子选择器 : h1>strong {color:red;}
* 伪类选择器 : :checked
* 伪元素 : ::after



#### 常见属性

* font-family,font-weight,font-size
* text-indent,text-align,line-height,vertical-align
* width,heigth,padding,border,margin
* color,background
* position,float,overflow,display




#### position

* static : 默认值，指定元素在文档原本的位置
* relative : 相对定位，不脱离文档流;先放置在未添加定位时的位置再在不改变页面布局的前提下调整元素位置(原本的位置留下空白)
* absolute : 指定元素相对于最近的非static定位祖先元素偏移，脱离文档流
* fixed : 不为元素预留空间，相对于屏幕视口位置指定元素位置



#### 常见的CSS hack 

* 条件注释法 : <!--[if IE]>        只在IE生效
* 类内属性前缀法 : color:red\9\0      只对IE9/10生效
* 选择器前缀法 : .background-color/+background-color/-background-color  IE678/67/6