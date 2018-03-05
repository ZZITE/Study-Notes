<template>
<div  class="swiper-wrap">
  <el-carousel class="swiper" indicator-position="" height="300px" number="5000" trigger="click" arrow="never">
    <el-carousel-item v-for="(item,index) in items" :key="index">
      <table border="0" cellpadding="0" cellspacing="0" width="1060px">
        <tr>
          <transition-group name="fadeIn" tag="ul">
          <td v-for="(i,index) in item.imgUrl[0]" :key="index" style="width:20%;">

            <div class="contentDiv" style="width: 200px;height: 260px;position:relative;padding-right:20px;margin-top:10px;overflow:hidden;">
              <a>
                  <img class="contentImg" :src="i">
                  <img class="contentImg2" src="https://www.stylewe.com/image_cache/resize/450x600/image/catalog/8.15Cyanine-Sea/711C0180-4.JPG">
              </a>
            </div>
          </td>
          </transition-group>
        </tr>
      </table>
    </el-carousel-item>
  </el-carousel>
</div>
</template>
<script>
export default {
  name: 'swiper2',
  data () {
    return {
      show: true,
      a: -1,
      items: [
        {
          imgUrl: [
            [
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/8.15Cyanine-Sea/711C0180-1.JPG',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/LONYUASH-8.07/6282-5.JPG',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/JIANSHAN-9-6/T2767-5.JPG',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/8.11Fanny8/547703736264-6.jpg',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/8.22EVEN-THOUGH/HB316-5.jpg'
            ],
            [
            'https://www.stylewe.com/image_cache/resize/450x600/image/catalog/8.15Cyanine-Sea/711C0180-4.JPG',
            ''
            ]
          ],
          redirectUrl: 'http://www.baidu.com'
        },
        {
          imgUrl: [
            [
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/Juliet%20Roses%E6%96%B0%E5%93%8120170802%20-%20%E5%AE%8C%E6%88%90/B_40_513_1.jpg',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/LONYUASH-8.07/6282-5.JPG',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/JIANSHAN-9-6/T2767-5.JPG',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/8.11Fanny8/547703736264-6.jpg',
            'https://www.stylewe.com/image_cache/resize/250x333/image/catalog/8.22EVEN-THOUGH/HB316-5.jpg'
          ],
          [

          ]
          ],
          redirectUrl: 'http://www.douyu.com'
        }
      ]
    }
  },
  methods: {

  }
}
</script>

<style scoped>
  .swiper-wrap {
    background: #fafafa;
    text-align: center;
    height: 300px;
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
    color: #fff;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #fff;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #fff;
  }
  .el-carousel__button {
    width: 8px;
    height: 8px;
    display: inline-block;
    border-radius: 100%;
    opacity: .2;
  }
    .el-carousel__indicator {
    background-color: #000;
  }
  .el-carousel__indicator is-active {
    background-color: rgba(93, 11, 11, 0);
  }

/* 图片切换hover */
.contentDiv img:hover {
  opacity: 0;
}
img {
  transition: 0.5s;
  width: 200px;
  height: 260px;
    
}
.contentImg2 {
  width: 220px;
  height: 260px;
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
</style>