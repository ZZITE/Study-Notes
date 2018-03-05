<template>
  <div class="content-wrap">
    <div class="content-title">
      <el-row class="block-col-2">
        <el-col :span="12">
          <span class="demonstration"></span>
          <el-dropdown trigger="click">
          <span class="el-dropdown-link">
            Sort By<i class="el-icon-caret-bottom el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>黄金糕</el-dropdown-item>
            <el-dropdown-item>狮子头</el-dropdown-item>
            <el-dropdown-item>螺蛳粉</el-dropdown-item>
            <el-dropdown-item>双皮奶</el-dropdown-item>
            <el-dropdown-item>蚵仔煎</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
        </el-col>
        <div class="title-right">
          <span>{{mes}}</span>
          <el-pagination class="pageNumber1" small layout="prev, pager, next" :total="50" @current-change="handleCurrentChange">
          </el-pagination>
        </div>
      </el-row>
    </div>


    <div class="contentUl">
      <ul>
        <li class="contentLi" v-for="(item, index) in goods" :key="index">
          <div class="contentDiv">
            <router-link to="/goods">
            <img class="contentImg" :src="item.src"/>
            <img class="contentImg2" :src="item.src2"/>
            </router-link>
          </div>
          <div class="contentDetail">
            <div class="dt1"><a>{{item.name}}</a></div>
            <div class="dt2"><a>{{item.itdus}}</a></div>
             <!-- 折扣 -->
            <div class="dt4" v-if="item.discount">
              $50
              <span class="dt4sp">{{item.price}}</span>
              <span class="sp123">
                Free Shipping
              </span>
            </div>

            <!-- 无折扣 -->
            <div class="dt3" v-else >{{item.price}}
              <span class="sp123">
                Free Shipping
              </span>
            </div>

          </div>
        </li>


      </ul>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      mes: '425 items in Tops',
      dt3: true,
      dt4: false,
      goods: [
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          src2: 'https://www.onlyfu.com/image/cache/catalog/dear/2017110902082259180769-300x400.jpg',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '$60',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '$66',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '$40',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '$65',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '$50',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
        {
          src: 'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/2016-6-21-dan/0594%20%281%29.JPG',
          name: 'Adidas',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          discount: '',
          price: '$70'
        },
      ]
    }
  },
  methods: {
    handleCurrentChange: function (val) {
      console.log(val)
      console.log(`当前页: ${val}`);
    }
  }
}
</script>

<style>
/* 图片切换hover */
.contentDiv img:hover {
    opacity: 0;
}
.contentDiv img{
    transition: 0.5s;
}
.contentImg2 {
  width: 200px;
  height: 300px;
}
.content-wrap {
  width: 100%;
  height: 100%;
  margin-top: -14px;
}
.content-title {
  height: 32px;
  position: relative;
  border-bottom: 1px solid #E5E5E5;
}
.block-col-2 {
  cursor: pointer;
}
.el-dropdown {
  margin-top: 4px;
}
.el-dropdown-menu {
  background: #fafafa;
}
.block-col-2 el-row {
  width: 200px;
}
.el-dropdown-link {
  font-size: 14px;
  color: #0F0F0F ;
}
.title-right {
  display: inline-block;
  position: absolute;
  height: 28px;
  line-height: 40px;
  width: 374px;
  right: 0;
  bottom: 2px;
  font-size: 14px;
  color: #0F0F0F;
}

.pageNumber1 {
  height: 16px;
  color: #0F0F0F 100%;
  background: #fafafa;
  float: right;
  bottom: 1px;
  left: 130px;
}
.pageNumber1 .el-pagination {
  padding: 8px 5px;
}
.pageNumber1 .el-pager li {
  background: #fafafa;
}
.pageNumber1 .el-pagination button.disabled {
  background: #fafafa;
}
.pageNumber1 .el-pagination .btn-next, .el-pagination .btn-prev {
  background: #fafafa;
}
.pageNumber1 .el-pager li.active {
  border-color: #fafafa;
  background-color: #fafafa;
  color: #E54C87;
  cursor: default;
}
.pageNumber1 .el-pager li:hover {
  color: #E54C87;
}
.pageNumber1 .el-pager li.btn-quicknext, .el-pager li.btn-quickprev {
    line-height: 22px;
}
.el-icon-arrow-right:hover {
  color: #E54C87;
}
.pageNumber1 .el-icon-arrow-left:hover {
  color: #E54C87;
}
.pageNumber1 .btn-next:hover {
  color:  #E54C87;
}

.contentUl {
  margin-left: -18px;
  margin-top: 10px;
  height: 100%;
}
.contentUl:after{
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;  
  }
.contentLi {
  margin-left: 19px;
  width: 200px;
  height: 380px;
  float: left;
}
.contentDiv {
  position: relative;
  width: 200px;
  height: 300px;
}
.contentDetail {
  height: 80px;
  width: 200px;
}
.dt1 .dt2 .dt3 {
  display:block;
  width: 188px;
  height: 25px;
}
.dt1 .dt3{
  color: #0F0F0F;
  font-size: 14px;
}
.dt2 {
  color: #595959 ;
  font-size: 12px;
}
.dt4 {
  color:#E54C87;
  font-size: 14px;
}
.dt4sp {
  margin-left: 2px;
  color: #595959 ;
  tab-size: 12px;
  text-decoration:line-through;
}
.sp123 {
  float: right;
  color: #0F0F0F;
  font-size: 12px;
}
.contentImg {
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  z-index: 1;
  background-color: #fff;
  margin: 0 auto;
}
.dt2 a {
  color: #595959;
}
.contentDetail a:hover {
  text-decoration: underline;
  color: #E54C87;
}
</style>