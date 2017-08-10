<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <div v-try="color">
      {{num}}
    </div>
    <button @click="add()">add</button>
    <author></author>
  </div>
</template>

<script>
import Vue from 'vue'
var Author = Vue.extend({
  template: "<p><a :href='url'>{{author}}</a></p>",
  data: function () {
    return {
      author: 'asasa',
      url: 'http://www.baidu.com'
    }
  }
})
new Author().$mount('author')
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
