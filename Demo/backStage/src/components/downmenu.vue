<template>
<!-- 导航栏页 -->
  <div class="downmenu">
    <el-menu :default-active="onRoutes" class="el-menu-vertical-demo" theme="dark" unique-opened router>
      <div class="downmenu-header">
        <h2>{{ username }}</h2>
        <button @click="tuichu">{{ out }}</button>
        <router-link to="word">
            <p style="color:#A2A2A2;font-size:12px;">修改密码</p>
        </router-link>
      </div>
            <template v-for="item in items">
                <template v-if="item.subs">
                    <el-submenu :index="item.index">
                        <template slot="title">{{ item.title }}</template>
                        <el-menu-item class="menter" v-for="(subItem,i) in item.subs" :key="i" :index="subItem.index">{{ subItem.title }}
                        </el-menu-item>
                    </el-submenu>
                </template>
                <template v-else>
                    <el-menu-item :index="item.index">
                        {{ item.title }}
                    </el-menu-item>
                </template>
            </template>
        </el-menu>
  </div>
</template>
<script>
import axios from 'axios'
export default {
        data() {
            return {
                name: '用户名限制8个字',
                out: '退出',
                items: [
                    {
                        index: 'cart',
                        title: '购物车'
                    },
                    {
                        index: 'picty',
                        title: '首页管理'
                    },
                    {
                        index: 'ifica',
                        title: '分类管理'
                    },
                    {
                        index: 'ment',
                        title: '订单管理'
                    },
                    {
                        index: '2',
                        title: '售后管理',
                        subs: [
                            {   
                                index: 'change',
                                title: '换货'
                            },
                            {
                                index: 'return',
                                title: '退货'
                            }
                        ]
                    },
                    {
                        index: 'min',
                        title: '商品管理',
                    },
                    {
                      index: 'adasd',
                      title: '产品详情',
                      subs: [
                            {
                                index: 'design',
                                title: '设计师',
                            },
                            {
                                index: 'size',
                                title: '尺码管理'
                            },
                            {
                                index: 'attr',
                                title: '产品属性'
                            },
                            {
                                index: 'skill',
                                title: '洗衣技巧'
                            },
                        ]
                    },
                    {
                        index: 'cle',
                        title: '文章管理'
                    },
                    {
                        index: '.asd',
                        title: '会员管理',
                        subs: [
                            {
                            index: 'member',
                            title: '会员列表'
                            },
                            {
                            index: 'grade',
                            title: '等级管理'
                            },
                            {
                            index: 'record',
                            title: '会员记录管理' 
                            }
                        ]
                    },
                    {
                        index: 'analy',
                        title: '数据分析',
                    },
                    {
                        index: 'dign',
                        title: '活动设置',
                        subs: [
                            {
                            index: 'asd',
                            title: '尺码管理'
                            },
                            {
                            index: 'xx',
                            title: '模特管理'
                            },
                            {
                            index: 'xasd',
                            title: '产品详情',
                            },
                            {
                            index: 'xasd',
                            title: '洗衣技巧',
                            }
                        ]
                    },
                    {
                      index: 'asdad',
                      title: '用户管理  ',
                      subs: [
                        {
                          index: 'user',
                          title: '用户'
                        },
                        {
                          index: 'dic',
                          title: '角色',
                        }
                      ]
                    },
                    {
                        index: 'set',
                        title: '系统设置'
                    }
                ]
            }
        },
        computed:{
             username(){
                let username = localStorage.getItem('ms_username');
                return username ? username : this.name;
            },
            onRoutes(){
                return this.$route.path.replace('/','');
            }
        },
        methods: {
            tuichu: function () {
                axios.get('/auth/logout')
                .then(function(response){
                    localStorage.removeItem('ms_username')
                    localStorage.removeItem('onlytoken')
                })
                .catch(function(err){
                    console.log(err);
                });
                this.$router.push('/login');
                
            }
        }

    }
</script>

<style>
.downmenu {
  z-index: 9999;
  float: left;
  width: 260px;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
}
.downmenu-header {
  width: 240px;
  height: 62px;
  padding: 18px 0 0 20px;
  border-bottom: 1px solid #4A4A4A; 
}
.downmenu-header h2 {
  float: left;
  margin-right: 28px;
  font-size: 16px;
  color: #F1F1F1;
}
.downmenu-header button {
  width: 40px;
  height: 20px;
  margin-top: 2px;
  border: 0;
  color: white;
  background: #D64B7F;
}
.downmenu .el-menu--dark {
  width: 260px;
  height: 1080px;
  background: #3A3A3A;
  z-index: 1000000;
}
.downmenu .el-menu--dark .el-menu-item, .el-menu--dark .el-submenu__title {
    border-bottom: 1px solid #4A4A4A;
}
.downmenu .el-submenu__title {
    margin-left: 4px;
}
.el-menu--horizontal.el-menu--dark .el-submenu .el-menu-item.is-active, .el-menu-item.is-active {
    color:#D64B7F;
}
.downmenu .el-submenu.is-active .el-submenu__title {
    border-bottom-color: #4A4A4A; 
}
</style>
