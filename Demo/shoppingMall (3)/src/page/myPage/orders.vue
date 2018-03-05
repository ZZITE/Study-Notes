<template>
  <div class="orders-wrap">
    <div v-if="parent">
      <div class="orders-title-right">
          <span style="font-size:16px;color:#0F0F0F">My Orders</span>
      </div>
      <div class="orders-content">
        <div class="category">
          <span style="margin-left:130px;">Order Info</span>
          <span style="margin-left:180px;">UNIT PRICE</span>
          <span style="margin-left:60px;">QTY</span>
          <span style="margin-left:90px;">Order Status</span>
          <span style="margin-left:100px;">Action</span>
        </div>
        <div class="orders-list" v-for="(item,index) in items" :key="index">
          <div class="orders-time">{{item.time}}</div>
          <div class="orders-imgDiv">
            <div class="orders-img">
              <img :src="item.src"/>
            </div>
            <div class="orders-detail">
              <h3>{{item.name}}</h3>
              <p>
                {{item.itdus}}
              </p>
                <span>Color : {{item.color}}</span>
                <span>Size : {{item.size}}</span>
                <span>Label Size : {{item.labelSize}}</span>
            </div>
          </div>

          <div class="orders-pay">
            <router-link to="/payment">
            <el-button type="primary" v-if="item.pay" size="small" class="or-btn">PAY</el-button>
            </router-link>
            
          </div>
          <div class="orders-right">
            <span style="display:inline-block;width:140px;">{{item.price}}</span>
            <span style="display:inline-block;width:100px;">{{item.qty}}</span>
            <span style="display:inline-block;width:150px;">{{item.status}}</span>
          </div>

          <div style="margin:30px 1px 0 0;float:right;text-align:right;">
            <div style="float:right;">
              <router-link to="/My/Orders/Detail">
                View Order
              </router-link>
            </div>
            <div style="margin-top:40px;text-align:right;">

              <router-link v-if="item.pay" to="/My/Orders/Withdraw">
                Cancle Order
              </router-link>
              <router-link v-else to="/payment">
                Severs
              </router-link>
            </div>
          </div>

        </div>
      </div>
      <div style="width:860px;height:80px;">    
        <el-pagination class="or-pageNumber" small layout="prev, pager, next" :total="50">
        </el-pagination>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'orders',
  data () {
    return {
      parent: true,
      child: false,
      items: [
        {
        time: '2017-08-29 04:27:28 Order NO.8T902765',
        src: '',
        name: 'ADIDAS',
        itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
        color: 'White',
        size: '8',
        labelSize: 'L',
        price: '$15.00000000000',
        qty: '10000000000',
        status: 'Awaiting Payment',
        pay: true
        },
        {
        time: '2017-08-29 04:27:28 Order NO.8T902765',
        src: '',
        name: 'ADIDAS',
        itdus: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
        color: 'White',
        size: '8',
        labelSize: 'L',
        price: '$15.00',
        qty: '1',
        status: 'Awaiting Payment',
        }
      ]
    }
  },
  methods: {

  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.orders-wrap {
  width: 100%;
  height: 100%;
  margin-top: -26px;
}
.orders-title-right {
  display: inline-block;
  height: 36px;
  line-height: 36px;
  width: 860px;
  right: 0;
  border-bottom: 1px solid #b7b7b7 ;
  font-size: 14px;
  color: #0F0F0F;
}

.or-pageNumber {
  height: 16px;
  float: right;
  color: #0F0F0F 100%;
  background: #fafafa;
}
.el-pagination {
  padding: 8px 5px;
}

.el-pager li {
  background: #fafafa;
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

.category {
  width: 100%;
  height: 30px;
  line-height: 30px;
}
.category span {
  font-size: 12px;
  color: #0F0F0F;
}
.orders-list {
  position: relative;
  width: 100%;
  height: 167px;
  border-top: 1px solid #b7b7b7;
}
.orders-time {
  margin-top: 20px;
  font-size: 12px;
  color: #595959 ;
}
.orders-imgDiv {
  float: left;
  height: 120px;
  width: 340px;
}
.orders-img {
  float: left;
  height: 120px;
  width: 80px;
}
.orders-img img {
  width: 100%;
  height: 100%;
}
.orders-detail {
  float: left;
  margin-left: 10px;
}
.orders-detail p {
  display: block;
  width: 232px;
  height: 30px;
  font-size: 12px;
  color: #595959;
  overflow: hidden;
}
.orders-detail span {
  margin-top: 6px;
  display: block;
  font-size: 12px;
  color: #0F0F0F;
}
.orders-right {
  float: left;
  margin-left: 20px;
}
.orders-right span {
  font-size: 14px;
  color: #0F0F0F;
}
.orders-pay {
  width: 35px;
  height: 20px;
  position: absolute;
  right: 10px;
  top: 8px;
}
.orders-pay .el-button {
  height: 20px;
}
.el-button--primary {
  width: 35px;
  line-height: 0;
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
.or-btn {
  height: 20px;
}
</style>
