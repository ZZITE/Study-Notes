import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/page/Hello'
import Swiper from '@/components/page/swiper'
import Home from '@/components/page/home'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/swiper',
      name: 'swiper',
      component: Swiper
    },
    {
      path: '/Home',
      name: 'home',
      component: Home
    }
  ]
})
