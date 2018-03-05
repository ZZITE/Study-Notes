<template>
<!-- 头部页面 -->
    <div class="header">
        <div class="header-nav" @mouseleave="hidden();hidden2()">
            <h2>{{ msage }}<em>{{ mssages }}</em></h2>
            <router-link to="/help">
                <a>帮助中心</a>
            </router-link>
            <ul>
                <li>
                    <a @mouseover="show2"><span><img v-bind:src="picty.url" alt=""></span>
                    <span><strong>{{picty.panda}}</strong></span>
                    </a>
                </li>
                <li><a  @mouseover="show">{{ picty.speck }}</a></li>
                <span class="xian">|</span>
                </ul>
                <!-- 语言 -->
            <div class="speak" v-if="this.static"  @mouseleave="hidden">
                <ul>
                <li v-for="(cd, index) in cds" :key="index">
                <a>{{cd}}
                </a>
                </li>
                </ul>
            </div>

                <!-- 价格单位 -->
                <div class="speak-one" v-if="this.static2" @mouseleave="hidden2">
                <ul>
                    <li v-for="(qz, index) in qzs" :key="index">
                        <a :href="qz.url">
                            <img :src="qz.picty" alt="">
                            {{ qz.spend }}
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <second></second>
        <ation></ation>
    </div>
</template>

<script>
import second from '@/components/hsecond'
import ation from '@/components/avigation'

export default {
  components: {
      'second': second,
      'ation': ation
  },
  data() {
    return {
        static: false,
        static2: false,
        msage: 'FREE SHIPPING ON ORDERS OF $50 OR MORE',
        mssages: 'DETAILS',
        picty: {
                panda: 'USD($)',
                speck: 'English',
                url: 'static/images/usa.png'
        },
        cds: ['English','Chinese','Japanese'],
        qzs: [
            { picty: 'static/images/usa.png', spend: 'USD($)'},
            { picty: 'static/images/oen.png', spend: 'EUR(ぃ)' },
            { picty: 'static/images/lantwo.png', spend: 'GBP(ん)'},
            { picty: 'static/images/fengye.png', spend: 'CAD(CA$)'},
            { picty: 'static/images/liuxing.png', spend: 'AUD(A$)'},
            { picty: 'static/images/threep.png', spend: 'MAN(MAX$)'},
            { picty: 'static/images/fourp.png', spend: 'AED(AED)'}
        ]
    }
  },
  methods: {
      show: function () {
        this.static = true;
      },
      hidden: function () {
        this.static = false
      },
      show2: function () {
        this.static2 = true
      },
      hidden2: function () {
        this.static2 = false
      }
  }
}
</script>

<style scoped>
/* 头部 */
.header {
    margin: 0 auto;
    width: 100%;
    background: #f0f0f0;
}
.header-nav  {
    width: 1080px;
    height: 22px;
    margin: 0 auto;
    padding-top: 8px;
    position: relative;
    /* background: skyblue; */
}
.header-nav h2 {
    float: left;
    font-size: 12px;
}
.header-nav em {
    border-bottom: 1px solid #b7b7b7;
}
/* 头部右侧样式 */
.header-nav a {
    float: right;
    margin-left: 20px;
}
.header-nav img {
    width: 20px;
    height: 12px;
    margin-right: 12px;
}
/* 第一块 */
.header-nav .speak {
    width: 110px;
    z-index: 3000;
    padding: 15px 0;
    background: #fff;
    border: 1px solid #e54c87;
    position: absolute;
    top: 18px;
    left: 800px;
}
.header-nav .speak a {
    float: left;
    font-size: 14px;
    margin-top: 4px;
}
.header-nav .speak-one {
    position: absolute;
    width: 155px;
    left: 900px;
    top: 18px;
    padding: 15px 0;
    line-height: 30px;
    z-index: 100000;
    background: #fff;
    border: 1px solid #e54c87;
}
.header-nav .speak-one img {
    float: left;
    width: 36px;
    height: 18px;
}
.header-nav .speak-one li {
    float: left;
}
.header-nav .speak-one a {
    float: left;
    font-weight: bold;
    font-size: 12px;
}
.header-nav a:hover {
    display: block;
    text-decoration: underline;
}
.xian {
    float: right;
    display: block;
    font-weight: bold;
    font-size: 12px;
    margin-left: 20px;
    color: #e5e5e5;
}
a:hover {
    color: #e54c87;
}
</style>