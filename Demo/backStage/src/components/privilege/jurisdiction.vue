<template>
<!-- 角色 -->
    <div class="user2">
        <div class="user2-main">

            <label style="color:#747474;margin-left:20px;" for="">角色查询：
                <el-input
                    placeholder="输入权限名称"
                    icon="search"
                    v-model="input2"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>


            <button @click="addShow=true;adduser()" style="float:right;margin-right:20px;">新建权限</button>

            <!--编辑-->
            <div id="mask" class="mask" v-if="editShow"></div>
            <div id="increase" class="increase" v-if="editShow">
                <el-collapse v-model="activeNames">
                    <el-collapse-item style="" title="基本资料">
                        <div class="data">
                            <label style="float:left;" for="">权限名称：
                                <input type="text" v-model="editname">
                            </label>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="拥有功能">
                        <el-table
                            :data="tableData2"
                            border
                            style="width: 100%;height:500px;overflow:scroll;">
                            <el-table-column
                            prop="url"
                            label="URL"
                            width="220">
                            </el-table-column>
                            <el-table-column
                            prop="desc"
                            label="功能描述"
                            width="220">
                            </el-table-column>
                            <el-table-column
                            label="操作">
                            <template scope="scope">
                            <el-checkbox-group v-model="editIdList">
                                <el-checkbox :label="item.id" v-for="(item,index) in scope.row.operation_set" :key="index">{{item.operation}}</el-checkbox>
                            </el-checkbox-group>
                            </template>

                            </el-table-column>
                        </el-table>
                    </el-collapse-item>
                </el-collapse>
                <div class="operation">
                  <button @click="editput">确认</button>
                  <button @click="editShow=false;editId=[]">取消</button> 
                  <button @click="deluser">删除</button> 
                </div>
            </div>

            <!-- 添加 -->
            <div class="datatwo" v-if="addShow">
                <el-collapse v-model="activeNames">
                    <el-collapse-item style="" title="基本资料">
                        <div class="data">
                            <label style="float:left;" for="">权限名称：
                                <input type="text" v-model="newUserName">
                            </label>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="拥有功能">
                        <el-table
                            :data="tableData"
                            border
                            style="width: 100%">
                            <el-table-column
                            prop="url"
                            label="URL"
                            width="220">
                            </el-table-column>
                            <el-table-column
                            prop="desc"
                            label="功能描述"
                            width="220">
                            </el-table-column>
                            <el-table-column
                            label="操作">

                            <template scope="scope">
                            <el-checkbox-group v-model="newnewUserId">
                                <el-checkbox :label="item.id" v-for="(item,index) in scope.row.operation_set" :key="index">{{item.operation}}</el-checkbox>
                            </el-checkbox-group>
                            </template>

                            </el-table-column>
                        </el-table>
                    </el-collapse-item>
                    <el-collapse-item style="" title="操作">
                        <div class="operation-nav">
                            <button @click="submitAdduser">确定</button>
                            <button @click="addShow=false;newnewUserId=[]">取消</button> 
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <!-- <div id="optional" class="optional">
                <div class="opter">
                    <h2 style="float:left;margin:10px 0 0 99px;">ADMIN 可用的角色</h2>
                </div>
                <ul style="float:left;width:1360px;height:657px;background:#fafafa;padding:30px 0 0 119px;">
                    <li style="float:left;margin-bottom:39px;" v-for="(weter,index) in weters" :key="index">
                         <h2 style="float:left;width:100%;margin-bottom:30px;border-bottom:1px solid #E5E5E5;">{{ weter.A }}</h2>
                         <el-checkbox-group v-model="checkList">
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理" ></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理" ></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理"></el-checkbox>
                            <el-checkbox label="订单管理" ></el-checkbox>
                        </el-checkbox-group>
                    </li>
                </ul>
                <div class="xuanze">
                    <strong>确定</strong>
                    <strong @click="quxiao">取消</strong>
                </div>
            </div> -->
        </div>

        <!-- 主体 -->
        <div class="class-z">
            <span style="width: 3%;display:inline-block;text-align:right">ID</span>
            <span style="width: 17%;display:inline-block;text-align:right">角色名称</span>
            <span style="float:right;margin-right:70px;display:inline-block;">操作</span>
        </div>
        <ul style="">
            <li style="float:left;width:100%;height:52px;border-bottom:1px solid #E5E5E5;line-height:52px" v-for="(list, index) in users" :key="index">
                <span style="width: 3%;display:inline-block;text-align:right">{{list.id}}</span>
                <span style="width: 18%;display:inline-block;text-align:right">{{list.name}}</span>
                <a style="float:right;margin-right:70px;display:inline-block;" @click="editShow = true;edit(list.id)">编辑</a>
            </li>
        </ul>





        <div class="positioning">
            <el-pagination style="float:right;height:100%;"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage"   
            :page-size="50"
            layout="total, prev, pager, next"
            :total="totalpage">
            </el-pagination>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
      return {
        checkList: ['复选框 A'],
        checkList: ['',''],
        /*tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: [1,2,3]
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }],*/
        activeNames: ['1'],
        checked: true,
        input2: '',
        users: [],
        totalpage: null,
        currentPage: 1,
        editShow: false,
        addShow: false,
        newUserName:'',
        tableData: [],
        tableData2: [],
        newnewUserId:[],
        editname: '',
        editId: null,
        editIdList: [],
        editname: ''
      }
    },
    methods: {
      dataloading : function () {
          var self = this
          axios.get('/account/role' + '?bg=1')
            .then(function (res) {
                console.log(res)
                self.users = res.data.object_list
                self.totalpage = res.data.page.count
            })
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      handleIconClick: function () {

      },
      adduser: function () {
          var self = this
          axios.get('/account/permission?page=all&o=group')
            .then(function (res) {
                console.log(res)
                self.tableData = res.data.object_list
            })
            .catch(function(err) {
                alert(err)
            })
      },
      hand: function () {
          var div1 = document.getElementById("mask")
          var div22 = document.getElementById("datatwo")
          div22.style.display="none"
          div1.style.display = "none"
      },
      submitAdduser: function () {
          var self = this
          axios.post('/account/role', {
              name: self.newUserName,
              permission_ids: self.newnewUserId
          })
           .then(function (res) {
                if (res.data.success) {
                alert('提交成功')
                self.addShow = false
                self.dataloading()
              } else {
                  if (res.data.message) {
                      alert('名称已存在')
                  } else {
                      alert('输入非法')
                  }
              }
            })
            .catch(function (err) {
              if (err.response.status === 403) {
                    alert('没权限')
                }
            })
      },
      edit: function (id) {
          var self = this
          axios.get('/account/role/' + id + '?bg=1')
            .then(function (res) {
                console.log(res)
                self.tableData2 = res.data.all_permission_set
                self.editname = res.data.name
                self.editIdList = res.data.permission_set
                self.editId = res.data.id
            })
            .catch(function () {
                alert('err')
            })
      },
      editput: function () {
          var self = this
          axios.put('/account/role/' + self.editId, {
              name: self.editname,
              permission_ids: self.editIdList
          })
            .then(function (res) {
                if (res.data.success) {
                alert('提交成功')
                self.editShow = false
                self.dataloading()
              } else {
                  if (res.data.message) {
                      alert('名称已存在')
                  } else {
                      alert('输入非法')
                  }
              }
            })
            .catch(function (err) {
              if (err.response.status === 403) {
                    alert('没权限')
                } else if (err.response.status === 404) {
                    alert('对象不存在')
                }
            })
      },
      deluser: function () {
        var self = this
        var r = confirm('是否删除角色？')
        if (r) {
        axios.delete('/account/role/' + self.editId)
            .then(function (res) {
                if (res.data.success) {
                    alert('删除成功')
                }
                self.editShow = false
                self.dataloading()
            })
            .catch(function (err) {
                 if (err.response.status === 404) {
                    alert('对象不存在')
                } else if (err.response.status === 403) {
                    alert('没有权限')
                }
                self.editShow = false
                self.dataloading()
            })
        } else {
            return;
        }
    }

    //   roles: function () {
    //       var div33 = document.getElementById("optional")
    //       var div2 = document.getElementById("increase")
    //       div33.style.display="block"
    //       div2.style.display="none"
    //   },
    //   quxiao: function () {
    //       var div33 = document.getElementById("optional")
    //       var div1 = document.getElementById("mask")
    //       div33.style.display="none"
    //       div1.style.display="none"
    //   }
    },
    created: function () {
        this.dataloading()
    }
  }
</script>

<style scoped>
.user2 {
    min-width:1366px;
    width: 100%;
    height: 100%;
    background: #fafafa;
    position: relative;
}
.user2-main {
    height: 32px;
    padding: 30px 20px;
}
.user2-main .el-input {
    width: 330px;
    height: 36px;
    border-radius: 0; 
}
.user2 .el-input__inner {
    border-radius: 0;
}
.user2-main label {
    margin-left: 20px;
}
.user2-main button {
    width: 90px;
    height: 30px;
    border: 0;
    outline: 0;
    color: white;
    background: #E54C87;
    cursor: pointer;
}
.user2-main .class-z {
    height: 24px;
    padding-top: 10px;
    border-top: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
    background: #F6F6F6;
}

 /* 底部 */
.positioning {
    position: fixed;
    height: 32px;
    right: 0;
    bottom: 0;
    background: #E3E3E3;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
    background: #E3E3E3;
}
.el-pager li {
    background: #E3E3E3;
}
.increase {
    position: absolute;
    float: left;
    left: 400px;
    top: 100px;
    width: 1000px;
    z-index: 9999;
    background: #FAFAFA;
}
.operation {
    width: 100%;
    
    text-align: center;
}
.operation button {
    margin: 100px 0 10px 20px;
}
.user2 .mask{ 
  z-index:900; 
  position:fixed!important; 
  position:absolute; 
  left:0px; top:0px; 
  width:100%;   
  height:100%;  
  background:#000; 
  filter: alpha(opacity=45); 
  opacity: 0.45; 
  -moz-opacity: 0.45; 
  -khtml-opacity: 0.45; 
}
.user2 .ment {
    height: 34px;
    background: #F6F6F6;
}
.user2-main .el-collapse-item__header {
    margin: 0;
    height: 34px;
    padding-left: 93px;
    background: #f6f6f6;
}
.user2-main .el-collapse-item__content {
    padding: 0;
}
.user2-main .data {
    height: 50px;
    margin-left: 30px;
    margin-top: 10px;
}
.user2-main .data span {
    color: #4C4C4C;
}

.datatwo {
    position: absolute;
    float: left;
    left: 400px;
    top: 100px;
    width: 1000px;
    z-index: 9999;
    background: #FAFAFA;
}
.user2 .datatwo input {
    width: 269px;
    height: 28px;
}
.user2 .operation-nav {
    padding: 11px 0 11px 420px;
}
.user2 .operation-nav button{
    width: 50px;
    height: 30px;
    border: 0;
    margin-right: 30px;
    color: white;
    outline: none;
    background: #E54C87;
    border-radius: 4px;   
}
.user2 .operation-nav button:hover {
    border: 1px solid #fff;
}
.user2 .operation-nav button:active {
    background: #fff;
    color: #E54C87;
}
.user2 .optional {
    display: none;
    position: fixed;
    width: 1600px;
    height: 900px;
    z-index: 1000;
    background: #fafafa;
}
.user2 .optional .opter {
    height: 34px;
    background: #F6F6F6;
    border-bottom: 1px solid #E5E5E5;
}

.user2 .bottom {
    position: relative;
    float: left;
    top: 50px;
    left: 400px;
    width: 300px;
}
.user2 .bottom strong {
    display: block;
    float: left;
    width: 90px;
    height: 30px;
    color: #4C4C4C;
    line-height: 30px;
    text-align: center;
}


.user2 .waten {
    float: left;
    width: 707px;
    height: 32px;
    border: 1px solid #E5E5E5;
    background: #f6f6f6;
}
.user2 .waten span {
    display: block;
    float: left;
    height: 100%;
    line-height: 32px;
    margin-left: 9px;
}

.user2 a:hover{
    color: #E54C87;
    text-decoration:underline;
    cursor: pointer;
}
</style>