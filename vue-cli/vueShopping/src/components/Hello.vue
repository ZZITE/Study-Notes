<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>{{changeNum}}</p>
    <button @click="add(2,$event)">add</button>
    <lin v-bind:aaaa="msg"></lin>
    <component v-bind:is="which"></component>
    <ul>
      <li v-for="list in reverseNews">{{list}}</li>        
    </ul>
    <btn @click.native="add(3)"></btn>
    <p>{{suggmes}}</p>
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
var componentA = {
  template: `<p>asa</p>`
}
var componentB = {
  template: `<p>this is B</p>`
}
var btn = {
  template: `<button>btn</button>`
}
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Just Do It',
      num: 0,
      color: 'red',
      which: 'componentA',
      items: [1, 2, 3, 4],
      suggmes: '少了',
      sugg: ['少了', '刚好', '多了']
    }
  },
  components: {
    'lin': {
      template: `<div>来自{{aaaa}}</div>`,
      props: ['aaaa']
    },
    'componentA': componentA,
    'componentB': componentB,
    'btn': btn
  },
  methods: {
    add: function (number, $event) {
      this.num += number
      if (this.which === 'componentA') {
        this.which = 'componentB'
      } else {
        this.which = 'componentA'
      }
    }
  },
  watch: {
    num: function (oldValue, newValue) {
      if (oldValue < 14) {
        this.suggmes = this.sugg[0]
      } else if (oldValue === 14) {
        this.suggmes = this.sugg[1]
      } else {
        this.suggmes = this.sugg[2]
      }
    }
  },
  computed: {
    changeNum: function () {
      return this.num + '转换后'
    },
    reverseNews: function () {
      return this.items.reverse()
    }
  },
  beforeCreate: function () {
    // console.log('sas')
  },
  updated: function () {
    // console.log('6-updated 被更新后')
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
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
