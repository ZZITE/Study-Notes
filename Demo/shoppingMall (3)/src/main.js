// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import axios from 'axios'
import promise from 'es6-promise'
// import 'font-awesome/css/font-awesome.css'

promise.polyfill()
// Vue.prototype.$http = axios

Vue.use(ElementUI)
axios.defaults.baseURL = 'http://192.168.0.112:8000'
axios.defaults.headers['olytoken'] = window.localStorage.getItem('token') || ''
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
