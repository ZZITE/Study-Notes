import Vue from 'vue'
import Router from 'vue-router'
import hellow from '@/components/hellow'
import login from '@/components/login'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/hellow',
      name: 'hellow',
      component: hellow
    }
  ]
})
