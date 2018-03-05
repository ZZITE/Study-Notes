// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import echarts from 'echarts'
import 'echarts/map/js/china.js'
import promise from 'es6-promise'
promise.polyfill()


Vue.prototype.$echarts = echarts
axios.defaults.baseURL = 'http://192.168.0.145:8080'
axios.defaults.headers['olytoken'] = window.localStorage.getItem('onlytoken') || ''
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
