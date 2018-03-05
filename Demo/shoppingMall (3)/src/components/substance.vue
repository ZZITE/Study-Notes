<template>
  <div class="homecontent">
    <section id="PopularCategories" class="homewrap">
      <div class="hometitle">
        <h2>Popular Categories</h2>
      </div>
        <div class="homemain">
          <div class="first-one">
            <router-link to="Product/TOPS">
              <img>
            </router-link>
            <span>sd</span>
          </div>
          <div class="first-two">
            <a>
              <img>
            </a>
          </div>
          <div class="first-three">
            <a>
              <img>
            </a>
          </div>
          <div class="first-four">
            <a>
              <img>
            </a>
          </div>
        </div>
    </section>


      <div id="swiper" class="hometitle">
          <h2>What's Popular</h2>
      </div>
      <swiper2></swiper2>


    <section class="homewrap wrap-sec">
      <div id="TheTrendHub1" class="title">
        <h2>The Trend Hub</h2>
      </div>
        <div class="main-sec">
          <div class="second-one">
            <div>
              <img>
            </div>
          </div>
          <div class="second-two">
            <div class="second-three">
              <h3>ddd</h3>
              <p>sdsdsdsdsdsdsd</p>
            </div>
            <ul class="second-eg">
              <!--   
                <li class="sec" v-for="item in items">
                  <div>
                    <img src="item">
                  </div>
                </li>
              -->
              <li class="second-four">
                <div>
                  <img>
                </div>
              </li>
              <li class="second-five">
                <div>
                  <img>
                </div>
              </lidiv>
              <li class="second-six">
                <div>
                  <img>
                </div>
              </li>
              <li class="second-seven">
                <div>
                  <img>
                </div>
              </li>


            </ul>
          </div>
      </div>
    </section>

    <section class="homewrap wrap-third">
      <div id="HowToWear" class="hometitle">
        <h2>How To Wear</h2>
      </div>
        <ul class="main-third">
          <li class="third-one">
            <img src="https://www.stylewe.com/image_cache/resize/340x520/image/catalog/advertising/20170815newseason.jpg">
            <span>New Season Soon</span>
          </li>
          <li class="third-two">
            <img>
            <span>Bold Colors Club</span>
          </li>
          <li class="third-three">
            <img>
            <span>Eye-catching Sleeves</span>
          </li>
        </ul>
    </section>

    <section class="homewrap wrap-fourth">
      <div id="TheTrendHub2" class="hometitle">
        <h2>The Trend Hub</h2>
      </div>
        <ul class="main-fourth">
          <li class="fourth-one">
            <div>
              <img>
              <span>Bold Colors Club</span>
            </div>
          </li>
          <li class="fourth-two">
            <div>
              <img>
              <span>Bold Colors Club</span>
            </div>
          </li>
          <li class="fourth-three">
            <div>
              <img>
              <span>Bold Colors Club</span>
            </div>
          </li>
          <li class="fourth-four">
            <div>
              <img>
              <span>Bold Colors Club</span>
            </div>
          </li>
        </ul>
    </section>


  </div>
</template>
<script>
import swiper2 from '@/components/swiper2'
export default {
  data () {
    return {
    }
  },
  components: {
    'swiper2': swiper2
  }
}
</script>

<style scoped>
.homewrap {
  background: #fafafa;
  text-align: center;
  height: 900px;
  overflow: hidden;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 1080px;
}
.hometitle {
  height: 100px;
  width: 230px;
  margin: 0 auto;
}
img {
    width: 100%;
    height: 100%;
    bottom: 0;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    z-index: 1;
    background-color: #fff;
    margin: 0 auto;
}
h2 {
  display: block;
  text-align: center;
  border-bottom: 1px solid #b7b7b7;
  color: #0f0f0f;
  font-size: 24px;
  line-height: 26px;
  height: 70px;
  width: 220px;
  line-height: 100px;
}
span {
  bottom: 0;
}
.homemain {
  position: relative;
  background: #fff;
  height: 800px;
}
.first-one {
  position: absolute;
  left: 0;
  top: 0;
  width: 530px;
  height: 480px;
}
.first-two {
  position: absolute;
  right: 0;
  top: 0;
  margin-left: 20px;
  width: 530px;
  height: 300px;
}
.first-three {
  position: absolute;
  top: 500px;
  left: 0;
  width: 530px;
  height: 300px;
}
.first-four {
  position: absolute;
  top: 320px;
  right: 0;
  width: 530px;
  height: 480px;
}
.wrap-sec {
  height: 760px;
}
.main-sec {
  height: 760px;
}
.second-one {
  float: left;
}
.second-one div {
  position: relative;
  width: 540px;
  height: 660px;
}
.second-two {
  float: left;
  width: 540px;
  height: 660px;
}
.second-three {
  width: 100%;
  height: 110px;
  text-align: left;
  margin-left: 20px;
}
h3 {
  position: relative;
  top: 10px;
  font-size: 20px;
  color:#303030;
}
p {
  font-size: 16px;
  color: #595959 ;
  position: relative;
  top: 20px;
}

.second-eg {
  width: 540px;
  height: 530px;
  list-style: none;
  padding: 0;
  margin: 0;
}
.second-eg div {
  position: relative;
  width: 250px;
  height: 255px;
}
.second-four {
  float: left;
  margin: 20px 0 0 20px;
}
.second-five {
  float: left;
  margin: 20px 0 0 20px;
}
.second-six {
  float: left;
  margin: 20px 0 0 20px;
}
.second-seven {
  float: left;
  margin: 20px 0 0 20px;
}





.wrap-third {
  height: 620px;
}
.main-third {
  height: 620px;
  text-align: left;
}
.third-one {
  margin-left: 20px;
  display: inline-block;
  position: relative;
  width:344px;
  height:520px; 
  background:rgba(183,183,183,1);
}
.third-two {
  margin-left: 20px;
  display: inline-block;
  position: relative;
  width:344px;
  height:520px; 
  background:rgba(183,183,183,1);
}
.third-three {
  margin-left: 20px;
  display: inline-block;
  position: relative;
  width:344px;
  height:520px; 
  background:rgba(183,183,183,1);
}

  .third-one:first-child {
    margin: 0;
}

.main-third span {
  display: inline-block;
  position: absolute;
  width:344px;
  height:32px; 
  background:rgba(255,255,255,1);
  opacity:0.8;
  z-index: 1; 
  font-size:16px;
  text-align: center;
  font-family:ArialMT;
  color:rgba(15,15,15,1);
  line-height:32px;
}

.wrap-fourth {
  height: 800px;
}
.main-fourth {
  height: 800px;
}
.fourth-one {
  float: left;
  margin: 0;
}
.fourth-two {
  float: left;
  margin-left:20px;
}
.fourth-three {
  float: left;
  margin: 20px 0 0 0px;
}
.fourth-four {
  float: left;
  margin: 20px 0 0 20px;
}
.main-fourth div {
  width: 530px;
  height: 340px;
  position: relative;
}


</style>
