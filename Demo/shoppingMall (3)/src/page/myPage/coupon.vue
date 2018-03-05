<template>
  <div class="volume">
    <h1>{{ mycou }}</h1>
    <h2>{{ card }}</h2>
    <el-input v-model="input55" :placeholder="code"></el-input>
    <el-button type="success">{{ und }}</el-button>
    <p>{{ needs }}</p>
    <div class="tabs">
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane :label="one" name="first">{{ not }}</el-tab-pane>
            <el-tab-pane :label="two" name="second">{{ yongyou }}</el-tab-pane>
            <el-tab-pane :label="three" name="third">{{ guoqi }}</el-tab-pane>
        </el-tabs>
    </div>
  </div>
</template>

<script>

export default {
    data() {
        return {
            activeName: 'second',
            input55: '',
            und: 'Activate',  
            mycou: 'MY COUPON',
            card: 'COUPON CARD',
            code: 'Enter Gift Code',
            needs: 'Gift code needs to be activated for usage.Please refresh the page if you cannot view the activated coupon.',
            one: 'UNUSED',
            two: 'EXPIRED',
            three: 'USED',
            not: 'You have no Coupon right now',
            yongyou: '121354531321',
            guoqi: '2017/09/16'
        }
    },
      methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      }
    }
}
</script>

<style>
.volume {
    width: 860px;
    height: 100%;
    margin-top: -34px;
}
.volume h1 {
    width: 100%;
    font-size: 16px;
    margin-top: 20px;
    color: #0F0F0F;
    border-bottom: 1px solid #B7B7B7;
}
.volume h2 {
    font-size: 14px;
    margin: 20px 0 10px 0;
    color: #0F0F0F;
}
/* input样式 */
.volume .el-button--success {
    float: left;
    width: 78px;
    height: 40px;
    background: #f85292;
    border: #f85292;
    border-radius: 0;
}
/* input样式 */
.volume .el-input {
    float: left;
    width: 300px;
    height: 40px;
    border-radius: 0;
}
/* 设置圆角样式 */
.volume .el-input__inner {
    border-radius: 0;
    height: 40px;
}
.volume p {
    float: left;
    width: 100%;
    margin-top: 10px;
    font-size: 12px;
    color: #595959;
}
.volume .tabs {
    float: left;
}
.volume .tabs .el-tabs__active-bar {
    width: 100%;
    height: 0;
}
.volume .el-tabs__item.is-active {
    color: #E54C87;
}
.volume .el-tabs__header {
    width: 860px;
    border-bottom: 1px solid #d1dbe5;
}
.volume .el-tabs__item {
    height: 38px;
    padding: 0 20px 0 0;
    color: #0F0F0F;
}
</style>