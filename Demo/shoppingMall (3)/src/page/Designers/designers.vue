<template>
  <div class="designers-wrap">
    <bread></bread>
    <div class="de-content">
      <div class="de-section" style="margin-top:14px;" v-for="(items, index) in designers" :key="index">
          <h2>{{items.initial}}</h2>
          <div class="de-name">
            <ul style="margin-top:4px;">
              <li v-for="(i, index) in items.item" :key="index">
                <router-link class="de-a" :to="{ path: '/Designers/detail', query: { id: i.id }}">
                {{i.name}}
                </router-link>
              </li>
            </ul>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import bread from '@/components/breadcrumb'
export default {
  name: 'designers',
  data () {
    return {
      designers: null
    }
  },
  components: {
    bread
  },
  methods: {
  },
  created: function () {
    var self = this
    axios.get('/designer?o=alpha&page=all')
    .then(function (res) {
       self.designers = res.data.object_list
       console.log(res.data.object_list)
    })
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.designers-wrap {
  width: 1080px;
  height: 100%;
  margin: 0 auto;
}
h2 {
  font-size: 16px;
  color: #0F0F0F;
}
.de-section {
  width: 1080px;
  float: left;
}
.de-name {
  width: 1080px;
  border-top: 1px solid #E5E5E5;
  margin-top: 4px;
}
.de-a:hover{
  color:#E54C87;
  text-decoration: underline;
}
.de-a {
  float: left;
  width: 90px;
  display: block;
  font-size: 14px;
  color: #595959;
  margin-right:84px ;
  margin-bottom: 10px;
}
.de-content::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
</style>