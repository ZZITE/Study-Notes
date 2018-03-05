<template>
  <div class="newin">
    <bread></bread>
    <div style="margin-top:20px;">
      <h2 style="display:inline-block;font-size:16px;color:#0F0F0F;">Today's Special</h2>
      <span style="display:inline-block;margin-left:10px;font-size:12px;color:#595959 ">Get up to 80% off on Designers Fashions with Limited Supply, Event starts at Noon ET Everyday!</span>
    </div>
    <div class="newinContent">
      <ul>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
        <li>
          <div class="newin-imgDiv">
            <img src="">
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import bread from '@/components/breadcrumb'
export default {
  name: 'home',
  data () {
    return {
    }
  },
  components: {
    bread
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.newin {
  width: 1080px;
  height: 100%;
  margin: 0 auto;
}
.newinContent {
  width: 1100px;
  height: 100%;
  margin-top: 10px;
  margin-left: -20px;
}
.newinContent::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden; 
}
.newin-imgDiv {
  width: 530px;
  height: 320px;
  float: left;
  margin-left: 20px;
  margin-bottom: 20px; 
}
img {
  width: 100%;
  height: 100%;
}
</style>