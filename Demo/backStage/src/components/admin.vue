<template>
<!-- 商品管理 -->
  <div class="spment">
    <div class="spment-header">
      <div style="float:left;" class="block">
        <span class="demonstration"></span>
        <label style="margin-left:20px;float:left;" for="">订单搜索:
            <el-input style="margin-left:20px;"
                placeholder="订单编号、电话号码"
                icon="search"
                v-model="input2"
                :on-icon-click="handleIconClick">
            </el-input>
        </label>
      </div>
      <div class="fabu">
          <button @click="skel">商品发布</button>
      </div>
      <div id="release" class="release">
        <div class="ziliao">
          <el-collapse v-model="activeNames">
            <el-collapse-item style="" title="基本资料">
              <span class="inputten"><strong>商品分类：</strong>
                    <el-select v-model="value4" clearable placeholder="NEW IN">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                    <el-select v-model="value45" clearable placeholder="NEW IN">
                      <el-option
                        v-for="item in option"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
              </span>
              <span><strong>商品名称：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
              <span><strong>SEO关键词：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
              <span><strong>SEO描述：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
              <span><strong>商品编号：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
              <span style="border-bottom:0;"><strong>价格：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
            </el-collapse-item>
            <el-collapse-item style="" title="产品信息">
              <span class="inputten"><strong>设计师：</strong>
                    <el-select v-model="value54" clearable placeholder="NEW IN">
                      <el-option
                        v-for="item in iptions"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
              </span>
              <span><strong>产品故事：</strong>
                <input style="margin:20px 0 0 30px;" type="text">
              </span>
              <span class="mtdata" style="height:145px;"><strong style="height:80px;padding:65px 0 0 40px;">模特：</strong>
                <em style="border-top:0;">
                  <label for="">身高：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em style="border-top:0;">
                  <label for="">胸围：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em style="border-top:0;">
                  <label for="">腰围：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em style="border-top:0;">
                  <label for="">臀围：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em style="border-right:0;border-top:0;width:760px;">
                  <label for="">所穿尺码：
                    <input type="text">
                  </label>
                </em>
                <em>
                  <label for="">臂宽：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em>
                  <label for="">体重：
                    <input type="text">
                    KG
                  </label>
                </em>
                <em>
                  <label for="">腿长：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em>
                  <label for="">腰围：
                    <input type="text">
                    CM
                  </label>
                </em>
                <em style="border-right:0;width:760px;"></em>
              </span>
              <span class="laueny" style="border-bottom:0;"><strong>洗衣技巧：</strong>
                  <el-checkbox v-model="checked">Cotton textile washing(括号里面为中文标注)</el-checkbox>
                  <el-checkbox v-model="checked">Cotton textile washing(棉纺织品洗法)</el-checkbox>
                  <el-checkbox v-model="checked">Wool and polyester blended fabric(羊毛与涤纶混纺面料)</el-checkbox>
                  <p class="newguess">新增</p>
              </span>
            </el-collapse-item>
            <el-collapse-item style="" title="产品属性">
              <span  class="laueny"><strong>主要材质:</strong>
                  <el-checkbox style="width:100px;" v-model="checked">斜纹布(Twill)</el-checkbox>
                  <el-checkbox style="width:100px;" v-model="checked">尼龙(nylon)</el-checkbox>
                  <el-checkbox style="width:100px;" v-model="checked">SATIN(色丁面料）</el-checkbox>
                  <p class="newguess">新增</p>
              </span>
              <span  class="laueny"><strong style="height:170px;padding:15px 0 0 40px;">英文:<p>(中文备注)</p></strong>
                  <el-checkbox style="width:100px;" v-model="checked">蝴蝶结(Bow)</el-checkbox>
                  <el-checkbox style="width:180px;" v-model="checked">动物图案(Animal pattern)</el-checkbox>
                  <el-checkbox style="width:100px;" v-model="checked">卡通形象(Cartoon)</el-checkbox>
                  <p class="newguess">新增</p>
              </span>
              <span class="laueny" style="border-bottom:0;"><strong style="height:170px;padding:15px 0 0 40px;">Opening:<p>(开口类型)</p></strong>
                  <el-checkbox style="width:170px;" v-model="checked">Zipper hasp(拉链搭扣)</el-checkbox>
                  <el-checkbox style="width:100px;" v-model="checked">Velcro(魔术贴)</el-checkbox>
                  <el-checkbox style="width:100px;" v-model="checked">Covered type(包盖式)</el-checkbox>
                  <p class="newguess">新增</p>
              </span> 
            </el-collapse-item>
            <el-collapse-item style="" title="商品规格">
              <span class="laundry"><strong>尺寸标准 (单选)：</strong>
                <el-radio-group style="float:left;width:500px;" v-model="radio2">
                  <el-radio :label="3">美上衣标准</el-radio>
                  <el-radio :label="6">美裤子标准</el-radio>
                  <el-radio :label="9">美直筒半裙标准</el-radio>
                  <el-radio :label="12">背心连衣裙</el-radio>
                </el-radio-group>
                <p class="newguess" style="margin: 25px 0 0 0;">新增</p>
              </span>
              <div class="content">
                <span class="lauenyy" style="border-top: 1px solid #E5E5E5;border-left: 1px solid #E5E5E5;border-right: 1px solid #E5E5E5"><strong>颜色:</strong>
                  <el-checkbox v-model="checked">红色</el-checkbox>
                  <el-checkbox v-model="checked">绿色</el-checkbox>
                  <el-checkbox v-model="checked">蓝色</el-checkbox>
                  <p class="newguess" style="margin-left:20px;">新增</p>
                </el-radio-group>
                </span>
                <span style="border-left: 1px solid #E5E5E5;border-right: 1px solid #E5E5E5"><strong>价格:</strong>
                  <input style="width:49px;height:32px;margin:20px 0 0 34px;" type="text">
                </span>
                <span style="border-left: 1px solid #E5E5E5;border-right: 1px solid #E5E5E5"><strong>尺码库存:</strong>
                  <input style="float:left;width:49px;height:32px;margin:20px 0 0 34px;" type="text">
                  <img @click="ethan" style="margin:20px 0 0 10px;border:1px solid #E5E5E5;width:32px;height:34px;" src="static/images/jiahao.png" alt="">
                  <div style="display:none;" id="tomrter" class="tomrter">
                    <label style="float:left;margin:21px 0 0 21px;width:400px;" for="">尺码：
                      <el-checkbox class="lauenyy" v-model="checked">红色</el-checkbox>
                      <el-checkbox class="lauenyy" v-model="checked">绿色</el-checkbox>
                      <el-checkbox class="lauenyy" v-model="checked">蓝色</el-checkbox>
                    </label>
                    <label style="float:left;margin:21px 0 0 21px;width:100%;" for="">库存：
                      <input style="width:36px;height:32px;" type="text">
                    </label>
                      <p class="newguess" style="margin:21px 0 0 200px;">确定</p>
                      <p @click="echter" class="newguess" style="margin:21px 0 0 20px;border:0;color:#747474;">取消</p>
                  </div>
                </span>
                <span style="height:100%;border-left: 1px solid #E5E5E5;border-right: 1px solid #E5E5E5"><strong style="height:122px; padding: 19px 0px 0px 19px;">图片: <p style="color:#A2A2A2;">最少5张</p></strong>
                  <el-upload
                    action="https://jsonplaceholder.typicode.com/posts/"
                    list-type="picture-card"
                    :on-preview="handlePictureCardPreview"
                    :on-remove="handleRemove">
                    <i class="el-icon-plus"></i>
                  </el-upload>
                  <el-dialog v-model="dialogVisible" size="tiny">
                    <img width="100%" :src="dialogImageUrl" alt="">
                  </el-dialog>
                </span>
              </div>
            </el-collapse-item>
          </el-collapse>
          <button class="classification">增加颜色图片分类</button>
          <button class="classifiton">确定发布</button>
        </div>
      </div>
      <div id="mask" style="display:none;" class="mask"></div>
      <div class="ation-maine">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="所有商品" name="first">
            <div class="class-z">
              <el-checkbox style="float:left;" v-model="checked">商品编号<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></el-checkbox>
              <span style="float:left;width:8%;text-align:right;">商品</span>
              <span style="float:left;width:22%;text-align:right;">价格<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:7%;text-align:right;">库存<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:6%;text-align:right;">状态</span>
              <span style="float:left;width:9.5%;text-align:right;">上架时间<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:12%;text-align:right;">修改时间<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
              <span style="float:left;width:7.5%;text-align:right;">类别</span>
              <span style="float:left;width:7%;text-align:right;">设计师</span>
              <span style="float:left;width:6%;text-align:right;">操作</span>
            </div>
            <ul>
              <li v-for="(order,index) in orders" :key="index">
                  <el-checkbox style="float:left;margin-top:10px;width:14%;" v-model="checked">{{ order.dingdan }}</el-checkbox>
                  <span style="float:left;width:19%;text-align:left;">
                    <img style="float:left;width:25px;height:32px;margin: 4px 10px 0 0;" :src="order.imag" alt="">
                    {{ order.ping }}
                  </span>
                  <span style="float:left;width:3.5%;text-align:right;">{{ order.meney }}</span>
                <div class="quter">
                  <div class="color">
                    <em style="margin-right:26px;">{{ order.colorone }}</em>
                    <em style="margin-right:23px;">{{ order.colortwo }}</em>
                    <em>{{ order.colorthree }}</em>
                  </div>
                  <span style="float:left;margin: 0 100px 0 75px;color:#E54C87;">{{ order.geshu }}</span>
                </div>
                <span style="float:left;text-align:left;color:#E54C87;"><strong style="float:left;width:100%;color:#4C4C4C;">{{ order.zhuangta }}</strong>{{ order.zhuangtai }}</span style="float:left;">
                <span style="float:left;text-align:right;">{{ order.shangtime }}</span>
                <span style="float:left;width:12%;text-align:right;">{{ order.xiutime }}</span>
                <span style="float:left;width:4.5%;text-align:right;"><strong style="float:left;width:100%;">{{ order.type1 }}</strong>{{ order.type2 }}</span style="float:left;">
                <span style="float:left;width:7%;text-align:right;">{{ order.sheji }}</span>
                <div style="float:left;width:6%;text-align:right;" class="bonter">
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
                  <span style="float:left;margin:20px 227px 0 116px;">收件人：亚历克斯·艾伯特</span>
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
          <el-tab-pane label="出售中" name="second">2</el-tab-pane>
          <el-tab-pane label="已售完" name="third">3</el-tab-pane>
          <el-tab-pane label="已下架" name="five">5</el-tab-pane>
        </el-tabs>
      </div>
    </div>
        <div class="positioning">
            <el-checkbox style="float:left;margin-top:6px;color:#4D4D4D;" v-model="checked">上架</el-checkbox>
            <span style="float:left;margin:6px 0 0 19px;color:#4D4D4D;">下架</span>
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
        dialogImageUrl: '',
        dialogVisible: false,
        radio2: 3,
        iptions: [{
          value: '选项1',
          label: '糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value54: '',
        option: [{
          value: '选项1',
          label: '糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }],
        value45: '',
        flag:true,
        activeNames: ['1'],
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
            imag:'static/images/xia.png',
            ping: '[示例商品]Gap简约流行青年休闲长裤小脚裤|男装350486 深色水洗',
            shangtime: '2017-05-06 20:30:20',
            meney: '$20.65',
            geshu: '20件',
            zhuangta: '出售中',
            zhuangtai: '首页显示',
            xiutime: '2017-05-06 20:30:20',
            type1: '裙子',
            type2: '短裙',
            sheji: '老王',
            fund: '编辑',
            fahuo: '下架',
            colorone: 'red(红色)：50',
            colortwo: 'blue(蓝色)：10',
            colorthree: 'yellow(黄色)：10'
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
        value44: '',
        value4: ''
      };
    },
     methods: {
        handleIconClick(ev) {
        console.log(ev);
      },
      font: function () {
            var query = document.getElementById("query")
            var mask = document.getElementById("mask")
            query.style.display = "none";
            mask.style.display = "none";
      },
      Shoe: function () {
            var query = document.getElementById("query");
            var mask = document.getElementById("mask")
            query.style.display = "block";
            mask.style.display = "block"
      },
      skel: function () {
            var release = document.getElementById("release")
            release.style.display = "block";
      },
      ethan: function () {
            var tomrter = document.getElementById("tomrter")
            tomrter.style.display = "block"
      },
      echter: function () {
            var tomrter = document.getElementById("tomrter")
            tomrter.style.display = "none"
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
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

<style scond>
.spment {
    float: left;
    width: 100%;
    height: 100%;
    background: #F6F6F6;
}
.spment-header {
  float: left;
  width: 100%;
  padding: 30px 0 0 0px;
  height: 86px;
  background: #fafafa;
}
.spment-header button:hover {
  color: #E54C87;
}
.spment-header .el-input__icon+.el-input__inner {
  width: 330px;
  height: 32px;
  border-radius: 0;
}
.spment-header .el-input__icon {
  right: 20px;
}
.spment-header .el-input {
  width: 330px;
  height: 32px;
  margin-left: 20px;
}
.spment-header button {
    font-size: 14px;
    border: 0;
    outline: 0;
    color: #747474;
    background: #fafafa;
}
.el-table__body-wrapper, .el-table__footer-wrapper, .el-table__header-wrapper {
  border: 0;
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
.spment-header .ation-maine {
  float: left;
  width: 100%;
  height: 52px;
} 
.spment-header .el-tabs__item:hover {
  text-decoration: underline;
}
.spment-header .el-tabs__item.is-active {
  color: #E54C87;
}
.spment-header .el-tabs__item {
  font-size: 16px;
}
.spment-header .el-tabs__active-bar {
  height: 0;
}
.spment-header .el-tabs__nav-scroll {
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
.ation-maine li {
  width: 100%;
  height: 62px;
  padding-top: 10px;
  border-top: 1px solid #E5E5E5;
}
.ation-maine .el-checkbox__label {
  margin-left: 20px;
}
.ation-maine li:hover {
  background: #f9f5f6;
}
.ation-maine li:active {
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
.ation-maine .el-checkbox {
  margin-left: 20px;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
    background: #E3E3E3;
}
.el-pager li {
    background: #E3E3E3;
}
.ation-maine .query {
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
.ation-maine .chacha {
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
  width: 415px;
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
.spment .fabu {
    position: relative;
    float: right;
    top: 45px;
    right: 50px;
    width: 90px;
    height: 30px;
    z-index: 10;
    cursor: pointer;
    background: #E54C87;
}
.spment .fabu button {
    color: white;
    margin-left:15px; 
    line-height: 30px;
    cursor: pointer;    
    background: #E54C87;
}
.spment .fabu button:hover {
    color: pink;
}
.release {
    display: none;
    position: fixed;
    width: 1660px;
    height: 1080px;
    top: 0;
    z-index: 1000;
    background: #FAFAFA;
}
.ziliao span {
  display: block;
  float: left;
  width: 1660px;
  height: 72px;
  background: #FAFAFA;
  border-bottom: 1px solid #E5E5E5;
  /* background: paleturquoise; */
}
.ziliao em {
  color: #747474;
}
.ziliao strong {
  display: block;
  float: left;
  width: 160px;
  height: 43px;
  padding: 29px 0 0 40px;
  border-right: 1px solid #E5E5E5;
  /* background: cadetblue; */
}
.inputten .el-input__icon+.el-input__inner {
  width: 250px;
  height: 32px;
}
.inputten .el-input {
    width: 250px;
    height: 32px;
    margin-top: 20px;
    margin-left: 30px;
}
.spment .el-collapse-item__content {
  padding: 0;
}
.spment .el-collapse-item__header {
  background: #F6F6F6;
}
.ziliao input {
  width: 664px;
  height: 32px;
}
.spment .mtdata em {
  display: block;
  float: left;
  width: 173px;
  height: 52px;
  padding: 20px 0 0 0;
  border-right: 1px solid #E5E5E5;
  border-top:  1px solid #E5E5E5;
}
.spment .mtdata input {
  width: 49px;
  height: 32px;
}
.spment .mtdata label {
  margin: 0 0 0 20px;
}
.laundry .el-radio-group {
  width: 1457px;
}
.laundry span {
  width: 14px;
  height: 14px;
  border-bottom: 0;
}
.laundry .el-radio-group .el-radio {
  width: 110px;
  margin: 30px 0 0 0;
}
.laundry .el-radio-group .el-radio:nth-child(1) {
  width: 110px;
  margin: 22px 0 0 20px;
}
.laundry .el-radio-group .el-radio:nth-child(4) {
  width: 110px;
  margin: 22px 0 0 20px;
}


.laueny span {
  width: 13px;
  height: 13px;
}
.laueny .el-checkbox {
  float: left;
  width: 300px;
  margin: 20px 0 0 30px;
}
.laueny .el-checkbox:nth-child(3) {
  float: left;
  width: 250px;
  margin: 20px 0 0 20px;
}
.laueny .el-checkbox__input.is-checked .el-checkbox__inner {
  margin-top: 5px;
}
.laueny .el-checkbox__inner {
  margin-top: 5px;
}
.newguess {
  float: left;
  width: 43px;
  height: 18px;
  text-align: center;
  line-height: 18px;
  margin: 20px 0 0 100px;
  color: #E54C87;
  border: 1px solid #E54C87;
}
.spment .content {
  float: left;
  width: 1580px;
  height: 360px;
  margin-top: 20px;
  margin-left: 20px;
}
.content span {
  width: 1580px;
  margin: 0 auto;
}
.content strong {
  padding: 29px 0 0 19px;
}
.lauenyy span {
  width: 13px;
  height: 13px;
}
.lauenyy .el-checkbox {
  float: left;
  width: 50px;
  margin: 20px 0 0 30px;
}
.lauenyy .el-checkbox__input.is-checked .el-checkbox__inner {
  margin-top: 5px;
}
.lauenyy .el-checkbox__inner {
  margin-top: 5px;
}
.spment .el-upload--picture-card {
  width: 100px;
  height: 100px;
  margin: 20px 0 0 34px;
}
.spment .el-icon-plus:before {
    position: relative;
    top: -20px;
}
.spment .classification {
  float: left;
  width: 132px;
  height: 32px;
  margin: 20px 600px 0 700px;
  color: #E54C87;
  border: 1px solid #E54C87;
}
.spment .classifiton {
  float: left;
  width: 274px;
  height: 40px;
  margin: 60px 0 0 640px;
  color: white;
  background: #E54C87;
}
.spment .classifiton:hover {
  color: pink;
}
.spment .tomrter {
  position: absolute;
  width: 500px;
  height: 147px;
  top: 473px;
  left: 220px;
  z-index: 10;
  box-shadow: 1px 1px 5px #E54C87;
  background: white;
}
.spment .color {
  position: absolute;
  display: none;
  float: left;
  width: 388px;
  height: 32px;
  left: -120px;
  bottom: -20px;
  padding: 20px 0 0 20px;
  background: white;
  box-shadow: 1px 1px 5px #E54C87;
}
.quter {
  position: relative;
  float: left;
}
.quter:hover .color {
  display: block;
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