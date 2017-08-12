<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>{{num}}</p>
    <button @click="add()">add</button>
    <lin v-bind:aaaa="msg"></lin>
  </div>
</template>

<script>
/*
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
*/
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Just Do It',
      num: 10,
      color: 'red'
    }
  },
  components: {
    'lin': {
      template: `<div>来自{{aaaa}}</div>`,
      props: ['aaaa']
    }
  },
  methods: {
    add: function () {
      this.num++
    }
  },
  beforeCreate: function () {
    console.log('sas')
  },
  updated: function () {
    console.log('6-updated 被更新后')
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
