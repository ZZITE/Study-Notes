<template>
  <div class="payment">
    <!-- 购物地址 -->
    <div class="pm-address">
      <h2 style="font-size:16px;color:#0F0F0F;margin-left:10px;">SHIPPING ADDRESS</h2>
        <div class="pm-input">
            <el-radio-group v-model="radio1">
              <el-radio class="radio" :label=index v-for="(item,index) in addressBook" :key="index">
                <span v-for="(i,index) in item" :key="index" class="btsp">{{i}}</span>
              </el-radio>
            </el-radio-group>
        </div>
    </div>

     <!-- 右边价格 -->
    <div class="shopsub">
      <h2 style="font-size:16px;color:#0F0F0F;text-align: left;margin: 10px 0 4px 4px">ORDER SUMMARY</h2>
        <div class="shopsubleft">
          <p>Subtotal (1 item(s)):</p>
          <p>Discount:</p>
          <p>Estimated Shipping:</p>
          <p>*Estimated Tax to be collected:</p>
          <p>Amount Payable:</p>
        </div>
        <div class="shopsubright">
          <p>$12.00</p>
          <p>$12.00000</p>
          <p>$12.00</p>
          <p>$12.00</p>
          <p>$12.00</p>
        </div>
      <div class="payImg">
        <img src="static/images/payment1.png">
        <span style="float:left;font-size:12px;color:#595959;margin-left:10px;">or</span>
        <img style="width:175px;height:22px;margin-left:10px;" src="static/images/payment2.png">
      </div>
      <el-button type="primary" size="small" style="width:240px;height:35px;margin-top:20px;font-size:18px;">Continue</el-button>
    </div>

    <!-- 购物方式 -->
    <div class="pm-address">
      <h2 style="font-size:16px;color:#0F0F0F;margin-left:10px;">SHIPPING METHOD</h2>
        <div class="pm-input">
            <el-radio-group v-model="radio2">
              <el-radio :label="1" class="radio">
                <span style="font-size:14px;color:#0f0f0f;">Standard Delivery</span>
                <span style="font-size:14px;color:#0f0f0f;margin-left:80px;">7-12 business days</span>
                <span style="font-size:12px;color:#595959;margin-left:9px;">(excluding processing time)</span>
                <span style="font-size:14px;color:#0f0f0f;margin-left:130px;">$0.0</span>
              </el-radio>
              <el-radio :label="2" class="radio">
                <span style="font-size:14px;color:#0f0f0f;">Express Delivery</span>
                <span style="font-size:14px;color:#0f0f0f;margin-left:80px;">2-5 business days</span>
                <span style="font-size:12px;color:#595959;margin-left:9px;">(excluding processing time)</span>
                <span style="font-size:14px;color:#0f0f0f;margin-left:130px;">$15.00</span>  
              </el-radio>             
            </el-radio-group>
        </div>
    </div>

    <!-- 底下购物商品信息 -->
    <div class="shopbag">
      <div class="bagtitle">
        <h2 style="font-size:16px;color:#0F0F0F;margin-left:10px;">ORDER PREVIEWS</h2>
        <div style="width:1080px;margin: 16px 0 10px 20px;"> 
          <span style="margin-left:25px;">ITEM</span>
          <span style="margin-left:70px;">DESCRIPTION</span>
          <span style="margin-left:70px;">ITEM SPECIFICS</span>
          <span style="margin-left:50px;">UNIT PRICE</span>
          <span style="margin-left:40px;">QUANTITY</span>
          <span style="margin-left:60px;">EDIT</span>
        </div>

            <div class="pay-child-detail" v-for="(item,index) in cart" :key="index">
              <div class="pay-child-list">
                <img style="width:62px;height:86px;float:left;margin-left:25px">
                <div style="display:inline-block;float:left;color:#0F0F0F;margin-left:20px">
                  <div style="font-size:14px;line-height:14px;">
                    {{item.name}} 
                  <p style="font-size:14px;line-height:12px;color:#595959;width:170px;height:37px;margin-top:10px;overflow:hidden;">
                    {{item.itdus}} 
                  </p>
                  </div>
                </div>
                <div style="font-size:14px;line-height:14px;margin-left:30px;float:left;width:120px;">
                  <div>Color : {{item.color}} </div>
                  <div style="margin-top:10px;">Size : {{item.size}} </div>
                  <div style="margin-top:10px;">Label Size : {{item.labelSize}} </div>
                </div>
                <div style="font-size:14px;line-height:14px;float:left;width:130px;">
                  {{item.price}} 
                </div>
                <div style="font-size:14px;line-height:14px;width:70px;float:left;">
                  {{item.qty}} 
                </div>

              </div>
            </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'payment',
  data () {
    return {
      radio1: 0,
      radio2: 1,
      fa: 'MOVE TO FAVORITES',
      money: '',
      cart : [
        {
          time: '2017-08-29 04:27:28 Order NO.8T902765',
          name: 'ADIDAS',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          color: 'White',
          size: '8',
          labelSize: 'L',
          price: '$15.00',
          qty: '1'     
        },
        {
          time: '2017-08-29 04:27:28 Order NO.8T902765',
          name: 'ADIDAS',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          color: 'White',
          size: '8',
          labelSize: 'L',
          price: '$15.00',
          qty: '1'     
        }
      ],
      addressBook : [
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238'],
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238']
        ]
    }
  },
  components: {
  },
  methods: {

  },
  computed: {

  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.payment {
  width: 1080px;
  height: 100%;
  margin: 0 auto;
}
.payment::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
.shopbag {
  width: 750px;
  float: left;
  background: #ffffff;
  margin-top: 20px;
}
.pm-address {
  width: 750px;
  float: left;
  background: #ffffff;
  margin-top: 20px;
}
.shopsub {
  float:right;
  margin-top: 20px;
  width: 310px;
  background: #ffffff;
  text-align: center;
}
.bagtitle span {
  font-size: 12px;
  color: #0F0F0F ;
}
.pay-child-detail {
  width: 100%;
  height: 106px;
  border-top: 1px solid #E5E5E5;
}
.pay-child-list {
  margin-top: 10px;
  text-align: left;
}
.pay-a {
  margin-top: 20px;
  display: block;
  margin-bottom: 10px;
  font-size: 12px;
  text-align: left;
}
.pay-a:hover {
  color: #E54C87;
  text-decoration:underline;
}
.el-button--primary {

  height: 20px;
  line-height: 2px;
  font-size: 12px;
  color: #fff;
  background-color: #E54C87;
  border-color: #E54C87;
  border-radius: 0;
}
.el-button--primary:hover {
  background-color: #E54C87;
  border-color: #fff;
}
.el-button--primary:focus {
  background-color: #E54C87;
  border-color: #E54C87;
}
.el-button--primary:active {
  color: #E54C87;
  background-color: #fff;
  border-color: #E54C87;
}
.fo-content-wrap router-Link {
  color: #E54C87;
}
.el-button {
  padding: 4px 4px;
}

.pm-input {
  margin-top: 10px;
  margin-bottom: 8px;
  line-height: 20px;
}
.radio {
  display: block;
  height: 20px; 
  margin-left: 10px;
}
.el-radio+.el-radio {
  margin: 10px;
}
.el-radio__input.is-checked .el-radio__inner {
  border-color: #E54C87;
  background: #fff;
}
.el-radio__inner {
  border-radius: 0;
}
.el-radio__inner:hover {
  border-color: #E54C87;
}
.el-radio__inner:active {
  border-color: #E54C87;
}
.el-radio__inner::after {
    width: 6px;
    height: 6px;
    border-radius: 0;
    background-color: #E54C87;
    content: "";
    position: absolute;
    left: 50%;
    top: 50%;
    -ms-transform: translate(-50%,-50%) scale(0);
    transform: translate(-50%,-50%) scale(0);
    transition: transform .15s cubic-bezier(.71,-.46,.88,.6);
}
.btsp {
  margin-right: 10px;
  font-size: 14px;
  color: #0F0F0F;
}
.shopsubleft {
  float: left;
  font-size: 14px;
  color: #0F0F0F;
  text-align: right;
}
.shopsubleft p {
  margin-top: 8px;
}
.shopsubright {
  float: right;
  font-size: 14px;
  color: #0F0F0F;
  text-align: left;
}
.shopsubright p {
  margin-top: 8px;
}

.payImg {
  float: left;
  width: 100%;
  height: 31px;
}
.payImg img {
  float: left;
  width: 50px;
  height: 15px;
  margin-left: 30px;
}
</style>