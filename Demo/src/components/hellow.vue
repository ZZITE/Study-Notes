<template>
  <div class="hellow">
   <h2>
     你好，{{name}}
   </h2>
  </div>
</template>

<script>
export default {
  name: 'hellow',
  data () {
    return {
    }
  },
  computed: {
    name () {
      return this.$store.state.name
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h2 {
    font-size: 2.6rem;
  }
</style>

