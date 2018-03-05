<template>
  <div id="transfer">
    <mytable></mytable>
  </div>
</template>

<script>
import mytable from '@/components/table'
export default {
 name: 'transfer',
  data () {
    return {
    } 
  },
  components: {
    mytable
  },
  created: function () {
    console.log(121)
  }
}
</script>

<style>
</style>
