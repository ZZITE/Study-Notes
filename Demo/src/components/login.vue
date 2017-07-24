<template>
  <div class="wrap">
      <input type="text" placeholder="账户名"  v-model="name"></input>
      </br>
      <input type="password" placeholder="密码"></input>
      </br>
      <button @click="addName()">{{login}}</button>
  </div>
</template>
<script>
export default {
  name: 'login',
  data () {
    return {
      login: '登录',
      name: ''
    }
  },
  methods: {
    addName: function() {
      if (this.name === '') {
        alert('请输入账户密码');
        return;
      }
      this.$store.commit('hellowName',this.name);
      this.$router.push({path:'/hellow'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

 input {
   margin: 0 auto;
   display: block;
   text-align: center;
   width: 14rem;
   height: 1.4rem;
   line-height: 2rem;
   border-radius: 0.4rem;
 }
 button {
   color: #666;
   margin-top: 0.4rem;
   height: 1.6rem;
   width: 6rem;
   background-color: #90CAAF;
   border-radius: 0.4rem;
 }
</style>
