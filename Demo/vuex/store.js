import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 定义状态
  state: {
   name: ''
    },
  mutations: {
    hellowName(state,change) {
      state.name = change
    }
  }
})

export default store