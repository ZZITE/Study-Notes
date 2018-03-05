<template>
  <div class="home">
    <swiper class="mt"></swiper>
    <substance></substance>
    <posleft></posleft>
  </div>
</template>

<script>
import swiper from '@/components/swiper'
import talkBox from '@/components/talkBox'
import substance from '@/components/substance'
import posleft from '@/components/posleft' 

export default {
  name: 'home',
  data () {
    return {
    }
  },
  components: {
    'swiper': swiper,
    'talkBox': talkBox,
    'substance': substance,
    'posleft': posleft
  },
  methods: {
    checkWebp: function () {
    try{
        return (document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp') == 0);
    }catch(err) {
        return false;
      }
    }
    /*
    supportWebp: function () {
      var d = document;
      var check = function() {
          var supportWebp;
          try {
              var ele = d.createElement('object');
              ele.type = 'image/webp';
              ele.innerHTML = '!';
              d.body.appendChild(ele);
              //奇妙所在,如果浏览器支持webp,那么这个object是不可见的(offsetWidth为0),
              //否则就会显示出来,有可视宽度.
              supportWebp = !ele.offsetWidth;
              d.body.removeChild(ele);
          }catch (err) {
              supportWebp = false;
          }
          return supportWebp;
      }
    }*/
  },
  mounted: function () {
    console.log(this.checkWebp()); 
    // console.log(this.supportWebp()); 
}

}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.mt {
  margin-top: 20px;
}
</style>
