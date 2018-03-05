<template>
  <div class="cart">
    <bread></bread>

    <div class="shopbag">
      <div class="bagtitle">
        <h2 style="font-size:16px;color:#0F0F0F;margin-left:10px;">Your shopping bag</h2>
        <div style="width:1080px;margin: 16px 0 10px 20px;"> 
          <span style="margin-left:25px;">ITEM</span>
          <span style="margin-left:70px;">DESCRIPTION</span>
          <span style="margin-left:70px;">ITEM SPECIFICS</span>
          <span style="margin-left:50px;">UNIT PRICE</span>
          <span style="margin-left:40px;">QUANTITY</span>
          <span style="margin-left:60px;">EDIT</span>
        </div>

            <div class="orders-child-detail" v-for="(item,index) in cart" :key="index">
              <div class="orders-child-list">
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
                  <el-input-number size="small" v-model="num" :min="1"></el-input-number>
                </div>
                <div style="font-size:12px;line-height:14px;float:right;height:50px;">
                  <a class="orders-a" @click="remove(index)">REMOVE</a>
                  <a class="orders-a" @click="addtofa(index)">{{fa}}</a>
                </div>
              </div>
            </div>

      </div>
    </div>
    <div class="shopsub">
      <h2 style="font-size:16px;color:#0F0F0F;margin-top: 10px">Subtotal (1 Item):{{submoney}}</h2>
      <p style="font-size:12px;color:#595959;">(Excluding freight)</p>
      <router-link to="/payment">
        <el-button type="primary" size="small" style="width:240px;height:35px;margin-top:20px;font-size:18px;">Proceed To Checkout</el-button>
      </router-link>
    </div>
  </div>
</template>

<script>
import bread from '@/components/breadcrumb'
export default {
  name: 'cart',
  data () {
    return {
      fa: 'MOVE TO FAVORITES',
      money: '',
      num: 1,
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
      ]
    }
  },
  components: {
    bread 
  },
  methods: {
    remove: function (index) {
      this.cart.splice(index, 1)
    },
    addtofa: function (index) {
      console.log('jiacanshu')
    }
  },
  computed: {
    submoney: function () {
      var l = this.cart.length
      var moneytotal = 0;
      var num
      if (l > 0) {
        var fuhao = this.cart[0].price.substring(0, 1)
        for (var i = 0; i < l; i ++) {
        num = Number(this.cart[i].price.substring(1))
        moneytotal += num
        }
          return fuhao + moneytotal
      }
      return 0;
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cart {
  width: 1080px;
  height: 100%;
  margin: 0 auto;
}
.cart::after {
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
.shopsub {
  float:right;
  margin-top: 20px;
  width: 310px;
  height: 130px;
  background: #ffffff;
  text-align: center;
}
span {
  font-size: 12px;
  color: #0F0F0F ;
}
.orders-child-detail {
  margin-bottom: 20px;
  width: 100%;
  height: 106px;
  border-top: 1px solid #E5E5E5;
}
.orders-child-list {
  margin-top: 20px;
  text-align: center;
}
.orders-a {
  margin-top: 20px;
  display: block;
  margin-bottom: 10px;
  font-size: 12px;
  text-align: left;
}
.orders-a:hover {
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

</style>