<template>
<!-- 设计师 -->
    <div class="Designer">
        <div class="Designer-header">
            <label style="float:left;margin-left:20px;" for="">设计师搜索：
                <el-input
                    @keyup.enter.native="handleIconClick"
                    placeholder=""
                    icon="search"
                    v-model="search"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>
            <button @click="show2=true" style="float:right;margin-top:50px;margin-right:30px;">新增设计师</button>
            <div id="xinzeng" class="xinzeng" v-if="show2">
                <div style="height:32px;" class="laeb">
                    <label for="">名称:
                    <el-input v-model="adddesignermes.name" placeholder="必须为英文，长度不超过32位" :maxlength="32"></el-input>
                    </label>
                    <label for="">中文备注:
                    <el-input v-model="adddesignermes.chinesename" placeholder="可选"></el-input>
                    </label>
                </div>
                <label style="float:left;margin-top:29px;margin-right:80px;" for="">
                    介绍:
                    <textarea v-model="adddesignermes.detail" style="float:right;margin-left:20px; width:632px;height:150px" placeholder="必填"></textarea>
                </label>
                <div class="designerBtn" style="width:100%;text-align:center;margin-top:20px;float:left">
                    <button  @click="addDesigner" style="margin-left:-50px;">确定</button>
                    <button  @click="show2=false">取消</button>
                </div>
            </div>
        </div>

        <div class="de-section" style="" v-for="(item, index) in designers" :key="index">
          <h2>{{item.initial}}</h2>
          <div class="de-name">
            <ul style="float:left;height:100%;overflow:hidden;">
              <li style="float:left;" v-for="(i, index) in item.item" :key="index">
                <a  class="de-a" @click="edit(i.id);shent()">   
                    {{ i.name }}({{i.name_desc}})
                </a>
              </li>
            </ul>

            <div id="mask" v-if="show" class="mask"></div>

              <transition name="fade">
              <div v-if="show" class="spender" >                
                    <h2 style="height:36px;line-height:36px;margin-left:0px;background:#F6F6F6">
                        <p style="margin-left:40px;font-size:16px;color:#4C4C4C">基本资料</p>
                    </h2>
                        <div class="data">
                            <span style="float:left;margin-left:120px">英文名称：<span v-if="!show3">{{detailEdit.name}}</span>
                            <input v-model="detailEdit.name" v-if="show3"></input>
                            </span>
                            <input style="float:left;margin-left:-30px" v-if="false"></input>
                            <span style="float:left;margin-left:293px;">中文备注：<span v-if="!show3">{{detailEdit.name_desc}}</span>
                            <input v-model="detailEdit.name_desc" v-if="show3"></input>
                            </span>
                        </div>
                    <h2 style="height:36px;line-height:36px;margin-left:0px;margin-top:10px;background:#F6F6F6">
                        <p style="margin-left:40px;font-size:16px;color:#4C4C4C">设计师介绍</p>
                    </h2>
                        <div style="width:100%;text-align:center;margin:20px 0;">
                        <textarea style="width:800px;height:200px;" v-model="detailEdit.desc"></textarea>
                        </div>
                    <h2 style="height:36px;line-height:36px;margin-left:0px;margin-top:10px;background:#F6F6F6">
                        <p style="margin-left:40px;font-size:16px;color:#4C4C4C">商品介绍</p>
                    </h2>
                        <div style="height:30px;padding-top:20px;">
                            <span style="float:left;margin-left:120px;">商品总数：50件</span>
                            <span style="float:left;margin-left:154px;">出售中：40件</span>
                            <span style="float:left;margin-left:168px;padding-bottom:20px;">已下架：10件</span>
                        </div>
                        <div>
                            <h2 style="height:36px;line-height:36px;margin-left:0px;margin-top:10px;background:#F6F6F6">
                                <p style="margin-left:40px;font-size:16px;color:#4C4C4C">追随</p>
                            </h2>
                            <p style="margin: 10px 0 10px 120px;">追随人数：{{detailEdit.follower_count}}</p>
                        </div>
                        <!--
                            <div style="width:100%;text-algin:center;margin:0 auto;">
                            <el-table
                                :data="tableData3"
                                height="250"
                                border
                                style="width: 100%">
                                <el-table-column
                                prop="date"
                                label="邮箱"
                                width="553">
                                </el-table-column>
                                <el-table-column
                                prop="name"
                                label="追随者时间"
                                width="183">
                                </el-table-column>
                            </el-table>
                            </div>
                        -->

                <div class="designerBtn" style="width:100%;text-align:center;margin-top:120px;">
                    <button @click="show3=true">编辑</button>
                    <button @click="editsubmit">提交</button>
                    <button @click="delDesigner">删除</button>
                    <button @click="show = false;show3=true">关闭</button>
                </div>
              </div>
              </transition>
          </div>
      </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            show2: false,
            show: false,
            show3: false,
            detailEdit: {},
            tableData3: [
                {
                    date: '123456789@qq.com',
                    name: '2017-05-05 20:20:15',
                    }, {
                    date: 'ncsncsansajbfvvxz@yahoo.com',
                    name: '2017-05-05 20:20:15',
                    }, {
                    date: '123456789@163.com',
                    name: '2017-05-05 20:20:15',
                }, 
            ],
            adddesignermes: {
                name: '',
                chinesename: '',
                detail: '',
            },
            search: '',
           designers: {}
        }
    },
    methods: {
    dataloading: function () {
        var self = this
        axios.get('/designer?o=alpha&page=all&bg=1')
          .then(function (res) {
              // console.log(res)
              self.designers = res.data.object_list
          })
          .catch(function (err) {
              console.log(err)
        })
    },
    handleIconClick() {
      var self = this
      axios.get('/designer?bg=1&o=alpha&search=' + self.search)
        .then(function (res){
            console.log(res)
            self.designers = res.data.object_list
        })
    },
    shent: function () {
        this.show = true
    },
    // 设计师添加
    addDesigner: function () {
        var self = this
        axios.post('/designer', {
            name: self.adddesignermes.name,
            name_desc: self.adddesignermes.chinesename,
            desc: self.adddesignermes.detail
        })
          .then(function (res) {
              console.log(res)
              if (res.data.success) {
                alert('提交成功')
                self.adddesignermes.name = ''
                self.adddesignermes.chinesename = ''
                self.adddesignermes.detail = ''
                self.show2 = false
                self.dataloading()
              } else {
                  if (res.data.message == 'name exist') {
                      alert('设计师名字已存在，不允许重复')
                  } else {
                      alert('输入非法')
                  }
              }
          })
    },
    // 设计师编辑获取数据
    edit: function (id) {
        var self = this
        axios.get('/designer/' + id + '?bg=1')
            .then(function (res) {
                console.log(res)
                self.detailEdit = res.data
            })
            .catch(function (err) {
                if (err.response.status === 404) {
                    alert('对象不存在')
                }
                self.show = false
                self.dataloading()
            })
    },
    // 设计师编辑更改提交
    editsubmit: function () {
        var self = this
        axios.put('/designer/' + self.detailEdit.id, {
          name: self.detailEdit.name,
          name_desc: self.detailEdit.name_desc,
          desc: self.detailEdit.desc
        })
          .then(function (res) {
              console.log(res)
              if (res.data.success) {
                alert('提交成功')
                self.show = false
                self.dataloading()
              } else {
                  if (res.data.message == 'name exist') {
                      alert('设计师名字已存在，不允许重复')
                  } else {
                      alert('输入非法')
                  }
              }
          })
          .catch(function (err) {
              if (err.response.status === 404) {
                    alert('对象不存在')
                    self.show = false
                    self.dataloading()
                }
          })
    },
    delDesigner: function () {
        var self = this
        var r = confirm('是否删除设计师？')
        if (r) {
        axios.delete('/designer/' + self.detailEdit.id)
            .then(function (res) {
                if (res.data.success) {
                    alert('删除成功')
                }
                self.show = false
                self.dataloading()
            })
            .catch(function (err) {
                 if (err.response.status === 404) {
                    alert('对象不存在')
                } else if (err.response.status === 403) {
                    alert('没有权限')
                }
                self.show = false
                self.dataloading()
            })
        } else {
            return;
        }
    }
  },
    created: function() {
        this.dataloading()
    }
}
</script>

<style scoped>
.Designer {
    width: 100%;
    height: 100%;
    background: #fafafa;
}
.Designer-header {
  width: 100%;
  padding: 30px 0 0 0px;
  background: #fafafa;
}
.Designer-header .el-input__icon+.el-input__inner {
  width: 330px;
  height: 32px;
  border-radius: 0;
}
.Designer-header .el-input__icon {
  right: 20px;
}
.Designer-header .el-input {
  width: 330px;
  height: 32px;
  margin-left: 20px;
}
.Designer-header button {
    width: 90px;
    height: 30px;
    background: #E54C87;
    border: 0;
    color: white;
    outline:none;
}
.Designer h2 {
    height: 26px;
    margin-left: 20px;
    border-bottom: 1px solid #E5E5E5; 
}
.de-section {
  width: 100%;
  float: left;
}
.de-name {
  width: 100%;
}
.de-a:hover{
  color:#E54C87;
  text-decoration: underline;
}
.de-a {
  float: left;
  width: 100%;
  display: block;
  font-size: 14px;
  color: #595959;
  margin-left: 39px;
  margin-top: 10px;
  margin-bottom: 10px; 
}
.de-content::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
.xinzeng {
    position: absolute;
    top: 200px;
    left: 650px;
    width: 775px;
    height: 376px;
    padding: 30px 0 0 99px;
    background: white;
}
.xinzeng .el-input {
    width: 280px;
}
.xinzeng .el-input__inner{
  /* float: left; */
  width: 269px;
  height: 32px;
  border-radius: 0;
}
.xinzeng button {
    width: 25px;
    height: 13px;
    margin-top: 8px;
    font-size: 12px;
    color: #BDBDBD;
    cursor:pointer;
    background: white;
}

.spender {
    position: absolute;
    width: 1000px;
    height: 840px;
    left: 500px;
    top: 80px;
    z-index: 1000;
    background: white;
}
.mask{ 
  z-index:900; 
  position:fixed!important; 
  position:absolute; 
  left:0px; top:0px; 
  width:100%;   
  height:100%;  
  background: rgba(0,0,0, 0.1); 
  filter: alpha(opacity=45); 
  opacity: 0.45; 
  -moz-opacity: 0.45; 
  -khtml-opacity: 0.45; 
}

.spender .data {
    padding: 20px 0 30px 0;
    font-size: 14px;
}
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
.designerBtn button{
    width: 50px;
    height: 30px;
    margin-left: 30px;
    border: 0;
    color: white;
    outline: none;
    background: #E54C87;
    border-radius: 4px;   
}
.designerBtn button:hover {
    border: 1px solid #fff;
}
.designerBtn button:active {
    background: #fff;
    color: #E54C87;
}
.de-a {
    cursor: pointer;
}
</style>
