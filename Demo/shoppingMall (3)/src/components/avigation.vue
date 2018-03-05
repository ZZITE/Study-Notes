<template>
<!-- 导航页 -->
  <div class="loctionnav" id="nav" @mouseleave="childhidden">
    <div class="nav-loction">
      <ul>
          <li v-for="(list, index) in tabs" :key="index">
            <router-link class="linkTo" :to="list.to" @mouseenter.native="childShow(index)" @click="mouseenter()">  <!-- @mouseenter.native="childShow(index)-->
              {{list.text}}
            </router-link>
          </li>
          <!--<span><strong>|</strong></span>-->
          <li  v-for="(list,index) in nav" :key="index">
            <router-link class="linkTo" :to="'/Product/' + list.name">  <!-- @mouseenter.native="childShow(index)-->
              {{ list.name }}
            </router-link>
          </li>
      </ul>
    </div>
    <gate v-if="childshow" @mouseleave.native="childhidden"></gate>
  </div>
</template>

<script>
import axios from 'axios'
import gate from '@/components/navigate' //导航隐藏div组件
export default {
   components: {
      'gate': gate
  },
  data() {
    return {
      childshow: false,
      tabs: [
        { text: 'NEW IN', to:'/NEWIN' },
        { text: 'FLASH SAIE', to:'/Product/FLASHSAIE' },
        { text: 'DESIGNERS',to:'/Designers'}
      ],
      nav: []
    }
  },
  created() {
    window.addEventListener('scroll',this.menuFixed) //下拉绝对定位
  },
  methods: {
      menuFixed: function (nav){ //下拉绝对定位
      var obj = document.getElementById('nav');
      var scrolled = window.pageYOffset < 125;
      if (scrolled) {
        obj.style.position = 'static'
      } else {
          obj.style.position = 'fixed'
          obj.style.top = 0
      }
    },
    childShow: function (index) {
      console.log(1)
      if(index !== 0) {
        this.childshow = true;
      }
  },
    childhidden: function () {
      this.childshow = false;
    } 
  },
  mounted: function () {
    var self = this
    axios.get('/category?page=all&sort=order')
      .then(function (res) {
        self.nav = res.data.object_list
        console.log(res)
        /*
        setTimeout(function() {
        var num = self.nav.length + 3
        var wh = 1080/num
        var li = document.getElementsByClassName('abc')
        console.log(li)
        for (var i = 0; i < num; i++ ) {
          li[i].style.width = wh + 'px';
        }
      },10)
        */
      })
      .catch(function (err) {
        console.log(err)
      })
  }
}
</script>
<style scoped>
/* 导航最外层 */
.loctionnav {
  padding-top: 10px;
  position: relative;
  width: 100%;
  height: 26px;
  z-index: 1000;
  line-height: 10px;
  background: #fafafa;
}
/* 内层居中div */
.nav-loction {
  width: 1080px;
  margin: 0 auto;
  vertical-align: middle;
}
.nav-loction ul {
  float: left;
  margin-left: -3px;
  width: 1080px;
  height: auto;
  border-bottom: 1px solid #e5e5e5;
}
.nav-loction li {
  height: 20px;
  font-size: 14px;
  float: left;
  margin-right: 14px;
}
.nav-loction li:first-child {
  margin-left: 0;
}
/* 选中第16个li */

/* |线样式 */
.nav-loction strong {
  float: left;
  position: relative;
  left: 266px;
  top: -2px;
  color: #b7b7b7;
}
.linkTo:hover {
  color: #E54C87
}
.linkTo:focus {
  color: #E54C87
}
</style>