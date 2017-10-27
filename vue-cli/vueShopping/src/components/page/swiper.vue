<template>
<div class="swiper-wrap">
  <el-carousel class="swiper" indicator-position="" height="450px" number="5000" trigger="click">
    <el-carousel-item v-for="(item,index) in items" :key="index">
    <a v-bind:href="item.redirectUrl">
    <img v-bind:src="item.imgUrl">
    </a>
    </el-carousel-item>
  </el-carousel>
</div>
</template>
<script>
export default {
  name: 'swiper',
  data () {
    return {
      items: [
        {
          imgUrl: 'https://www.stylewe.com/image_cache/resize/1060x1000/image/catalog/advertising/20170824BESTSELLER.jpg',
          redirectUrl: 'http://www.baidu.com'
        },
        {
          imgUrl: 'https://www.stylewe.com/image_cache/resize/1060x1000/image/catalog/advertising/20170824banner.jpg',
          redirectUrl: 'http://www.douyu.com'
        }
      ]
    }
  }
}
</script>

<style>
  .swiper-wrap {
    background: #f5f5f5;
    text-align: center;
    height: 450px;
    overflow: hidden;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }
  .swiper {
    width: 1080px;
    margin: 0 auto;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #e54c87;
  }
  .el-carousel__button {
    width: 8px;
    height: 8px;
    display: inline-block;
    border-radius: 100%;
    opacity: .2;
  }
  .el-carousel__button {
    background: #e54c87;
  }
</style>