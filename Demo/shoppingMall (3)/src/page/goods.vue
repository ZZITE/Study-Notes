<template>
<!-- 购物选择页面 -->
    <div class="purchase">
        <bread></bread>
        <div style="margin-top:20px">
        <div class="thumbnail">
        <div class="main">
            <div style="float:left;" class="magnifier-box" id="magnifier1">
                <div class="magnifier-container"></div>
                <ul class="magnifier-thumb">
                    <li class="active"> 
                        <img @click="there" src="http://www.huanghanlian.com/widget/magnifier/img/c2.jpg" data-source="http://www.huanghanlian.com/widget/magnifier/img/c2a.jpg">
                    </li>
                    <li>
                        <img src="http://www.huanghanlian.com/widget/magnifier/img/macbook-small.jpg" data-source="http://www.huanghanlian.com/widget/magnifier/img/macbook-big.jpg">
                    </li>
                    <li>
                        <img src="http://www.huanghanlian.com/widget/magnifier/img/c2.jpg" data-source="http://www.huanghanlian.com/widget/magnifier/img/c2a.jpg">
                    </li>
                    <li>
                        <img src="http://www.huanghanlian.com/widget/magnifier/img/macbook-small.jpg" data-source="http://www.huanghanlian.com/widget/magnifier/img/macbook-big.jpg">
                    </li>
                        <li>
                        <img src="http://www.huanghanlian.com/widget/magnifier/img/c2.jpg" data-source="http://www.huanghanlian.com/widget/magnifier/img/c2a.jpg">
                    </li>
                </ul>
            </div>
        </div>
        </div>
        <div class="thumbnail-two">
            <h2>{{ there.collar }}</h2>
            <strong>{{ there.numberone }}</strong>
            <em>{{ there.numbertwo }}</em>
            <h4>Select Color</h4>
            <div class="quanfirt">
            <span class="pri-size" v-for="(color,index) in there.colors" :key="index">{{color}}</span>
            </div>
            <h4 style="float:left">Select Color</h4>
            <h3 style="float:right;margin: 20px 0 0 0;color:#595959;font-size:12px">{{ there.guide }}</h3>
            <div class="quandup">
                <span class="pri-size" v-for="(size,index) in there.sizes" :key="index">{{size}}</span>
            </div>
            <p style="float:left;font-size:12px;margin-top:8px;">{{ there.label }}</p>
            <div class="domper">
            <p>{{ there.free }}</p>
            <router-link to="/payment">
            <button class="btn-one">Click to buy</button>
            </router-link>
            <button class="btn-two">Click to buy</button>
            <h2 style="margin: 12px 0 12px 0">Easy 15 days Returns & Exchange</h2>
            </div>
            <h4 style="float:left;margin:0 20px 0 0;">Select Color</h4>
            <img style="float:left; margin-top:3px;" src="static/images/aixin.png" alt="">
            <div class="share">
                <h3>{{ there.are }}</h3>
                <span v-for="(shar,index) in there.shars" :key="index"></span>
            </div>
        </div>
        <div class="dmment">
            <ul style="float:left;margin-right:200px;">
                <h2>{{ there.tails }}</h2>
                <li v-for="(deta,index) in there.detas" :key="index">
                    {{ deta }}
                </li>
            </ul>
            <ul style="float:left;margin-right:200px;">
                <h2>{{ there.care }}</h2>
                <li v-for="(mater,index) in there.maters" :key="index">
                    {{ mater }}
                </li>
            </ul>
            
            <ul>
                <h2>{{ there.maril }}</h2>
                <li v-for="(terch,index) in there.terchs" :key="index">
                    {{ terch }}
                </li>
            </ul>
        </div>
        <div class="likenow">
            <p>{{ there.like }}</p>
            <span v-for="(also,index) in there.alsos" :key="index">
                <img class="contentImg" style="width:100%;height:100%;float:left;" :src="also.img1" alt="">
                <img class="contentImg2" style="width:100%;height:100%;float:left;" :src="also.img2" alt="">
            </span>
        </div>
        <div class="viewed">
            <p>{{ there.ntly }}</p>
            <span v-for="(vieviw,index) in there.vieviws" :key="index">
                <img class="contentImg" style="width:100%;height:100%;float:left;" :src="vieviw.img1" alt="">
                <img class="contentImg2" style="width:100%;height:100%;float:left;" :src="vieviw.img2" alt="">
            </span>
        </div>
        </div>
    </div>
</template>

<script>
import bread from '@/components/breadcrumb'
export default {
    name: 'goods',
    data() {
        return {
        there: {
                collar: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
                numberone: '$50',
                numbertwo: '$50',
                guide: 'Size Guide',
                label: 'Label Size XL, Shoulder:15.2,Bust:43.3,Sleeve Length:15.2,Length:35.4.(In inches).',
                free: '※Free Shipping',
                are: 'SHARE:',
                tails: 'Details',
                care: 'Material and Care',
                maril: 'Material and Care',
                like: 'YOU MAY ALSO LlKE',
                ntly: 'RECENTLY VIEWED',
                colors: [ 'red','blue','pink' ],
                sizes: [ 'S', 'M', 'XXL' ],
                shars: [ '1', 'black', '1','4'],
                detas: [ 'Navy blue top in a pattemed weave', 'Navy blue top in a pattemed weave','Navy blue top in a pattemed weave','Navy blue top in a pattemed weave' ],
                maters: [ 'Navy blue top in a patterned weave', 'Navy blue top in a patterned weave','Navy blue top in a patterned weave','Navy blue top in a patterned weave' ],
                terchs: [ 'Designer lris is talented in making', 'creations of runway style, super star', 'style, combining silk, organza, and' ],
                alsos: [
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Gray-Comfy-Cozy-Pocketed-Cardigan-LC27774-11-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017110902082259180769-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Green-Christmas-Suede-Deer-Patch-Aztec-Sleeve-Pocket-Hoodie-LC250678-9-24871-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017111220471684056484-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Brown-A-line-Casual-Fit-Christmas-Fashion-Sweater-LC27720-17-24623-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/20171031044920239156-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Apricot-Lace-up-Shoulder-Sweater-LC27688-18-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017101306261952344676-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/2017101306135958394769-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/Khaki-Cross-Back-Hollow-out-Sweater-LC27685-16-300x400.jpg'
                    },
                ],
                vieviws: [ 
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Black-Gold-Button-Slit-Bandage-Skirt-LC28457-2-21558-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017051117345549966418-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Burgundy-Drawstring-Cowl-Neck-Sweatshirt-Dress-LC250574-3-24803-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/201711090534596871260-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/Cute-Christmas-Reindeer-Knit-White-Hooded-Sweater-LC27785-1-24575-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/201710270339407813306-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/White-Floral-Print-Drawstring-Hoodie-LC250242-1-23915-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017092705311587294605-300x400.jpg'
                    },
                    {
                        img1: 'https://www.onlyfu.com/image/cache/catalog/dear/2017103003103281351066-300x400.jpg',
                        img2: 'https://www.onlyfu.com/image/cache/catalog/dear/Black-Christmas-Reindeer-Knit-Sweater-Winter-Jumper-LC27790-2-24602-300x400.jpg'
                    }
                ]

            }
        }
    },
    components: {
        bread
    },
    mounted () {
        (function() {
            var Magnifier = function(el, opts) {
            var self = this;
            var defaults = {
            event: "mouseover",
            }
            opts = opts || {};
            for (var w in defaults) {
            if ("undefined" == typeof opts[w]) {
            opts[w] = defaults[w];
            }
            }
            this.params = opts;
            this.container = r(el);
            if (this.container.length > 1) {
            var x = [];
            return this.container.each(function() {
            x.push(new Magnifier(this, opts))
            }), x
            }
            this.containers = this.container[0];
            this.contbox = this.container.find(".magnifier-container")[0];
            this.conmain = this.container.find(".magnifier-container")[0];
            this.init();
            }
            Magnifier.prototype = {
            init: function() {
            var self = this;
            this.rendDom();
            this.mark = this.container.find(".magnifier-mark")[0];
            this.float_box = this.container.find(".magnifier-float-box")[0];
            this.big_box = this.container.find(".magnifier-big-box");
            this.small = this.container.find(".magnifier-small")[0];
            this.big_Image = this.big_box.find("img")[0];
            this.event();
            },
            //渲染dom
            rendDom: function() {
            var self = this;
            var initimg = this.container.find(".magnifier-thumb li img")[0].getAttribute("src");
            var initimgs = this.container.find(".magnifier-thumb li img")[0].getAttribute("data-source");
            var small = document.createElement("div");
            small.className = "magnifier-small";
            var mark = document.createElement("div");
            mark.className = "magnifier-mark";
            var float = document.createElement("div");
            float.className = "magnifier-float-box";
            var img = document.createElement("img");
            img.setAttribute("src", initimg)
            small.appendChild(mark);
            small.appendChild(float);
            small.appendChild(img);
            var big_box = document.createElement("div");
            big_box.className = "magnifier-big-box";
            var boximg = document.createElement("img");
            boximg.setAttribute("src", initimgs);
            big_box.appendChild(boximg);
            this.conmain.appendChild(small);
            this.conmain.appendChild(big_box);
            this.boximg = this.container.find(".magnifier-small img")[0];
            this.tabimg();
            },
            //执行切换图片
            tabimg: function() {
            var self = this;
            this.tabimgs = this.conmain = this.container.find(".magnifier-thumb li");
            for (var i = 0; i < this.tabimgs.length; i++) {
            self.tabimgs[i].addEventListener(this.params.event, function() {
            for (var j = 0; j < self.tabimgs.length; j++) {
            self.tabimgs[j].className = "";
            }
            this.className = "active";
            var onec = this.children[0].getAttribute("src");
            var onecd = this.children[0].getAttribute("data-source");
            self.change(onec, onecd);
            }, false);
            }
            },
            //改变大小图片
            change: function(o, b) {
            this.boximg.setAttribute("src", o);
            this.big_Image.setAttribute("src", b);
            },
            //执行初始化鼠标事件
            event: function() {
            var self = this;
            self.mark.addEventListener('mouseover', function() {
            self.float_box.style.display = "block";
            self.big_box[0].style.display = "block";
            }, false);
            self.mark.addEventListener('mouseout', function() {
            self.float_box.style.display = "none";
            self.big_box[0].style.display = "none";
            }, false);
            self.mark.addEventListener('mousemove', function(e) {
            var e = e || window.event; //兼容多个浏览器的event参数模式
            self.moveevent(e)
            }, false);
            },
            //开始移动
            moveevent: function(e) {
            var self = this;
            var left = e.clientX - this.contbox.offsetLeft - this.small.offsetLeft - this.float_box.offsetWidth / 2;
            var top = e.clientY - this.contbox.offsetTop - this.small.offsetTop - this.float_box.offsetHeight / 2;
            if (left < 0) {
            left = 0;
            } else if (left > (this.mark.offsetWidth - this.float_box.offsetWidth)) {
            left = this.mark.offsetWidth - this.float_box.offsetWidth;
            }
            if (top < 0) {
            top = 0;
            } else if (top > (this.mark.offsetHeight - this.float_box.offsetHeight)) {
            top = this.mark.offsetHeight - this.float_box.offsetHeight;
            }
            this.float_box.style.left = left + "px";
            this.float_box.style.top = top + "px";
            var percentX = left / (this.mark.offsetWidth - this.float_box.offsetWidth);
            var percentY = top / (this.mark.offsetHeight - this.float_box.offsetHeight);
            this.big_Image.style.left = -percentX * (this.big_Image.offsetWidth - this.big_box[0].offsetWidth) + "px";
            this.big_Image.style.top = -percentY * (this.big_Image.offsetHeight - this.big_box[0].offsetHeight) + "px";
            }
            }
            var r = (function() {
            var e = function(e) {
            var a = this,
            t = 0;
            for (t = 0; t < e.length; t++) {
            a[t] = e[t];
            }
            return a.length = e.length, this
            };
            e.prototype = {
            addClass: function(e) {
            if ("undefined" == typeof e) return this;
            for (var a = e.split(" "), t = 0; t < a.length; t++)
            for (var r = 0; r < this.length; r++) this[r].classList.add(a[t]);
            return this
            },
            each: function(e) {
            for (var a = 0; a < this.length; a++) e.call(this[a], a, this[a]);
            return this
            },
            html: function(e) {
            if ("undefined" == typeof e) return this[0] ? this[0].innerHTML : void 0;
            for (var a = 0; a < this.length; a++) this[a].innerHTML = e;
            return this
            },
            find: function(a) {
            for (var t = [], r = 0; r < this.length; r++)
            for (var i = this[r].querySelectorAll(a), s = 0; s < i.length; s++) t.push(i[s]);
            return new e(t)
            },
            append: function(a) {
            var t, r;
            for (t = 0; t < this.length; t++)
            if ("string" == typeof a) {
            var i = document.createElement("div");
            for (i.innerHTML = a; i.firstChild;) this[t].appendChild(i.firstChild)
            } else if (a instanceof e)
            for (r = 0; r < a.length; r++) this[t].appendChild(a[r]);
            else this[t].appendChild(a);
            return this
            },
            }
            var a = function(a, t) {
            var r = [],
            i = 0;
            if (a && !t && a instanceof e) {
            return a;
            }
            if (a) {
            if ("string" == typeof a) {
            var s, n, o = a.trim();
            if (o.indexOf("<") >= 0 && o.indexOf(">") >= 0) {
            var l = "div";
            for (0 === o.indexOf("<li") && (l = "ul"), 0 === o.indexOf("<tr") && (l = "tbody"), (0 === o.indexOf("<td") || 0 === o.indexOf("<th")) && (l = "tr"), 0 === o.indexOf("<tbody") && (l = "table"), 0 === o.indexOf("<option") && (l = "select"), n = document.createElement(l), n.innerHTML = a, i = 0; i < n.childNodes.length; i++) r.push(n.childNodes[i])
            } else
            for (s = t || "#" !== a[0] || a.match(/[ .<>:~]/) ? (t || document).querySelectorAll(a) : [document.getElementById(a.split("#")[1])], i = 0; i < s.length; i++) s[i] && r.push(s[i])
            } else if (a.nodeType || a === window || a === document) {
            r.push(a);
            } else if (a.length > 0 && a[0].nodeType) {
            for (i = 0; i < a.length; i++) {
            r.push(a[i]);
            }
            }
            }
            return new e(r)
            };
            return a;
            }())
            window.magnifier = Magnifier;
            })()
            new magnifier("#magnifier1");
            }
        }
</script>
<style>
.purchase{
    width: 1080px;
    margin: 0 auto;
    height: 1400px;
}
.rember {
    font-size: 12px;
    color: #595959;
    margin-top: 10px;
}
.thumbnail {
    float: left;
    width: 457px;
    height: 470px;
    margin: 10px 20px 0 2px;
}
.thumbnail-two {
    float: left;
    width: 483px;
    height: 462px;
    margin-top: 20px;
}
.thumbnail-two h2 {
    float: left;
    margin-bottom: 20px;
    font-size: 16px;
    color: #0F0F0F;
}
.thumbnail-two strong { 
    margin-right: 10px;
    font-size: 18px;
    color: #E54C87;
}
.thumbnail-two em {
    text-decoration: line-through;
    color: #595959;
}
.thumbnail-two .quanfirt {
    float: left;
    width: 100%;
    margin-left: 10px;
}
.pri-size {
    float: left;
    display: block;
    padding: 0 24px;
    height: 36px;
    margin: 5px 10px 0 0;
    border: 1px solid #ccc;
    font-size: 16px;
    text-align: center;
    line-height: 36px;
}
.pri-size:visited {
    border: 1px solid #E54C87;
    color: #E54C87; 
}
.pri-size:hover {
    border: 1px solid #E54C87;
}
.pri-size:active {
    border: 1px solid #E54C87;
    color: #E54C87;
}
.thumbnail-two h4 {
    margin-top: 15px;
}
.thumbnail-two .quandup {
    float: left;
    width: 100%;
    margin-left: 10px;
}   
.domper {
    float: left;
    width: 100%;
    margin-top: 20px; 
}
.domper p {
    font-size: 14px;
    color:#0F0F0F;
    margin-bottom: 20px;
}
.btn-one {
    float: left;
    width: 210px;
    height: 50px;
    margin-right: 20px;
    outline:0;
    color: #E54C87;
    border: 0;
    font-size: 16px;
}
.btn-one:active {
    border: 1px solid #E54C87;
}
.btn-two:active {
    border: 1px solid #b7b7b7;
}
.btn-two {
    float: left;
    width: 210px;
    height: 50px;
    outline:0;
    border: 0;
    font-size: 16px;
    color: white;
    background: #E54C87;
}
.share {
    float: left;
    top: 30px;
    left: -110px;
    position: relative;
}
.share h3 {
    float: left;
    margin-top: 5px;
}
.share span {
    float: right;
    margin: 0 0 0 10px;
    border-radius: 0;
    background: pink;
    width: 20px;
    height: 20px;
}
.dmment {
    float: left;
    width: 100%;
    height: 109px;
    margin-top: 30px;
    padding: 30px 0;
    border-top: 1px solid #b7b7b7;
    border-bottom: 1px solid #b7b7b7;
}
.dmment h2 {
    font-size: 14px;
    font-weight: bold;
    color: #0F0F0F;
}
.likenow {
    float: left;
    width: 1080px;
    height: 290px;
    padding: 30px 0;
    border-bottom: 1px solid #b7b7b7;
}
.likenow p {
    text-align: center;
    font-size: 26px;
    color: #0F0F0F;
}
.likenow span {
    display: block;
    float: left;
    width: 200px;
    height: 245px;
    margin-right: 20px;
    background: black;
}
.likenow span:nth-child(6) {
    margin-right: 0;
}
.viewed {
    float: left;
    width: 1080px;
    height: 290px;
    padding: 30px 0;
}
.viewed p {
    text-align: center;
    font-size: 26px;
    color: #0F0F0F;
}
.viewed span {
    display: block;
    float: left;
    width: 200px;
    height: 245px;
    margin-right: 20px;
    background: #872f2f;
}
.viewed span:nth-child(6) {
    margin: 0;
}

/* 缩略图样式 */
.main {
    width:457px;
    height: 470px;
}
 /*公共*/
.magnifier-container {
    float:right;
    width: 366px;
    height: 470px;
    position: relative;

}
.magnifier-small{
    position: relative;
    z-index: 1;
    width: 366px;
    height: 100%;
}
.magnifier-small img{
    /*max-width: 100%;
    max-height: 100%;*/
    width: 366px;
    height: 470px;
}
.magnifier-mark {
    position: absolute;
    display: block;
    width: 366px;
    height: 470px;
    background-color: #fff;
    filter: alpha(opacity:0);
    opacity: 0;
    z-index: 10;
}
.magnifier-mark:hover {
    cursor: move   
}
.magnifier-float-box {
    display: none;
    width: 160px;
    height: 120px;
    position: absolute;
    background: #fff;
    border: 2px solid #fff;
    filter: alpha(opacity:0.6);
    opacity: 0.6;
}
.magnifier-big-box {
    display: none;
    position: absolute;
    top: 0;
    float:left;
    left: 386px;
    width: 400px;
    height: 400px;
    overflow: hidden;
    border: 1px solid #ccc;
    z-index: 1;
}
.magnifier-big-box img {
    position: absolute;
    z-index: 5;
}
.magnifier-thumb {
    float: left;
    width: 72px;
    height: 470px;
    margin: 0 19px 0 0;
    padding: 0;
}
.magnifier-thumb li {
    display: inline-block;
    width: 70px;
    height: 84px;
    vertical-align: middle;
    line-height: 50px;
    margin-bottom: 10px;
    /*display: table-cell;*/
}
.magnifier-thumb img:hover {
    border: 2px solid #E54C87;
}
.magnifier-thumb li:nth-child(5) {
    margin: 0;
}
.magnifier-thumb li img {
    max-width: 70px;
    height: 86px;
    vertical-align: middle;
}
/* 图片切换hover */
.likenow img:hover {
    opacity: 0;
}
.viewed img:hover {
    opacity: 0;
}
.viewed img {
    transition: 0.5s;
    width: 200px;
    height: 260px;
}
.likenow img {
    transition: 0.5s;
    width: 200px;
    height: 260px;
}
.contentImg2 {
    position: relative;
    top: -245px;
    width: 220px;
    height: 260px;
}
.contentImg {
    width: 100%;
    height: 100%;
    bottom: 0;
    left: 0;
    position: relative;
    right: 0;
    top: 0;
    z-index: 1;
    background-color: #fff;
    margin: 0 auto;
}
</style>