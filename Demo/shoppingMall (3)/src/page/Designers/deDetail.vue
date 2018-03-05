<template>
  <div class="deDetail-wrap">
    <bread></bread>
    <header style="margin-top:20px;">
      <div style="display:inline-block;font-size:16px;color:#0F0F0F;">{{designer.name}}</div>
      <span style="display:inline-block;margin-left:10px;"><el-button @click="changefollow" type="primary" size="small" style="width:86px;height:18px;">{{follow  }}</el-button></span>
      <p style="margin-top:10px;">{{designer.desc}}</p>
    </header>
    <div class="deDetailContent">
    <listContent></listContent>
    </div>
  </div>
</template>

<script>
import bread from '@/components/breadcrumb'
import listContent from '@/components/listContent'
import axios from 'axios'
export default {
  name: 'deDetail',
  data () {
    return {
      designer: {
        name: 'Abbott Vintage',
        desc: 'Founded in 2013, this bag brand focuses on simplicity and rumination. It stresses the design of dimensionally geometrical lines. In terms of material, the bags are made of the first layer of cowhide leather or sheepskin with scratch and scar, which feels soft. The concept of design is to emphasize the idea of Simplicity by the contrast between the cross-cutting Design material and texture. She hopes to open a small business on the streets in Europe to share some bags with stories. By placing the Retro rumination above the trend of artistic feelings, a bag with a story can eventually find the rightful owner.'
      }
    }
  },
  components: {
    bread,
    listContent
  },
  methods: {
    changefollow: function () {
      var self = this
        axios({
          method: 'post',
          url: '/user/follow', 
          data: {
            designer_id: self.designer.id 
          }
        })
        .then(function (res) {
          console.log(res)
          self.designer.is_following = res.data.is_following
        })
        .catch(function(err) {
          alert('请先登录')
          // self.$router.push({path: '/login'})
        })
    }
  },
  created: function () {
    var self = this
    axios.get('/designer/'+ self.$route.query.id)
    .then(function (res) {
      console.log(res.data)
      self.designer = res.data
    })
  },
  computed: {
    follow: function () {
      if (this.designer.is_following === true) {
        return 'UNFOLLOW'
      } else {
        return 'FOLLOW'
      } 
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.deDetail-wrap {
  width: 1080px;
  height: 100%;
  margin: 0 auto;
}
.el-button--primary {

  height: 20px;
  line-height: 2px;
  font-size: 12px;
  color: #fff;
  background-color: #E54C87;
  border-color: #E54C87;
  border-radius: 0;
}
.el-button--primary:hover {
  background-color: #E54C87;
  border-color: #fff;
}
.el-button--primary:focus {
  background-color: #E54C87;
  border-color: #E54C87;
}
.el-button--primary:active {
  color: #E54C87;
  background-color: #fff;
  border-color: #E54C87;
}
.fo-content-wrap router-Link {
  color: #E54C87;
}
.el-button {
  padding: 4px 4px;
}
.deDetailContent {
  width: 1080px;
  margin-top: 20px;
}
.content-title {
  border: 0;
}
</style>