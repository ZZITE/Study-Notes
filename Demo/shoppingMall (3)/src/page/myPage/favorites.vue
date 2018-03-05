<template>
<div class="fa-content-wrap">
    <div class="fa-header">
      My Favorites
    </div>
    <div class="fa-contentUl">
      <ul>


        <li class="fa-contentLi" v-for="(item, index) in goods" :key="index">
          <div class="fa-contentDiv">
            <router-link to="/goods">
            <img class="fa-contentImg" :src="item.src"/>
            </router-link>
          </div>
          <div class="fa-contentDetail">
            <div class="dt1"><a>{{item.name}}</a></div>
            <div class="dt2"><a>{{item.itdus}}</a></div>
             <!-- 折扣 -->
            <div class="dt4" v-if="item.discount">
              $50
              <span class="dt4sp">{{item.price}}</span>
              <span class="fa-sp">
                Free Shipping
              </span>
            </div>

            <!-- 无折扣 -->
            <div class="dt3" v-else >{{item.price}}
              <span class="fa-sp">
                Free Shipping
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <div class="fa-Pagination">
          <el-pagination class="fa-pageNumber" small layout="prev, pager, next" :total="50" @current-change="handleCurrentChange">
          </el-pagination>
        </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      dt3: false,
      dt4: true,
      goods: [
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.fa-content-wrap {
  width: 860px;
  position: relative;
}

.fa-header {
  margin-top: -14px;
  width: 100%;
  border-bottom: 1px solid #b7b7b7;
  font-size: 16px;
  color: #0F0F0F;
}
.fa-contentUl {
  margin-left: -18px;
  margin-top: 10px;
  height: 100%;
}
.fa-contentUl::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
.fa-contentLi {
  margin-left: 19px;
  width: 200px;
  height: 380px;
  float: left;
}
.fa-contentDiv {
  position: relative;
  width: 200px;
  height: 300px;
}
.fa-contentDetail {
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
.fa-sp {
  float: right;
  color: #0F0F0F;
  font-size: 14px;
}
.fa-contentImg {
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
.fa-contentDetail a:hover {
  text-decoration: underline;
}
.fa-Pagination {
  position: absolute; 
  left: 480px;
  top: -20px;
  width: 380px;
  height: 40px;
}
.fa-pageNumber {
  height: 16px;
  float: right;
  color: #0F0F0F 100%;
  background: #fafafa;
  margin-top: 10px;
}
.fa-pageNumber .el-pagination {
  padding: 8px 5px;
}
.fa-pageNumber .el-pager li {
  background: #fafafa;
}
.fa-pageNumber .el-pagination button.disabled {
  background: #fafafa;
}
.fa-pageNumber .el-pagination .btn-next, .el-pagination .btn-prev {
  background: #fafafa;
}
.fa-pageNumber .el-pager li.active {
  border-color: #fafafa;
  background-color: #fafafa;
  color: #E54C87;
  cursor: default;
}
.fa-pageNumber .el-pager li:hover {
  color: #E54C87;
}
.fa-pageNumber .el-icon-arrow-right:hover {
  color: #E54C87;
}
.fa-pageNumber .el-icon-arrow-left:hover {
  color: #E54C87;
}
.fa-pageNumber .btn-next:hover {
  color:  #E54C87;
}
</style>
