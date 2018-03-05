<template>
<!-- 最外层底部div -->
  <div class="footer">
      <!-- 居中div -->
      <div class="footer-bottom">
          <!-- 搜索和小图标 -->
          <div class="bottomone">
              <el-input v-model="input5" placeholder="Your Email Address"></el-input>
              <el-button type="success">{{ UP }}</el-button>
              <div class="bottomtwo">
                  <a href="">
                      <h2>{{ US }}</h2>
                      <img src="static/images/youxiang.png" alt="">
                      <img src="static/images/xiangji.png" alt="">
                      <img src="static/images/ff.png" alt="">
                      <img src="static/images/bofang.png" alt="">
                      <img src="static/images/gezi.png" alt="">
                      <img src="static/images/weibo.png" alt="">
                  </a>
              </div>
          </div>
          <!-- 下层ul介绍 -->
          <div class="cuper-one">
              <ul style="margin: 0 330px 0 0">
                  <li v-for="(rnb,index) in rnbs" :key="index">
                      <a :href="rnb.url">
                          {{ rnb.tex }}
                        <strong>{{ rnb.textt }}</strong>
                      </a>
                  </li>
              </ul>
              <ul>
                <li v-for="(tnb,index) in tnbs" :key="index">
                    <a :href="tnb.url">
                        {{ tnb.tex }}
                        <strong>{{ tnb.textt }}</strong>
                    </a>
                </li>
              </ul>
              <ul style="float:right">
                <li v-for="(Anb,index) in Anbs" :key="index">
                    <a :href="Anb.url">
                        {{ Anb.tex }}
                        <strong>{{ Anb.textt }}</strong>
                    </a>
                </li>
              </ul>
          </div>
          <!-- 说明 -->
          <p>{{ dibiao }}</p>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            // 第一行导航
            rnbs: [
                { textt: 'COMPANY', url:'http://www.baidu.com'},
                { tex: 'About Us', url:'/' },
                { tex: 'Our Designers', url:'/' },
                { tex: 'Terms & Tonditions', url:'/' },
                { tex: 'Privacy policy', url:'/' },
            ],
            // 第二行导航
            tnbs: [
                { textt: 'HELP CENTER' },
                { tex: 'Q&A' },
                { tex: 'Delivery' },
                { tex: 'Returns & Exchanges' },
                { tex: 'Payment Methods' },
            ],
            // 第三行导航
            Anbs: [
                { textt: 'CUSTOMER SERVlCE' },
                { tex: 'Contact Us' },
                { tex: 'My Account' },
                { tex: 'Safe Shopping Guarantee' }
            ],
            // 数据数值
            input5: '',
            dibiao: '© 2015-2017 STYLEWE.COM',
            UP: 'SIGN UP',
            US: 'Contact Us:'
        }
    }
}
</script>

<style>
/* 最外div样式 */
.footer {
    width: 100%;
    height: 250px;
    background: #f0f0f0;
    border-top: 1px solid #b7b7b7;
    clear: both;
}
.footer-bottom {
    width: 1080px;
    margin: 0 auto;
    padding: 20px 0 0 0;
}
/* 中间div样式 */
.bottomone {
    float: left;
    width: 100%;
    padding-bottom: 20px;
    border-bottom: 1px solid #b7b7b7;
}
/* input样式 */
.bottomone .el-button--success {
    float: left;
    width: 78px;
    height: 36px;
    margin-right: 50px;
    background: #f85292;
    border: #f85292;
    border-radius: 0;
}
/* input样式 */
.bottomone .el-input {
    float: left;
    width: 300px;
    margin-left: 180px;
    border-radius: 0;
}
/* 设置圆角样式 */
.bottomone .el-input__inner {
    border-radius: 0;
}
/* 右边小图标样式 */
.bottomtwo {
    float: left;
    width: 300px;
    height: 36px;
    line-height: 36px;
}
/* 底部最下导航样式 */
.cuper-one {
    float: left;
    width: 1080px;
    margin: 0 auto;
}
.cuper-one a {
    display: block;
    width: 100%;
    color: #5a5a5a;
}
.cuper-one a:hover {
    color: pink;
}

/* 底部介绍样式 */
.footer-bottom p {
    font-size: 12px;
    text-align: center;
    color: #5a5a5a;
}
.footer-bottom img {
    margin-left: 2px;
}
.footer-bottom img:hover {
    border-radius: 50%;
    background: #E54C87;
}
/* 三个字体样式 */
.cuper-one strong {
    font-weight: bold;
    color: black;
}
.cuper-one ul {
    float: left;
    line-height: 25px;
}
.bottomtwo h2 {
    float: left;
}
</style>