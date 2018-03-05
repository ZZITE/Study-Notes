<template>
<!-- 购物车 -->
    <div class="cart">
        <!-- 购物车头部 -->
        <div class="cart-header">
            <!-- 搜索和日期 -->
            <div style="float:left;" class="block">
                <span class="demonstration"></span>
                <label style="margin-left:20px;color:#747474;" for="">订单搜索:
                <el-input style="margin-left:20px;"
                placeholder="订单编号、电话号码"
                icon="search"
                v-model="input2"
                :on-icon-click="handleIconClick">
                </el-input>
                </label>
                <el-date-picker
                v-model="value4"
                type="datetimerange"
                :picker-options="pickerOptions2"
                placeholder="选择时间范围"
                align="right">
                </el-date-picker>
            </div>
            <el-button style="margin-left:29px;">清空搜索</el-button>
        </div>
        <!-- 导航条 -->
        <div class="class">
              <el-checkbox style="float:left;" v-model="checked">邮箱</el-checkbox>
              <span style="float:left;width:24%;text-align:right;">商品</span>
              <span style="float:left;width:48%;text-align:right;">添加时间</span>
              <span style="float:left;width:18%;text-align:right;">操作</span>
        </div>
        <!-- 主内容 -->
        <ul style="float:left;width:100%;height:100%;background:#fafafa;">
            <li style="float:left;width:100%;border-bottom:1px solid #E5E5E5;" v-for="(ethan,index) in ethans" :key="index">
                <el-checkbox style="float:left;margin-top:28px;width:14%;" v-model="checked">{{ ethan.email }}</el-checkbox>
                <span style="float:left;width:20%;text-align:left;margin:20px 0 20px 180px;">
                    <img style="float:left;width:25px;height:32px;margin: 4px 10px 0 0;" :src="ethan.imag" alt="">
                    {{ ethan.ping }}
                </span>
                <span style="float:left;width:34.5%;text-align:right;margin:28px 0 0 0;">{{ ethan.time }}</span>
                <span @click="fn()" style="float:left;width:13.4%;text-align:right;margin:28px 0 0 0;cursor: pointer;">{{ ethan.operation }}</span>
            </li>
        </ul>
        <!-- 弹窗 -->
        <div v-if="show" id="tcoper" class="tcoper">
            <div class="dataone">
                <h2 style="font-size:16px;color:rgba(76,76,76,1);">基本资料</h2>
            </div>
            <div class="nameto">
                <label for="">英文名称：
                    <span>admin</span>
                </label>
            </div>
            <div style="border-top:1px solid #E5E5E5;" class="dataone">
                <h2 style="font-size:16px;color:rgba(76,76,76,1);">购物车</h2>
            </div>
            <div class="fromter">
                <span style="display:block;float:left;width:180px;height:32px;border:1px solid #E5E5E5;line-height:32px;text-align: center;background:#F6F6F6;">添加时间</span>
                <span style="display:block;float:left;width:576px;height:32px;border-top:1px solid #E5E5E5;line-height:32px;text-align:center;background:#F6F6F6;
                border-right:1px solid #E5E5E5;border-bottom:1px solid #E5E5E5;">操作</span>
                <ul style="float:left;">
                    <li style="" v-for="(num,index) in nums" :key="index">
                        <strong style="display:block;float:left;width:180px;height:70px;border-left:1px solid #E5E5E5;
                        border-right:1px solid #E5E5E5;border-bottom:1px solid #E5E5E5;line-height:70px;text-align:center;">{{ num.time }}</strong>
                        <strong style="display:block;float:left;width:576px;height:70px;border-right:1px solid #E5E5E5;
                        border-right:1px solid #E5E5E5;border-bottom:1px solid #E5E5E5;line-height:70px;">
                            <img style="float:left;width:25px;height:30px;margin:20px 11px 0 63px;" :src="num.imges" alt="">
                            <p style="float:left;overflow:hidden;">{{ num.introduce }}</p>
                        </strong>
                    </li>
                </ul>
            </div>
        </div>
        <!-- 底部 -->
        <div class="positioning">
            <el-checkbox style="float:left;margin-top:6px;color:#4D4D4D;" v-model="checked">导出邮箱</el-checkbox>
                <span style="float:left;margin:6px 0 0 19px;color:#4D4D4D;">通知客户付款</span>
                <el-pagination style="float:right;height:100%;"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage1"   
                :page-size="100"
                layout="total, prev, pager, next"
                :total="1000">
            </el-pagination>
        </div> 
    </div>
</template>
<script>
export default {
    data() {
        return {
            show: false,
            currentPage1: 5,    
            currentPage2: 5,
            currentPage3: 5,
            currentPage4: 4,
            input2: '',
            value4: '',
            checked: true,
            nums: [
                {
                    time: '2017-09-12 00:00:00',
                    imges: 'static/images/jiahao.png',
                    introduce: '[示例商品]Gap简约流行青年休闲长裤小脚裤|男装350486 深色水洗'
                },
            ],
            ethans: [
                {
                    email: '1296532122@qq.com',
                    imag: 'static/images/jiahao.png',
                    ping: '[示例商品]Gap简约流行青年休闲长裤小脚裤|男装350486 深色水洗',
                    time: '2017-09-07 19:12:52',
                    operation: '操作'
                },
            ],
            pickerOptions2: {
            shortcuts: [{
                text: '最近一周',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                    picker.$emit('pick', [start, end]);
                }
                }, {
                    text: '最近一个月',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                    picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近三个月',
                    onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                    picker.$emit('pick', [start, end]);
                    }
                }],
            },
        }
    },
    methods: {
        handleIconClick(ev) {
            console.log(ev);
        },
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
        },
        fn: function(){
            if(this.show==true){
                this.show=false;
            }else{
                this.show=true
          }
        },
    }
}
</script>

<style>
/* 主体 */
.cart {
    float: left;
    width: 100%;
    height: 100%;
    background: #F6F6F6;
}
.block .el-date-table {
   display: none;
}
/* 头部样式 */
.cart-header {
    float: left;
    width: 100%;
    padding: 30px 0 0 0px;
    height: 86px;
    background: #fafafa;
}
.cart-header button:hover {
  color: #E54C87;
}
.cart-header .el-input__icon+.el-input__inner {
  width: 330px;
  height: 32px;
  border-radius: 0;
  font-size: 12px;
  color:rgba(153,152,153,1);
}
.cart-header .el-input__icon {
  right: 20px;
}
.cart-header .el-input {
  width: 330px;
  height: 32px;
  margin-left: 20px;
}
.cart-header button {
    font-size: 14px;
    border: 0;
    outline: 0;
    color: #747474;
    background: #fafafa;
}
/* 导航条样式 */
.class {
    float: left;
    width: 100%;
    height: 28px;
    padding-top: 5px;
    background: #F6F6F6;
    border-top: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
}
.cart .el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.cart .el-checkbox {
    margin-left: 20px;
}
.cart .el-checkbox__label {
    margin: 0;
}
.cart .el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.cart .el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.cart .el-checkbox__inner::after {
  left: 2px;  
  top: -1px;
  border-color: #e54c87;
}
/* 弹窗样式 */
.tcoper {
    position: fixed;
    width: 1000px;
    height: 880px;
    left: 580px;
    top: 20px;
    z-index: 1000;
    background: white;
    box-shadow: 1px 1px 5px 1px rgba(112,5,46,0.3);
}
.dataone {
    width: 904px;
    height: 25px;
    padding: 9px 0 0 96px;
    background: #F6F6F6;
    border-bottom: 1px solid #E5E5E5;
}
.nameto {
    width: 881px;
    height: 44px;
    padding: 20px 0 0 119px;
}
/* 表单样式 */
.fromter {
    width: 762px;
    height: 865px;
    padding: 20px 119px 0 119px;
}
/* 底部 */
.positioning {
    position: fixed;
    width: 1660px;
    height: 32px;
    bottom: 0;
    z-index: 1101111;
    background: #E3E3E3;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
    background: #E3E3E3;
}
.el-pager li {
    background: #E3E3E3;
}
.positioning .el-pagination__total {
  display: none;
}
</style>        
