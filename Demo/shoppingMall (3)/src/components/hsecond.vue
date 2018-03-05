<template>
<!-- 导航中间部分 -->
  <div class="secondheader">
      <!-- logo和input结构 -->
      <div class="secondheader-nav" @mouseleave="mylistshow = false;">
          <a :href="url"><img class="funtter" v-bind:src="pictt" alt=""></a>
            <el-input
                placeholder="Search..."
                icon="search"
                v-model="input2"
                :on-icon-click="handleIconClick">
            </el-input>
            <!-- 用户和语言购物车结构 -->
            <ul class="banana" style="position:relative;margin-right: 2px;">
                <li @mouseover="mylistshow = true" ><strong>|</strong><router-link :to=to>{{loginName}}</a></router-link>

                <div class="my-list" v-if="mylistshow" @mouseleave="mylistshow = true;">
                    <span><em></em></span>
                    <ul>
                      <li v-for="(list, index) in mylist" :key="index" @click="mylistshow = false;deltoken(index)">
                        <router-link :to="list.to">
                            {{list.text}}
                        </router-link>
                      </li>
                    </ul>
                </div>

                </li>
                <!-- 路由传参 -->
                <li><strong>|</strong><router-link :to="{ path: '/My/Favorites', params: { page: 2 }}"><i style="font-size: 16px;" class="fa fa-star-o" aria-hidden="true"></i></router-link></li>
                <li><strong>|</strong><router-link to="/Cart"><i style="font-size: 16px;" class="fa fa-shopping-bag" aria-hidden="true"></i></router-link></li>
            </ul>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            token: null,
            mylistshow: false,
            to: null,
            loginName: null,
            input2: '',
            url: '/',
            pictt: 'static/images/wenzi.png',
            mylist: [
                {
                    text: 'My Orders',
                    to: '/My/Orders'
                },
                {
                    text: 'My Favorites',
                    to: '/My/Favorites'
                },
                {
                    text: 'My Following',
                    to: '/My/Following'
                },
                {
                    text: 'My Coupon',
                    to: '/My/Contact'
                },
                {
                    text: 'Profile',
                    to: '/My/Profile'
                },
                {
                    text: 'About Us',
                    to: '/My/About'
                },
                {
                    text: 'Contact Us',
                    to: '/My/Contact'
                },
                {
                    text: 'Change Password',
                    to: '/My/Changepwd'
                }
            ]
        }
    },
    methods: {
    handleIconClick(ev) {
        console.log(ev);
    },
    signOut() {
        if (window.localStorage.getItem('token')) {
                this.loginName = 'My'
                this.to = '/My'
                this.mylist.push({
                    text:'Sign Out',
                    to: '/'
                })
                this.token = window.localStorage.getItem('token')
      } else {
          this.loginName = 'Log In/Sign Up'
          this.to = '/login'
      }
      return;
    },
    deltoken (index) {
        var self = this
        if (index === 8) {
            window.localStorage.setItem('token', '')
            self.signOut()
            self.mylist.pop()
            axios.get('/auth/logout')
            .then(function () {
                alert('登出')
            })
        }
    },
  },
  created: function () {
      this.signOut()
  },
    watch: {
        $route: function () {
            if (window.localStorage.getItem('token') !== this.token)
            this.signOut()
        } 
    }
}
</script>

<style scoped>
.secondheader {
    border-top: 1px solid #b7b7b7;
    width: 100%;
    height: 95px;
    background: #fafafa;
}
/* logo和input样式*/
.secondheader-nav {
    width: 1080px;
    height: 53px;
    margin: 0 auto;
    padding: 21px 0 21px 0;
}
.secondheader-nav .funtter {
    float: left;
    width: 101px;
    height: 53px;
}
.secondheader-nav .el-input {
    float: left;
    width: 524px;
    margin: 12px 0 0 225px;
}
.secondheader-nav a {
    font-size: 12px;
    line-height: 24px;
}
/* 用户和购物车样式 */
.secondheader-nav .banana {
    float: right;
}

.secondheader-nav strong {
    float: left;
    color: #e5e5e5;
    margin: 0 14px 0 14px;
}
.banana li {
    float: left;
    margin-top: 17px;
}
.banana li a {
    font-size: 14px;
}
.secondheader-nav .el-input__icon+.el-input__inner {
    border-radius: 0;
}
.secondheader-nav .el-input__icon+.el-input__inner:focus {
    border-color: #E54C87;
}
.banana li a:hover{
    color: #E54C87;
    text-decoration: underline
}



.my-list {
    width: 180px;
    z-index: 3000;
    padding: 10px 0;
    background: #fff;
    border: 1px solid #e54c87;
    position: absolute;
    top:50px;
    right:40px;
}
.my-list span {
    display:block; 
    width:0; 
    height:0; 
    border-width:0 10px 10px; 
    border-style:solid; 
    border-color:transparent transparent #e54c87; 
    position:absolute; 
    top:-10px; 
    left:50%;/* 三角形居中显示 */
    margin-left:-10px;/* 三角形居中显示 */
}
.my-list em {
    display:block; 
    width:0; 
    height:0; 
    border-width:0 10px 10px; 
    border-style:solid; 
    border-color:transparent transparent #fff; 
    position:absolute; 
    top:1px; 
    left:-10px;
}
.my-list a {
    float: left;
    line-height: 12px;
    font-size: 12px;
}

.my-list li {
    text-align:left;
    width: 100%;
    float: left;
    margin: 10px 0 10px 10px;
}
.my-list li:nth-child(9) a {
    color: red;
}
.my-list li:nth-child(9) a:hover {
    color: #E54C87;
}
</style>