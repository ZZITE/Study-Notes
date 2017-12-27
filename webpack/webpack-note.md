# webpack learnning notes

## About 
  关于webpack, 伴随着快速的版本更新, 也渐渐成为前端开发中的一项主要生产力, 作为一个合格的前端工程师, 你也许对使用它没那么熟练(毕竟配置使用确实过于繁琐, 官方的说明也比较匮乏), 但如果对其一无所知, 那就说不过去了。本篇文章是我自己学习webpack过程中的一些笔记, 整合成对于webpack基础学习的。

  在学习之前首先对webpack有个初步的认识。
  
  如果把前端的网页看作是一个应用, 而我们通常需要一堆复杂的js代码以及各种依赖包, 外部文件, 去构建它。使用webpack的一大作用就如同图片所示, 模块化的特点可以让你将一个复杂的项目细化为文件, 不仅仅是js,作为一个`module bundler`, webpack最终会将你需要的一切打包成一个或多个`bundler`  
  ![image](https://doc.webpack-china.org/bf093af83ee5548ff10fef24927b7cd2.svg)
  同时你可以在webpack愉快的使用typescript、sass等浏览器原先并不支持的扩展开发语言, 因为webpack最终都会将将其转换和打包为合适的格式供浏览器使用。

  在3.0之后, webpack还在很大程度上肩负起了前端项目优化的责任。
  
## Install

```
//全局安装
npm install -g webpack
```
webpack支持全局安装, 但官方并不推荐。试想当你将其全局安装后, 版本都将锁定在一个上, 而不同的项目中实际上可能用了不同版本的webpack, 这样一来将产生一些不必要的冲突。所以我们应该尽可能在单个项目去安装webpack。

首先创建一个文件夹`webpack_note`
, 在文件目录下执行
```
npm init
```
根据提示初始化项目, 生成一个package,json文件, 用于说明和描述你的这个项目(包含你的信息, 项目模块等)
```
npm install --save-dev webpack
```
`--save`将其保存到package.json中 `-dev`只得是只在开发环境中使用, 生产环境中不使用

这一步是将webpack安装到当前的项目中, 通过package.json你可以看到多出了这一项
```
"devDependencies": {
    "webpack": "^3.10.0"
  }
```
同时, 输入`webpack -v`也可以查看安装情况和版本号

这里你也许会遇到一个版本更新遇到的问题。当你使用了旧版本的webpack, 而你想将它更新的话, 你只要将项目文件中的`node_modules`文件夹删除后重新安装webpack即可。但如果是一个老旧的项目,在已经存在许多依赖的情况下, 而你想要更新他的webpack版本, 这时候你需要在package.json文件中找到我们`"webpack": "^3.10.0"`将其中的版本号改为你需要的版本, 然后再将`node_modules`文件夹删除, 最后使用
```
npm install
```
它将会根据你的package.json去加载所需的依赖。


## Usage

### 基本的webpack结构
webpack的使用和打包大多依赖于webpack.config.js的配置。正确使用webpack的姿势,首先在根目录下新建一个webpack.config.js文件, 内容如下
```
module.exports={
    //入口文件的配置项
    entry:{},
    //出口文件的配置项
    output:{},
    //模块：例如解读CSS,图片如何转换，压缩
    module:{},
    //插件，用于生产模版和各项功能
    plugins:[],
    //配置webpack开发服务功能
    devServer:{}
}
```
以上便是一个没有内容的标准webpack配置模版

* entry：配置入口文件的地址，可以是单一入口，也可以是多入口。
* output：配置出口文件的地址，在webpack2.X版本后，支持多出口配置。
* module：配置模块，主要是解析CSS和图片转换压缩等功能。
* plugins：配置插件，根据你的需要配置不同功能的插件。
* devServer：配置开发服务功能，后期我们会详细讲解。

这里简单举一个多出口文件的例子

首先在src文件夹下新建`entry.js`, `entry2.js`, `index.html`三个文件
* index.html
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>webpack</title>
</head>
<body>
    <h2 id="title"></h2>
    <div id="content"></div>
</body>
</html>
```
* entry.js
```
document.getElementById('title').innerHTML = 'hello word'
```
* entry2.js
```
document.getElementById('content').innerHTML = 'hello word'
```
更改webpack.config.js中
```
entry: {
    entry: './src/entry.js',
    entry2: './src/entry2.js'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].js'
  }
```
别忘了在顶端加上`const path = require('path');`

此时我们就定义好了一个简单的出入口文件关系,在终端输入`webpack`就会进行打包, dist目录下多出了打包好的index.html, entry.js, entry2.js三个文件。

那么, 要如何预览我们在开发过程中的成果呢, webpack提供了热更新功能, 只需要做以下配置

修改webpack.config.js
```
    devServer:{
        //设置基本目录结构
        contentBase:path.resolve(__dirname,'dist'),
        //服务器的IP地址，可以使用IP也可以使用localhost
        host:'localhost',
        //服务端压缩是否开启
        compress:true,
        //配置服务端口号
        port:1717
    }
```
* contentBase:配置服务器基本运行路径，用于找到程序打包地址。
* host：服务运行地址，建议使用本机IP，这里为了讲解方便，所以用localhost。
* compress：服务器端压缩选型，一般设置为开启，如果你对服务器压缩感兴趣，可以自行学习。
* port：服务运行端口，建议不使用80，很容易被占用，这里使用了1717.

然后安装webpack-dev-server
```
npm install webpack-dev-server --save-dev
```
最后修改package.json
```
"scripts": {
    "server":"webpack-dev-server"
 },
```
这时候在终端运行`npm  run  server`就可以打开服务器,到浏览器中查看效果了。

### CSS文件打包

Webpack在生产环境中有一个重要的作用就是减少http的请求数, 就是把多个文件打包到一个js里, 这样请求数就可以减少好多。这里说下怎么打包文件夹里的CSS文件到js文件中。

#### Loaders
这里终于涉及到webpack的一个核心功能Loaders啦。通过使用不同的loader, webpack通过调用外部的脚本或工具可以对各种各样的格式的文件进行处理, 例如：
* 可以把SASS文件的写法转换成CSS，而不在使用其他转换工具。
* 可以把ES6或者ES7的代码，转换成大多浏览器兼容的JS代码。
* 可以把React中的JSX转换成JavaScript代码。
这里我们用它来做CSS文件的打包, 首先在src目录下新建一个CSS文件夹, 添加一个index.css文件
```
body {
color: #fff;
background: #ccc;
}
```
在entry.js文件中引入它
```
import css from './css/index.css';
```
然后就是使用所需的loader来解析啦。首先安装：
```
npm install style-loader --save-dev
npm install --save-dev css-loader
```
其中style-loader:它是用来处理css文件中的url()等

css-loader：它是用来将css插入到页面的style标签
安装后在webpack.config.js做相应的配置
```
module:{
        rules: [
            {
              test: /\.css$/,
              use: [ 'style-loader', 'css-loader' ]
            }
          ]
    },
```
所有的loader在使用时都要做单独的配置, 这之中几个字段
* test：用于匹配处理文件的扩展名的表达式，这个选项是必须进行配置的；
* use：loader名称，就是你要使用模块的名称，这个选项也必须进行配置，否则报错；
* include/exclude:手动添加必须处理的文件（文件夹）或屏蔽不需要处理的文件（文件夹）（可选）；
* query：为loaders提供额外的设置选项（可选）。

这时, css文件就被正确的引入到项目中,并且在生产环境中正确打包到entry.js文件中。

### 压缩js代码
在生产环境中, 我们通常需要压缩js代码来提升性能。在Webpack中可以很轻松的通过插件来实现JS代码的压缩。
首先需要在webpack.config.js中引入`uglifyjs-webpack-glugin`插件
```
const uglify = require('uglifyjs-webpack-plugin');
```
引入后在plugins配置里new一个 uglify对象就可以了
```
 plugins:[
        new uglify()
    ],
```
这时候在使用`webpack` 打包后会发现js代码已经被压缩了。

    

