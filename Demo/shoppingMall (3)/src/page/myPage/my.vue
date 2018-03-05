<template>
  <div class="my">
    <bread></bread>
    <!--<myNav :page="page"></myNav> -->
    <ul class="myNav">
      <li v-for="(item,index) in nav" :key="index"  @click="tt(index)">
        <router-link :class="{'active': index == select}" :to="item.to">{{item.name}}</router-link>
      </li>
    </ul>
    <keep-alive>
    <router-view class="yyy"></router-view>
    </keep-alive>
  </div>
</template>

<script>
import bread from '@/components/breadcrumb'
import myNav from './myNav'
export default {
  name: 'my',
  props:['page'],
  data () {
    return {
      // 获取路由传来的参数
      select: null,
      nav: [
        {
          name:'Profile',
          to: '/My/Profile'
        },
        {
          name: 'My Orders',
          to: '/My/Orders'
        },
        {
          name: 'My Favorites',
          to: '/My/Favorites'
        },
        {
          name: 'My Following',
          to: '/My/Following'
        },
        {
          name: 'My Coupon',
          to: '/My/Coupon'
        },
        {
          name: 'About Us',
          to: '/My/About'
        },
        {
          name: 'Contact Us',
          to: '/My/Contact'
        },
        {
          name: 'Change Password',
          to: '/My/Changepwd'
        },
        {
          name: 'Returns and Exchanges',
          to: '/My/Service'
        }
      ]
    }
  },
  components: {
    'bread': bread,
    //'myNav': myNav
  },
//:class="{'active': index == selected }
  methods: {
    tt: function (index) {
      this.select = index;
    }
  }/*,
  watch: {
    select: function (newValue) {
      window.sessionStorage.setItem("index", newValue)
    }
  },
  created: function () {
    if(window.sessionStorage.getItem("index")) {
      this.select =  window.sessionStorage.getItem("index")
    }
    else {
      this.select = 2;
    }
  }*/
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.my {
  height: 100%;
  width: 1080px;
  margin: 0 auto;
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
.myNav a:link {
  color: #0F0F0F;
}
.myNav a:hover {
  text-decoration: underline;
  text-decoration-style: solid 2px;
  color:#E54C87;
}
.yyy {
  width: 860px;
  height: 100%;
  margin-left: 220px;;
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


