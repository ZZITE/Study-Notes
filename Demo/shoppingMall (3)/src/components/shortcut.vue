<template>
<ul class="footerShortcut" style="z-index: 1000; position: fixed; bottom: 45px; margin-left: 0px; width: 40px; left: 1863px;right:0;height: 225px;">
  <li>
    <a>
      <i class="fa fa-shopping-cart" aria-hidden="true"></i>
    </a>
  </li>
  <li class="showDiv">
    <a>
      <i class="fa fa-bell-o" aria-hidden="true"></i>
    </a>
    <div class="div1">
      <h1>sdsds</h1>
    </div>
  </li>
    <li class="showDiv">
    <a>
      <i class="fa fa-mobile" aria-hidden="true"></i>
    </a>
    <div class="div2">
    </div>
  </li>
  <li class="showDiv">
    <a>
      <i class="fa fa-weixin" aria-hidden="true"></i>
    </a>
    <div class="div2">
    </div>
  </li>
  <li v-bind:class="toTop">
    <a @click="backToTop()">
      <i class="fa fa-angle-up" aria-hidden="true"></i>
    </a>
  </li>
</ul>
</template>
<script>
export default {
  name: 'shortcut',
  data () {
    return {
      toTop: 'toTopHidden'
    }
  },
  methods: {
    handleScroll () {
      var scrolled = window.pageYOffset > 0;
      if (scrolled) {
        this.toTop = 'toTopShow'
      } else {
          this.toTop = 'toTopHidden'
      }
    },
    backToTop () {
      //document.body.scrollTop = 0
      //document.documentElement.scrollTop = 0
      window.scrollBy(0,-250);
        //延时递归调用，模拟滚动向上效果
        var scrolldelay = setTimeout(this.backToTop,50);
        var sTop=document.documentElement.scrollTop+document.body.scrollTop;
        if(sTop==0) 
        clearTimeout(scrolldelay);
    },
    debounce (fn,delay,mustRunDelay) {
      var timer = null;
      var t_start;
      return function(){
        var context = this;
        var args = arguments;
        var t_curr = +new Date();
        clearTimeout(timer);
        if(!t_start){
            t_start = t_curr;
        }
        if(t_curr - t_start >= mustRunDelay) {
            fn.apply(context,args);
            t_start = t_curr
        } else {
            timer = setTimeout(function(){
                fn.apply(context,args);
            },delay);
        }
      } 
    }
  },
  mounted () {
    window.addEventListener('scroll', this.debounce(this.handleScroll,100,1000));
  },
  watch: {
    '$route' (to, from) {
      if (window.pageYOffset > 0) {
        document.documentElement.scrollTop = 0
      }
      return
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  li {
    width: 40px;
    height: 40px;
    margin-bottom: 5px;
    position: relative;
    background: #333;
    font-size: 22px;
    color: #fff;
    text-align: center;
    vertical-align: middle;
  }
  .showDiv :hover {
    background: #fdf0d6;
  }
  i {
    cursor: pointer;
    background: #333;
    display: block;
    font-size: 22px;
    color: #fff;
    line-height: 40px;
    text-align: center;
  }
  .f-icon-line-cart {
    font-family: font;
    font-style: normal;
    font-weight: 400;
    line-height: 1em;
  }
  .f-icon-line-cart::before {
    font-family: font;
    font-style: normal;
    font-weight: 400;
    display: inline-block;
    text-decoration: inherit;
    width: 1em;
    margin-right: .2em;
    text-align: center;
    font-variant: normal;
    text-transform: none;
    line-height: 1em;
    margin-left: .2em;
    -webkit-font-smoothing: antialiased;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .8s
  }
  .fade-enter, .fade-leave-active {
    opacity: 0
  }
  .toTopHidden {
    visibility:hidden;
    -webkit-transition:all 0.5s linear;
    -moz-transition:all 0.5s linear;
    -ms-transition:all 0.5s linear;
    -o-transition:all 0.5s linear;
    transition:all 0.5s linear;
    opacity:0.5;
  }
  .toTopShow {
    -webkit-transition:all 0.5s linear;
    -moz-transition:all 0.5s linear;
    -ms-transition:all 0.5s linear;
    -o-transition:all 0.5s linear;
    transition:all 0.5s linear;
    visibility:visible; 
    opacity:1;
  }
  .div1 {
    width: 240px;
    height: 200px;
    padding: 15px;
    position: absolute;
    top: 0;
    right: 40px;
    margin-top: -80px;
    background: #fdefd4;
    color: #fff;
    display: none;
  }
  .div2 {
    width: 240px;
    height: 200px;
    padding: 15px;
    position: absolute;
    top: 0;
    right: 40px;
    margin-top: -80px;
    background: #fdefd4;
    color: #fff;
    display:none;
  }
  .showDiv:hover>div {
    display: block !important;
  }
  li:hover {
    background: #fdf0d6;
  }

</style>