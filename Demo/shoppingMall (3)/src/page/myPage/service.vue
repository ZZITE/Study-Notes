<template>
  <div class="refundfirt">
      <h1>{{ and }}</h1>
      <div class="refundfirt-header">
          <ul style="float:left;color:black;">
            <li v-for="(ldg, index) in ldgs" :key="index">
                {{ ldg }}
            </li>
          </ul>
      </div>

      <div class="refundfirt-main" id="aaa">
          <ul>
            <li v-for="(i,index) in thect" :key="index">
                <div class="refundfirt-mann">
                    <h2>{{ i.ornumber }}</h2>
                    <img :src="i.img" alt="">
                    <h3>{{ i.adi }}</h3>
                    <p>{{ i.collar }}</p>
                    <span>{{ i.colore }}</span>
                    <strong style="font-size:12px;">{{ i.sizer }}</strong>
                    <em style="font-size:12px;">{{ i.lasize }}</em>
                </div>
                    <div class="information">
                        <h2>{{ i.qian }}</h2>
                        <p>{{ i.timet }}</p>
                        <span>{{ i.type }}</span>
                        <strong>{{ i.status }}</strong>
                        <button style="color:white"  @click="removeTodo($index)">{{ i.cancel }}</button>
                    </div>
                    <el-input v-model="input" :placeholder="i.for"></el-input>
                    <p style="color: red;" v-if="cnsd">{{ i.tishi }}</p>
                </li>
          </ul>
      </div>
  </div>
</template>

<script>

export default {
    name: 'service',
    data() {
        return {
            input: '',
            cnsd: true,
            and: 'RETURNS AND EXCHANGES',
            ldgs: ['Order lnfo','UNlT PRICE','Application Date','type','Order Status'],
            thect: [
                {   
                    ornumber: 'Order NO.8T902765',
                    img:'static/images/usa.png',
                    adi: 'ADlDAS',
                    collar: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
                    colore: 'Color:white',
                    sizer: 'Size:8',
                    lasize: 'Label Size : L',
                    qian: '$15.00',
                    timet: '2017-08-17 04:15:03',
                    type: 'Refund only',
                    status: 'waiting process',
                    cancel: 'cancel',
                    for: 'REASONS FOR REFUND',
                    tishi: '退款原因:'
                },
                {   
                    ornumber: 'Order NO.8T902765',
                    img:'static/images/usa.png',
                    adi: 'ADlDAS',
                    collar: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
                    colore: 'Color:white',
                    sizer: 'Size:8',
                    lasize: 'Label Size : L',
                    qian: '$15.00',
                    timet: '2017-08-17 04:15:03',
                    type: 'Refund only',
                    status: 'waiting process',
                    cancel: 'cancel',
                    for: 'REASONS FOR REFUND',
                    tishi: '退款原因:'
                },
            ]
        }
    },
    methods: {  
         removeTodo: function (index) {  
             this.thect.splice(index, 1);  
        }  
    }  
}
</script>

<style>
.refundfirt {
    width: 860px;
    height: 635px;
    margin: 0 auto;
    margin-top: -34px;
}
.refundfirt h1 {
    width: 100%;
    font-size: 16px;
    margin-top: 20px;
    border-bottom: 1px solid #B7B7B7;
}
.refundfirt-header {
    width: 100%;
    height: 29px;
    margin-top: 10px;
    border-bottom: 1px solid #b7b7b7;
}
.refundfirt-header li {
    float: left;
    font-size: 12px;
}
.refundfirt-header li:nth-child(2) {
    margin-left: 300px;
}
.refundfirt-header li:nth-child(3) {
    margin-left: 55px;
}
.refundfirt-header li:nth-child(4) {
    margin-left: 100px;
}
.refundfirt-header li:nth-child(5) {
    margin-left: 80px;
}
.refundfirt-main {
    float: left;
    width: 100%;
}
.refundfirt-main ul {
    float: left;
}
.refundfirt-main li {
    float: left;
}
.refundfirt-mann {
    float: left;
    width: 327px;
}
.refundfirt-mann img {
    float: left;
    width: 78px;
    height: 108px;
    margin-right: 10px;
    margin-top: 4px;
}
.refundfirt-mann h2 {
    margin: 20px 0 10px 0;
    font-size: 12px;
    color: #595959;
}
.refundfirt-mann h3 {
    float: left;
    width: 210px;
    margin-bottom: 4px;
    font-size: 14px;
    color: #0F0F0F;
}
.refundfirt-mann p {
    float: left;
    width: 210px;
    height: 34px;
    font-size: 12px;
    color: #595959;
    overflow: hidden;
}
.refundfirt-mann span {
    display:block;
    float:left;
    width:210px;
    margin-top: 2px;
    font-size:12px;
    color:#0F0F0F;
}
.refundfirt-mann strong {
    display:block;
    float:left;
    width:210px;
    font-size:12px;
    margin-top: 2px;
    color:#0F0F0F;
}
.information {
    float: left;
    width: 500px;
    height: 100%;
    margin: 47px 0 0 33px;
}
.information h2 {
    float: left;
    margin: 0;
    font-size: 14px;
    color: #0F0F0F;
}
.information p {
    float: left;
    font-size: 14px;
    margin-left: 55px;
    color: #0F0F0F;
}
.information span {
    display: block;
    float: left;
    width: 80px;
    margin: 0 0 0 55px;
    font-size: 14px;
    color: #0F0F0F;
}
.information strong {
    display: block;
    float: left;
    width: 97px;
    margin: 0 0 0 30px;
    font-size: 14px;
    color: #0F0F0F;
}
.information button {
    float: right;
    width: 71px;
    height: 100%;
    margin: 10px 17px 0 0;
    outline: 0;
    border: 0;
    border-color: #F85292;
    background: #F85292;
}
.refundfirt-main .el-input__inner {
    height: 64px;
    margin-top: 10px;
    padding: 0 0 35px 10px;
    border-radius: 0;
}
</style>