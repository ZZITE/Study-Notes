<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <div v-try="color">
      {{num}}
    </div>
    <button @click="add()">add</button>
  </div>
</template>

<script>
import Vue from 'vue'
Vue.directive('try', {
  bind: function () {
    console.log('1 - bind')
  },
  inserted: function (el, binding) {
    console.log('2 - inserted')
    el.style = 'color:' + binding.value
  },
  update: function () {
    console.log('3 - update')
  },
  componentUpdated: function () {
    console.log('4 - componentUpdated')
  },
  unbind: function () {
    console.log('1 - bind')
  }
})
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      num: 10,
      color: 'red'
    }
  },
  methods: {
    add: function () {
      this.num++
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
