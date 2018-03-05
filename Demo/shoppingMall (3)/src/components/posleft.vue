<template>
<!-- 首页左侧导航快，点击对应a标签可以跳到首页的块 -->
<div>
    <!-- 橘黄色div块 -->
    <div v-show="isShow" class="commoditynavigation">
        <!-- 图片 -->
        <div class="title">
            <img style="float:left;margin-bottom:10px;margin-left: 2px;" src="static/images/navimg.png" alt="">
        </div>
        <!-- ul li v-for循环a连接 -->
        <ul>
            <li v-for="(nav,index) in navs" :key="index">
                <!-- 跳转连接参数(id) -->
                <a :href="nav.linkto">
                    <!-- 名字 -->
                    {{ nav.name }}
                </a>
            </li>
        </ul>
    </div>
    <!-- 隐藏出现事件图片 -->
     <img id="div1"  @click="showToggle" style="position:fixed;left:158px;top:33%;cursor:pointer" src="static/images/jiantou.png" alt="">
</div>
</template>

<script>
export default {
    data() {
        return {
            isShow:true,
            navs: [
                {
                    name: 'DAlLY DEALS',
                    linkto: '#swiper1'
                },
                {
                    name: 'Popular Categories',
                    linkto: '#PopularCategories'
                },
                {
                    name: 'What‘s Popular',
                    linkto: '#swiper'
                },
                {
                    name: 'The Trend Hub',
                    linkto: '#TheTrendHub1'
                },
                {
                    name: 'How To Wear',
                    linkto: '#HowToWear'
                },
                {
                    name: 'The Trend Hub',
                    linkto: '#TheTrendHub2'
                }
            ]
        }
    },
    methods: {
        // 隐藏出现事件函数
        showToggle:function(){  
            this.isShow = !this.isShow  
            if(this.isShow){  
                var div1 = document.getElementById("div1")
                div1.style.marginLeft = "0"
                this.btnText = "隐藏"
            }else{
                var div1 = document.getElementById("div1")
                div1.style.marginLeft = "-160px"
                this.btnText = "显示"  
            }  
        }  
    }
}
</script>

<style scoped>
/* 父级div样式 */
.commoditynavigation {
    position: fixed;
    width: 160px;
    height: 366px;
    top: 163px;
    background: #ffb400;
}
/* 包裹图片div的块 */
.title {
    width: 148px;
    height: 79px;
    background-size: 100% 100%;
}
/* a标签样式 */
.commoditynavigation a {
    display: block;
    float: left;
    font-size: 12px;
    width: 124px;
    height: 20px;
    padding: 6px 10px;
    margin: 4px 0;
    line-height: 20px;
    margin-left: 6px;
    border-radius: 3px;
    background: #ffddbf;
}
/* a标签鼠标移动上去的效果 */
.commoditynavigation a:hover {
    text-decoration: underline;
}
/* a标签鼠标点击之后的效果 */
.commoditynavigation a:active {
    background: #b36900;
    color: #fff!important;
}
</style>
