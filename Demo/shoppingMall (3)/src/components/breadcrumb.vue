<template>
    <div class="breadcrumb">
      <el-breadcrumb separator=">">
      <el-breadcrumb-item class="titleHover" :to="{ path: '/' }">Home</el-breadcrumb-item>
      <el-breadcrumb-item class="titleHover" v-for="(item,index) in path" :key="index" :to="{ path: item.to }">{{item.pathname}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>   
</template>
<script>
export default {
  data () {
    return {
      path: []
    }
  },
  methods: {
    bread: function () {
      this.path = []
      const pa = this.$route.fullPath.split('/')
      for (var i = 0; i < pa.length; i++) {
        if (pa[i] === '') {
          pa.splice(i,1)
        }
      }
      for (var j = 0; j < pa.length; j++) {
      this.path.push({
        pathname: pa[j],
        to:  pa[j]
      })
      }
    }
  },
  mounted: function () {
    this.bread()
  },
  watch: {
    '$route' (to, from) { 
        this.bread()
    }
  }
}
</script>

<style>
.breadcrumb {
   margin-top: 10px;
   height: 20px;
   width:220px;
 }
 .el-breadcrumb {
   color: #595959;
   font-size: 12px;
 }
 .titleHover :hover {
   color: #E54C87;
 }
 .el-breadcrumb__item__inner {
   color: #999;
 }
 .el-breadcrumb__item:last-child .el-breadcrumb__item__inner {
   color: #999;
 }

</style>