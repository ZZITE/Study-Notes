<template>
<!-- 退货 -->
  <div class="tuiment">
    <div class="tuiment-header">
      <div style="float:left;" class="block">
        <span class="demonstration"></span>
        <label style="margin-left:20px;" for="">订单搜索:
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
      <el-button @click="Show">高级搜索</el-button>
      <div id="mask" style="display:none;" class="mask"></div>
      <div id="div1" class="div1">
          <h2>{{ scron }}</h2>
          <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item class="inputone" label="订单货号：" prop="name">
              <el-input v-model="ruleForm.name" placeholder="订单序列号"></el-input>
            </el-form-item>
              <el-form-item label="下单时间：" required>
              <el-date-picker
                v-model="value44"
                type="datetimerange"
                :picker-options="pickerOptions2"
                placeholder="选择时间范围"
                align="right">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="商品信息：" prop="region">
            <el-input v-model="ruleForm.region" placeholder="编码/商品名称/设计师"></el-input>
            </el-form-item>
              <el-form-item label="收货信息：" prop="desc">
              <el-input v-model="ruleForm.desc" placeholder="电话/收货人/地址"></el-input>
            </el-form-item>
            <el-form-item label="用户名：" prop="mesg">
              <el-input v-model="ruleForm.mesg"></el-input>
            </el-form-item>
            <div class="typer">
              <el-form-item label="付款状态" prop="type">
              <el-checkbox-group v-model="ruleForm.type">
                <el-checkbox label="待付款" name="type"></el-checkbox>
                <el-checkbox label="待备货" name="type"></el-checkbox>
                <el-checkbox label="待发货" name="type"></el-checkbox>
                <el-checkbox label="已发货" name="type"></el-checkbox>
                <el-checkbox label="已完成" name="type"></el-checkbox>
              </el-checkbox-group>
            </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="submitForm('ruleForm')">筛选</el-button>
                  <el-button style="margin-left:20px;" @click="font">取消</el-button>
                  <el-button @click="resetForm('ruleForm')">清空筛选</el-button>
                </el-form-item> 
            </div>
          </el-form>
      </div>
      <div class="ation-nav">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="所有退货" name="first">
            <div class="class-z">
              <el-checkbox style="float:left;" v-model="checked">订单号<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></el-checkbox>
              <span style="float:left;width:9%;text-align:right;">邮箱</span>
              <span style="float:left;width:20.4%;text-align:right;">申请原因</span>
              <span style="float:left;width:25%;text-align:right;">申请时间<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:14%;text-align:right;">申请状态 <img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:10%;text-align:right;">当前进度<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:7%;text-align:right;">操作</span>
            </div>
            <ul>
              <li v-for="(order,index) in orders" :key="index">
                <el-checkbox style="float:left;width:14%;" v-model="checked">{{ order.dingdan }}</el-checkbox>
                <span style="float:left;width:19%;text-align:left;">{{ order.email }}</span>
                <p style="float:left;width:18%;overflow:hidden;">{{ order.address }}</p>
                <span style="float:left;width:13.3%;text-align:right;">{{ order.money }}</span>
                <span style="float:left;width:8%;text-align:right;">{{ order.time }}</span style="float:left;">
                <span style="float:left;width:10.5%;text-align:right;">{{ order.number }}</span>
                <div style="float:left;width:9.2%;text-align:right;" class="bonter">
                  <span @click="Shoe" style="display:block;cursor:pointer">{{ order.fund }}</span>
                  <span>{{ order.fahuo }}</span>
                </div>
                <div id="mask" style="display:none;" class="mask"></div>  
                <div id="query" class="query">
                  <div style="height:29px" class="dingxin">
                    <h2 style="float:left;font-size:16px;color:#4C4C4C;margin:5px 0 0 96px;">订单信息</h2>
                  </div>
                  <h2 style="float:left;margin:30px 190px 20px 116px;">订单编号：201709185632145</h2>
                  <span style="float:left;width:300px;margin:30px 0 20px 0;">订单状态：已付款/<strong>未备货</strong>/未发货/未配送</span>
                  <span style="float:left;width:385px;margin-left:114px;">下单时间：2017-05-05 10:25:25</span>
                  <button class="chacha" @click="font"> X</button>
                  <span style="float:left;margin:0 0 0 0px;width:380px;">支付时间：2017-09-09 09:09:09</span>
                  <span style="float:left;width:100%;margin:20px 0 20px 116px;">物流信息：这里显示物流当前信息</span>
                  <div style="float:left;margin-bottom:20px;height:29px;" class="dingxin">
                    <h2 style="float:left;font-size:16px;color:#4C4C4C;margin:5px 0 0 96px;">客户信息</h2>
                  </div>
                  <span style="float:left;margin: 0 0 0 116px;width:100%;">邮箱：1222232122@qq.com</span>
                  <span style="float:left;margin:20px 227px 0 116px">收件人：亚历克斯·艾伯特</span>
                  <span style="float:left;margin-top:20px;">联系人电话：12136545646</span>
                  <span style="float:left;width:100%;margin:20px 0 0 116px;">收货地址：美利坚合众国 加利福尼亚州 某某街 某某楼某某号</span>
                  <span style="float:left;width:100%;margin: 20px 0 29px 116px;">买家留言：这是留言内容</span>
                  <div style="float:left;margin-bottom:20px;height:29px" class="dingxin">
                    <h2 style="float:left;font-size:16px;color:#4C4C4C;margin:5px 0 0 96px;">商品信息</h2>
                  </div>
                  <div class="enger">
                    <div class="touhan">
                      <em style="width:415px;">产品信息</em>
                      <em style="width:137px;">属性</em>
                      <em style="width:68px;">数量</em>
                      <em style="width:68px;">单价</em>
                      <em style="width:68px;">优惠</em>
                    </div>
                    <ul>
                        <li v-for="(txer, index) in txers" :key="index">
                          <div class="nowone">
                            <span style="margin: 15px 0 0 0;" class="colore">{{ txer.span }}</span>
                            <img :src="txer.img" alt="">
                            <p style="float:left;margin:0 0 0 0;width:347px;overflow:hidden;">{{ txer.main }}</p>
                          </div>
                          <div class="nowtwo">
                            <em style="margin-top: 7px;">{{ txer.color }}</em>
                            <em>{{ txer.big }}</em>
                            <em>{{ txer.label }}</em>
                          </div>
                          <div class="nowthree">
                            <em>{{ txer.jian }}</em>
                          </div>
                          <div class="nowfour">
                            <em>{{ txer.money }}</em>
                          </div>
                          <div class="nowfive">
                            <em>{{ txer.yhmoney }}</em>
                          </div>
                        </li>
                    </ul>
                  </div>
                  <div class="nowsix">
                      <h2 style="color:black;float:right;margin-top:8px;">合计：<span style="color:black;margin-left:30px;">数量：2</span><span style="color:black;margin-left:30px;">实付：2</span></h2>
                  </div>
                  <div style="float:left;margin-bottom:10px;height:29px" class="dingxin">
                    <h2 style="float:left;font-size:16px;color:#4C4C4C;margin:5px 0 0 96px;">预单备注</h2>
                  </div>
                  <!-- <div style="float:left;" class="nowent"> -->
                      <label for="" style="float:left;margin-bottom:10px;">
                          <em style="width:50px;height:10px;float:right;margin:0;" v-if='flag'><span style="float:left;">{{ orders.inputer }}</span></em>
                          <input type="text" v-model="orders.inputer" v-else @change='input()'>
                          <button style="float:left;color:#4C4C4C;margin: 0 0 0 117px;" @click='edit(orders)'>输入备注内容: </button>
                      </label>
                  <!-- </div> -->
                  <div style="float:left;height:29px" class="dingxin">
                    <h2 style="float:left;font-size:16px;color:#4C4C4C;margin:5px 0 0 96px;">操作</h2>
                  </div>
                  <div class="caozuo">
                      <button>发货</button>
                      <button>导出</button>
                  </div>
                </div>
              </li>
            </ul>
          </el-tab-pane>
          <el-tab-pane label="未处理" name="second">2</el-tab-pane>
          <el-tab-pane label="处理中" name="third">3</el-tab-pane>
          <el-tab-pane label="完成退货" name="five">5</el-tab-pane>
          <el-tab-pane label="拒绝退货" name="six">6</el-tab-pane>
        </el-tabs>
      </div>
    </div>
        <div class="positioning">
            <el-checkbox style="float:left;margin-top:6px;color:#4D4D4D;" v-model="checked">导出快递信息</el-checkbox>
            <span style="float:left;margin:6px 0 0 19px;color:#4D4D4D;">导入快递信息</span>
            <span style="float:left;margin:6px 0 0 19px;color:#4D4D4D;">导出地址信息</span>
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
        flag:true,
        currentPage1: 5,
        currentPage2: 5,
        currentPage3: 5,
        currentPage4: 4,
        checked: true,
        activeName: 'first',
        value3: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
        ruleForm: {
          name: '',
          region: '',
          type: [],
          typet: [],
          mesg: '',
          desc: '',
        },
        orders: [
          {
            dingdan: '800193290244713',
            email: '1296532122@qq.com',
            number: '无进度',
            address: '衣服有点小，因为胸比较大装不下，颜色也衬托不出少女心，就是这样的',
            money: '2017-09-07 19:12:52',
            time: '未处理',
            fund: '查看',
            fahuo: '发货',
          },
        ],
        txers: [
          {
            span: '800193290244713',
            img: 'static/images/shang.png',
            main: '[示例商品]Gap简约流行青年休闲长裤小脚裤|男装350486 深色水洗',
            color: 'Color: White',
            big: 'Size: 8',
            label: 'label Size: L',
            jian: '1件',
            money: '58.00',
            yhmoney: '10.00'
          },
          {
            span: '800193290244713',
            img: 'static/images/shang.png',
            main: '[示例商品]Gap简约流行青年休闲长裤小脚裤|男装350486 深色水洗',
            color: 'Color: White',
            big: 'Size: 8',
            label: 'label Size: L',
            jian: '1件',
            money: '58.00',
            yhmoney: '10.00'
          },
        ],
        rules: {
          name: [
            { required: true, message: '请输入订单序号', trigger: 'blur' },
            { min: 8, max: 15, message: '长度在 8 到 15 个字符', trigger: 'blur' }
          ],
          mesg: [
          	{ required: true, message: '请输入用户名', trigger: 'blur' }
          ],
          region: [
            {required: true, message: '请输入信息', trigger: 'blur' }
          ],
          type: [
            { type: 'array', required: true, message: '请至少选择一个', trigger: 'change' }
          ],
          typet: [
            { type: 'array', required: true, message: '请至少选择一个', trigger: 'change' }
          ],
          desc: [
            { required: true, message: '请填写信息', trigger: 'blur' }
          ]
        },
        scron: '高级搜索:',
        input2: '',
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
          }]
        },
        value4: '',
        value44: ''
      };
    },
     methods: {
        handleIconClick(ev) {
        console.log(ev);
      },
      Show: function () {
            var div1 = document.getElementById("div1");
            var mask = document.getElementById("mask");
            div1.style.display = "block";
            mask.style.display = "block";
      },
      font: function () {
            var div1 = document.getElementById("div1")
            var query = document.getElementById("query")
            var mask = document.getElementById("mask")
            query.style.display = "none";
            div1.style.display = "none";
            mask.style.display = "none";
      },
      Shoe: function () {
            var query = document.getElementById("query");
            var mask = document.getElementById("mask")
            query.style.display = "block";
            mask.style.display = "block"
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      handleClick(tab, event) {
        console.log(tab, event);
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      edit(orders){
        orders.inputer = ''
        this.flag=false;
        },
        input(){
        this.flag=true;
        },
    }
  };
</script>

<style>
.tuiment {
    float: left;
    width: 100%;
    height: 100%;
    background: #F6F6F6;
}
.tuiment-header {
  float: left;
  width: 100%;
  padding: 30px 0 0 0px;
  height: 86px;
  background: #fafafa;
}
.tuiment-header button:hover {
  color: #E54C87;
}
.tuiment-header .el-input__icon+.el-input__inner {
  width: 330px;
  height: 32px;
  border-radius: 0;
}
.tuiment-header .el-input__icon {
  right: 20px;
}
.tuiment-header .el-input {
  width: 330px;
  height: 32px;
  margin-left: 20px;
}
.tuiment-header button {
    font-size: 14px;
    border: 0;
    outline: 0;
    color: #747474;
    background: #fafafa;
}
.el-table__body-wrapper, .el-table__footer-wrapper, .el-table__header-wrapper {
    border: 0;
}
.tuiment .el-tabs__item.is-active {
    color: #E54C87;
}
.div1 {
  position: fixed;
  display: none;
  top: 0;
  right: 0;
  width: 1641px;
  height: 340px;
  z-index: 1000;
  padding: 20px 0 30px 19px;
  background: #fafafa;
}
.div1  h2 {
  font-size: 14px;
  color: #747474;
}
.div1 .el-input__inner{
  width: 330px;
  height: 32px;
  border-radius: 0;
}
.div1 .el-input__icon {
  top: 2px;
  right: 0;
}
.div1 .el-form-item {
  float: left;
  width: 600px;
}
.div1 button:hover:nth-child(1) {
  color: pink;
}
.div1 button:hover {
  color: #E54C87;
}
.div1 .el-button--primary {
  width: 90px;
  height: 30px;
  color: white;
  background: #E54C87;
  border-radius: 0;
}
.div1 .el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.div1 .el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.div1 .el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.div1 .el-checkbox__inner::after {
  left: 2px;
  top: -1px;
  border-color: #e54c87;
}
.typer {
  width: 500px;
}
.typer button {
  margin-top: 22px;
}
.el-form-item__content {
  height: 35px;
}
.tuiment-header .ation-nav {
  width: 100%;
  height: 52px;
} 
.tuiment-header .el-tabs__item:hover {
  text-decoration: underline;
}
.tuiment-header .el-tabs__item.is-active {
  color: #E54C87;
}
.tuiment-header .el-tabs__item {
  font-size: 16px;
}
.tuiment-header .el-tabs__active-bar {
  height: 0;
}
.tuiment-header .el-tabs__nav-scroll {
  margin-top: 10px;
}
.class-z {
  width: 100%;
  height: 28px;
  padding-top: 5px;
  background: #F6F6F6;
}
.el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.el-checkbox__inner::after {
  left: 2px;
  top: -1px;
  border-color: #e54c87;
}
.el-tabs__header {
  margin: 0;
}
.class-z span {
  color: #4D4D4D;
}
.ation-nav li {
  width: 100%;
  height: 62px;
  padding-top: 10px;
  border-top: 1px solid #E5E5E5;
}
.ation-nav .el-checkbox__label {
  margin-left: 20px;
}
.ation-nav li:hover {
  background: #f9f5f6;
}
.ation-nav li:active {
  background: #E5E5E5;
}
.fooner {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 1660px;
  height: 32px;
  background: #E3E3E3;
}
.fooner .el-pagination__total {
  display: none;
}
.ation-nav .el-checkbox {
  margin-left: 20px;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
    background: #E3E3E3;
}
.el-pager li {
    background: #E3E3E3;
}
.ation-nav .query {
  display: none;
  position: fixed;
  top: 10px;
  left: 565px;
  width: 1000px;
  height: 869px;
  z-index: 1000;
  background: #FAFAFA;
  box-shadow: 1px 1px 5px 1px rgba(112,5,46,0.3);
}
.ation-nav .chacha {
  position: relative;
  top: -27px;
  left: 160px;
  cursor: pointer;
  background: #F6F6F6;
}
.el-form-item__error {
  left: 20px;
}
.query strong {
  color: #E54C87;
}
.query h2 {
  color: #747474;
}
.query span {
  color:#747474;
}
.enger {
  float: left;
  width: 761px;
  /* height: 100%; */
  margin-left: 118px;
  border: 1px solid #E5E5E5;
  background: #FAFAFA;
}
.enger .touhan {
  width: 100%;
  height: 33px;
  background: #F6F6F6;
}
.enger em {
  float: left;
  display: block;
  text-align: center;
  line-height: 33px;
  border-right: 1px solid #E5E5E5;
}
.enger li {
  padding: 0;
  height: 108px;
  border-bottom: 1px solid #E5E5E5;
}
.enger .nowone {
  float: left;
  height: 86px;
  padding-top: 22px;  
  border-right: 1px solid #E5E5E5; 
}
.enger .colore {
  /* float: left; */
  color: #4C4C4C;
}
.enger img {
  float: left;
  width: 38px;
  height: 46px;
  margin: 10px 10px 0 20px;
}
.enger .nowtwo {
  float: left;
  width: 137px;
  height: 108px;
  border-right: 1px solid #E5E5E5;
}
.enger .nowtwo em {
  height: 20px;
  margin: 0 0 0 20px;
  border: 0;
}
.enger .nowthree {
  float: left;
  width: 68px;
  height: 108px;
  border-right: 1px solid #E5E5E5;
}
.enger .nowthree em {
  margin: 8px 0 0 20px;
  border: 0;
}
.enger .nowfour {
  float: left;
  width: 68px;
  height: 108px;
  border-right: 1px solid #E5E5E5;
}
.enger .nowfour em {
  margin: 8px 0 0 20px;
  border: 0;
}
.nowfive {
  float: left;
  width: 68px;
  height: 108px;
}
.enger .nowfive em {
  margin: 8px 0 0 20px;
  border: 0;
}
.nowsix {
  float: right;
  width: 765px;
  height: 31px;
  margin-right: 118px;
  border-bottom: 1px solid #E5E5E5; 
}
.nowent {
  width: 100%;
}
.nowent li {
  border: 0;
}
.class-z img {
  width: 12px;
  height: 12px;
}
.el-date-range-picker.has-sidebar.has-time {
  margin-left: 500px;
  z-index: 1000000000000;
}
.dingxin {
  width: 100%;
  height: 35px;
  background: #F6F6F6;
  /* border-bottom: 1px solid #E5E5E5; */
}
.mask{ 
  z-index:900; 
  position:fixed!important; 
  position:absolute; 
  left:0px; top:0px; 
  width:100%;   
  height:100%;  
  background:#000; 
  filter: alpha(opacity=45); 
  opacity: 0.1; 
  -moz-opacity: 0.45; 
  -khtml-opacity: 0.45; 
}
.caozuo {
    float: left;
    width: 100%;
    height: 35px;
    padding-top: 10px;
    background: white;
}
.caozuo button:nth-child(1) {
  width: 64px;
  height: 30px;
  color: white;
  font-size: 16px;
  margin-left: 430px;
  background: #E54C87;
}
.caozuo button:nth-child(2) {
  font-size: 16px;
  margin-left: 20px;
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

</style>