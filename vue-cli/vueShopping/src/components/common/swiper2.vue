<template>
<div class="swiper2-wrap">
  <el-carousel class="swiper2" indicator-position="" height="300px" number="5000" trigger="click" arrow="never">
    <el-carousel-item v-for="(item,index) in items" :key="index">
      <table border="0" cellpadding="0" cellspacing="0" width="1060px">
        <tr>
          <transition-group name="fadeIn" tag="ul">
          <td v-for="(i,index) in item.imgUrl[0]" :key="index" style="width:20%;">

            <div style="width: 200px;height: 260px;position:relative;padding-right:20px;margin-top:10px;overflow:hidden;">
              <a>
                <transition name="el-zoom-in-center">
                  <img :src="i" v-show="index !== a" @mouseenter="changeImg(index)">
                </transition>
                <transition name="el-zoom-in-center">
                  <img src="https://www.stylewe.com/image_cache/resize/450x600/image/catalog/8.15Cyanine-Sea/711C0180-4.JPG" @mouseleave="aa()">
                </transition>
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
    changeImg: function (index) {
      this.a = index
    },
    aa: function (ev) {
        this.a = -1
    }
  }
}
</script>

<style scoped>
  .swiper2-wrap {
    background: #fff;
    text-align: center;
    height: 300px;
    overflow: hidden;
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100%;
  }
  .swiper2 {
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
  img {
    width: 200px;
    height: 260px;
  }
  .fold-enter-active,.fold-leave-active {
      transition:all 0.5s
  }
    .fold-enter,.fold-leave {
      transform :translate3d(0,0,0);
    }
    .shopcart-list {
      position:absolute;
      transform:translate3d(0,-100%,0);
      top: 100%;
      z-index:-1;
      width:100%;
    }

</style>