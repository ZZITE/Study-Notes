<template>
  <div class="talkBox">
    <div class="box-header">
      <img/>
      <span class="header-text">{{headerText}}</span>
    </div>
  </div>
</template>
<<script>
export default {
  data () {
    return {
      headerText: "Let's talk! "
    }
  }
}
</script>

<style scoped>
  .talkBox {
    background: #ffffff;
    height: 393px;
    right: 45px;
    display: block;
    width: 300px;
    text-align: left !important;
    bottom: 0;
    position: fixed;
    z-index: 100000;
    transition: height 0.6s;
    border-radius: 3px 3px 0px 0px;
    word-break: break-word;
    word-wrap: break-word;
    box-sizing: border-box;
    box-shadow: 0 0 10px 2px rgba(0,0,0,0.1);
  }
  .box-header {
    cursor: pointer;
    border-radius: 3px 3px 0px 0px;
    height: 43px;
    background: #777777;
  }
  .header-text {
    float: left;
    margin: 11px 0 0 10px;
    font-size: 14px;
    width: 170px;
    font-weight: 500;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: 24px;
    text-transform: inherit;
    vertical-align: baseline;
    color: #FFFFFF;
  }
</style>
