<template>
  <div class="my">
    <ul class="myNav">
      <li v-for="(item,index) in nav" :key="index">
        <a :class="{'active': index == selected }" @click="tt(index)">{{item}}</a>
      </li>
    </ul>
    <keep-alive>
    <component class="my-right" :is="currentView"></component>
    </keep-alive>
  </div>
</template>

<script>
import profile from './profile'
import orders from './orders'
import favorites from './favorites'
export default {
  name: 'my',
  props:['page'],
  data () {
    return {
      selected: this.page,
      nav: ['Profile','My Orders','My Favorites','My Following','My Coupon','Contact Us','Contact Us','Change Password'],
      comp: ['profile','orders','favorites'],
      profile: "profile", //导航栏1
      orders: "orders", //导航栏2
      orders: "second", //导航栏2
      third: "third", //导航栏3
      currentView: 'favorites',//默认选中子组件
    }
  },
  components: {
    profile,
    orders,
    favorites
  },
  methods: {
    tt: function (index) {
      this.currentView = this.comp[index]
      this.selected = index
    }
  },
  watch: {
    currentView: function (newValue) {
      window.sessionStorage.setItem("curr", newValue)
    },
    selected: function (newValue) {
      window.sessionStorage.setItem("sele", newValue)
    },
  },
  created: function () {
    if(window.sessionStorage.getItem("curr")) {
      // 如果是点击情况下进入择根据传入参数
      if (this.page) {
        this.currentView = this.comp[this.page]
        this.selected = this.page
        } else {
            this.currentView = window.sessionStorage.getItem("curr")
            this.selected =  window.sessionStorage.getItem("sele")
        }
    }
    return
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.my {
  width: 100%;
  height: 100%;
}
.myNav {
  float: left;
  width: 200px;
}
.myNav li {
  height: 30px;
  line-height: 30px;
  font-size: 14px;
  border-top: 1px solid #E5E5E5;
}
.myNav :first-child {
  border: 0;
}
a:hover {
  color: #E54C87 ;
}
.my-right {
  margin: -24px 0 0 20px;
  float: left;
}
.active {
  color: #E54C87 !important;
}
.myNav a:hover{
  text-decoration: underline;
  text-decoration-style: solid 2px;
}
</style>