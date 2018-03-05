<template>
          <div class="orders-detail-wrap">
          <span style="font-size:16px;color:#0F0F0F">My Orders</span>
          <router-link to="/payment">
          <el-button type="primary" size="small" style="float:right;margin-top:2px;margin-right:10px;width:40px;height:26px;">PAY</el-button>
          </router-link>
          <div style="width:100%;">
            
            <div class="orders-child-detail" v-for="(childItem,index) in childItem" :key="index">
              <div class="orders-child-list">
                <img style="width:62px;height:86px;float:left">
                <div style="display:inline-block;float:left;color:#0F0F0F;margin-left:14px">
                  <div style="font-size:14px;line-height:14px;">
                    {{childItem.name}} 
                  <p style="font-size:14px;line-height:12px;color:#595959;width:170px;height:37px;margin-top:10px;overflow:hidden;">
                    {{childItem.itdus}} 
                  </p>
                  </div>
                </div>
                <div style="font-size:14px;line-height:14px;margin-left:76px;float:left;">
                  <div>Color : {{childItem.color}} </div>
                  <div style="margin-top:10px;">Size : {{childItem.size}} </div>
                  <div style="margin-top:10px;">Label Size : {{childItem.labelSize}} </div>
                </div>
                <div style="font-size:14px;line-height:14px;margin-left:93px;float:left;">
                  {{childItem.price}} 
                </div>
                <div style="font-size:14px;line-height:14px;margin-left:128px;float:left;">
                  {{childItem.qty}} 
                </div>
              </div>
            </div>

            <div style="border-top: 1px solid #b7b7b7">
              <ul>
                <li class="childLi">
                  Subtotal (1 item(s)):
                  <span style="margin-left:20px;">$23.80</span>
                </li>
                <li class="childLi">
                  Discount:
                  <span style="margin-left:20px;">$0.00</span>
                </li>
                <li class="childLi">
                  Estimated Shipping:
                  <span style="margin-left:20px;">$16.80</span>
                </li>
                <li class="childLi" >
                  <p style="border-bottom:1px solid #B7B7B7;width:260px;float:right">*Estimated Tax to be collected:
                  <span style="margin-left:20px;">$0.00</span>
                  </p>
                </li>
                <li class="childLi" style="margin-top:40px;">
                  Amount Payable:
                  <span style="margin-left:20px;">$40.60</span>
                </li>
                <li style="float:left;margin-top:40px;border-bottom:1px solid #b7b7b7">
                  Shipping Address
                </li>
                <li style="float:right;margin-top:40px;font-size:16px;">sdsd</li>
                <li style="float:left;margin-top:10px;width:100%;">
                  <span style="margin-right:10px;">Howard T Villarreal</span>
                  <span>2301 Oakwood CircleL</span>
                  <span>Los Angeles</span>
                  <span>United States</span>
                  <span>900172310</span>
                  <span>949-340-8238</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
</template>
<<script>
export default {
  name: 'orDetail',
  data () {
    return {
      childItem : [
        {
          time: '2017-08-29 04:27:28 Order NO.8T902765',
          name: 'ADIDAS',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          color: 'White',
          size: '8',
          labelSize: 'L',
          price: '$15.00',
          qty: '10000',          
        },
        {
          time: '2017-08-29 04:27:28 Order NO.8T902765',
          name: 'ADIDAS',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          color: 'White',
          size: '8',
          labelSize: 'L',
          price: '$15.00',
          qty: '1',          
        },
        {
          time: '2017-08-29 04:27:28 Order NO.8T902765',
          name: 'ADIDAS',
          itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
          color: 'White',
          size: '8',
          labelSize: 'L',
          price: '$15.00',
          qty: '1',          
        }
      ]
    }
  }
}
</script>
<style>
.orders-child-detail {
  width: 100%;
  height: 106px;
}
.orders-child-list {
  margin-top: 10px;
}
.childLi {
  text-align: right;
}
.orders-detail-wrap {
  height: 100%;
  width: 860px;
  margin-top: -20px;
}
.orders-detail-wrap::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden; 
}


.el-pagination button.disabled {
  background: #fafafa;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
  background: #fafafa;
}
.el-pager li.active {
  border-color: #fafafa;
  background-color: #fafafa;
  color: #E54C87;
  cursor: default;
}
.el-pager li:hover {
  color: #E54C87;
}
.el-pager li.btn-quicknext, .el-pager li.btn-quickprev {
    line-height: 22px;
}
.el-icon-arrow-right:hover {
  color: #E54C87;
}
.el-icon-arrow-left:hover {
  color: #E54C87;
}
.btn-next:hover {
  color:  #E54C87;
}
.el-button--primary {
  width: 35px;
  height: 20px;
  line-height: 4px;
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
.orders-a:hover{
  color: #E54C87;
  text-decoration: underline;
  text-decoration-style: solid 2px;
}
</style>

