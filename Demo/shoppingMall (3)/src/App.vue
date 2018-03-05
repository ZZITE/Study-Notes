<template>
  <div id="app">
    <homeHeader></homeHeader>
    <div class="appView">
    <transition name="el-fade-in-linear">
    <router-view class="appContent"></router-view>
    </transition>
    </div>
    <homeFoot class="appFooter"></homeFoot>
    <shortcut></shortcut>
  </div>
</template>

<script>
import homeFoot from '@/components/footer'
import homeHeader from '@/components/header'
import shortcut from '@/components/shortcut'
export default {
  name: 'app',
  components: {
    'homeFoot': homeFoot,
    'homeHeader': homeHeader,
    'shortcut': shortcut
  },
   watch:{
            '$route':function(to,from){
                document.body.scrollTop = '0'
            }
        }
}
</script>

<style>
  #app {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .2s
  }
.fade-enter, .fade-leave-to /* .fade-leave-active in below version 2.1.8 */ {
  opacity: 0
}
.appView {
  height: auto; min-height: 100%;
}
.appContent {
  padding-bottom: 300px;
}
.appFooter {
  position: relative;
  margin-top: -100px; /* footer高度的负值 */
  height: 250px;
  clear:both;
}
.transition-box {
    margin-bottom: 10px;
    width: 200px;
    height: 100px;
    border-radius: 4px;
    background-color: #20A0FF;
    text-align: center;
    color: #fff;
    padding: 40px 20px;
    box-sizing: border-box;
    margin-right: 20px;
  }

</style>
