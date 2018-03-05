<template>
  <div class="filters-wrap">
    <bread></bread>
    <filters class="filters"></filters>
    <transition name="fade">
    <listContent class="listContent"></listContent>
    </transition>
  </div>
</template>
<script>
import filters from '@/components/filters'
import listContent from '@/components/listContent'
import bread from '@/components/breadcrumb'
export default {
  name: 'productList',
  data () {
    return {
    }
  },
  components: {
    'filters': filters,
    'listContent': listContent,
    'bread': bread
  },
  mounted: function () {
    console.log(this.$route.params.id)
  },
  watch: {
   '$route' (to, from) { 
      const toDepth = to.path.split('/')
      console.log(toDepth[toDepth.length-1])
   }
  }
}
</script>
<style scoped>
  .filters {
    float: left;
    width:200px;
  }
  .listContent {
    float: left;
    width:860px;
    margin-left: 20px;
  }
 .filters-wrap {
   margin: 0 auto;
   width: 1080px;
   height: 100%;
 }
.filters-wrap::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
 }
 
</style>
