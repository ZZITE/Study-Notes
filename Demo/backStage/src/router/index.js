import Vue from 'vue'
import Router from 'vue-router'
// import login from '@/components/login'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import echarts from 'echarts'

Vue.prototype.$echarts = echarts
Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/home',
      component: resolve => require(['../components/home.vue'], resolve),
      children: [
        {
          path: '/picty',
          component: resolve => require(['../components/addpictures.vue'], resolve)
        },
        {
          path: '/ment',
          component: resolve => require(['../components/management.vue'], resolve)
        },
        {
          path: '/ifica',
          component: resolve => require(['../components/classification.vue'], resolve)
        },
        {
          path: '/design',
          component: resolve => require(['../components/product/designer.vue'], resolve)
        },
        {
          path: '/analy',
          component: resolve => require(['../components/analysis.vue'], resolve)
        },
        {
          path: '/change',
          component: resolve => require(['../components/customer/exchange.vue'], resolve)
        },
        {
          path: '/return',
          component: resolve => require(['../components/customer/returne.vue'], resolve)
        },
        {
          path: '/min',
          component: resolve => require(['../components/admin.vue'], resolve)
        },
        {
          path: '/user',
          component: resolve => require(['../components/privilege/user.vue'], resolve)
        },
        {
          path: '/dic',
          component: resolve => require(['../components/privilege/jurisdiction.vue'], resolve)
        },
        {
          path: '/size',
          component: resolve => require(['../components/product/size.vue'], resolve)
        },
        {
          path: '/attr',
          component: resolve => require(['../components/product/attributes.vue'], resolve)
        },
        {
          path: '/skill',
          component: resolve => require(['../components/product/skille.vue'], resolve)
        },
        {
          path: '/word',
          component: resolve => require(['../components/xjpassword.vue'], resolve)
        },
        {
          path: '/set',
          component: resolve => require(['../components/xtsettings.vue'], resolve)
        },
        {
          path: '/cart',
          component: resolve => require(['../components/cart.vue'], resolve)
        },
        {
          path: '/cle',
          component: resolve => require(['../components/Article.vue'], resolve)
        },
        {
          path: '/member',
          component: resolve => require(['../components/Membershipmanagement/Member.vue'], resolve)
        },
        {
          path: '/grade',
          component: resolve => require(['../components/Membershipmanagement/Grade.vue'], resolve)
        },
        {
          path: '/record',
          component: resolve => require(['../components/Membershipmanagement/Record.vue'], resolve)
        }
      ]
    },
    {
      path: '/login',
      component: resolve => require(['../components/login.vue'], resolve)
    }
  ]
})