<template>
<!-- 用户 -->
    <div class="username">
        <div class="user-main">
            <label style="color:#747474;float:left" for="">帐号搜索：
                <el-input
                    placeholder="输入邮箱，电话号码或实名"
                    @keyup.enter.native="handleIconClick"
                    icon="search"
                    v-model="search"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>

        <!-- 角色筛选 -->
            <button id="shaixuan" style="" @click="filtershow=true;filter()">角色筛选</button>
            <div class="screent" v-if="filtershow">
                  <el-checkbox-group v-model="filterCheckList">
                    <el-checkbox :label="list.id" v-for="(list, index) in filterList" :key="index">{{list.name}}</el-checkbox>
                </el-checkbox-group>
                <div class="bottom">
                    <button @click="submitFilter">筛选</button>
                    <button @click="filtershow=false">取消</button>
                    <button @click="filterCheckList=[]">清空筛选</button>
                </div>
            </div>


            
            <button style="float:right;margin-right:20px;">新建用户</button>


        <!-- 编辑 -->
            <div id="mask" v-if="show" class="mask"></div>

            <div id="increase" class="increase" v-if="show">
                <el-collapse v-model="activeNames">
                    <el-collapse-item style="" title="基本资料">
                        <div style="height:155px;" class="data">

                            
                            <label style="margin-left:30px;" for="">生日：
                                <input type="date" v-model="userEdit.birthday">
                            </label>
                            <label style="margin-left:30px;" for="">电话：
                                <input type="text" v-model="userEdit.phone_num">
                            </label>
                            <label style="margin-left:30px;" for="">邮箱：
                                <input type="text" v-model="userEdit.email">
                            </label>
                            </br>
                            <label style="margin-top:20px;margin-left:30px;" for="">地址：
                                <input type="text">
                            </label>
                            <label style="margin-top:20px;margin-left:30px;" for="">实名：
                                <input type="text" v-model="userEdit.fullname">
                            </label>
                            <label style="margin-top:20px;margin-left:30px;" for="">激活：
                                <input type="text" v-model="userEdit.is_active">
                            </label>

                            <div style="margin-top:70px;font-size:14px">
                            <span style="">创建时间：{{userEdit.created_time}}</span>
                            <span style="margin-left:140px;">上次修改时间：{{userEdit.modify_time}}</span>
                            <span style="margin-left:140px;">用户类型：{{userEdit.type}}</span>
                            </div>
                            
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="角色">
                        <div class="role" style="height:260px;overflow:scroll">

                            <el-checkbox-group v-model="usercheckList">
                                <el-checkbox :label="list.id" v-for="(list, index) in userEdit.all_role_set" :key="index" >{{list.name}}</el-checkbox>
                            </el-checkbox-group>
                            
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="操作记录">
                        <div class="record" style="height:300px;overflow:scroll">
                            <el-table
                                :data="tableData3"
                                height="100%"
                                border
                                style="width: 100%">
                                <el-table-column
                                prop="date"
                                label="时间"
                                width="180">
                                </el-table-column>
                                <el-table-column
                                prop="name"
                                label="IP"
                                width="180">
                                </el-table-column>
                                <el-table-column
                                prop="address"
                                label="操作">
                                </el-table-column>
                            </el-table>
                        </div>
                    </el-collapse-item>
                </el-collapse>
                <div class="userEditBtn">
                  <button @click="submitEdit(userEdit.id)">确认</button>
                  <button @click="show=false">取消</button>
                  <button @click="delUser(userEdit.id)">删除</button>
                </div>
            </div>


            <div id="datatwo" class="datatwo">
                <el-collapse v-model="activeNames">
                    <el-collapse-item style="" title="基本资料">
                        <div style="height:155px;" class="data">
                            <label style="float:left;" for="">帐号：
                                <input type="text">
                            </label>
                            <label style="float:left;margin-left:65px;width:500px;" for="">使用者：
                                <input type="text">
                            </label>
                            <label style="float:left;margin-top:20px;" for="">电话：
                                <input type="text">
                            </label>
                            <label style="float:left;margin:20px 0 0 68px;" for="">E-mail:
                                <input type="text">
                            </label>
                            <span style="float:left;margin:20px 0 0 0;">注册时间：2017-09-12 00：00：00</span>
                            <span style="float:left;margin:20px 0 0 170px;">上次访问IP：192.168.250.150</span>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="角色">
                        <div class="role">
                            <button style="float:left;background:white;color:#E54C87;border:1px solid #E54C87;">增加角色</button>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item style="" title="操作">
                        <div class="operation-nav">
                            <span>确定</span>
                            <span>取消</span> 
                        </div>
                    </el-collapse-item>
                </el-collapse>
            </div>


            <!--
            <div id="optional" class="optional">
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
                    <strong>取消</strong>
                </div>
            </div>
            -->
              
        </div>

        <!-- 列表 -->
        <div class="class-z">
            <div style="margin-left:20px;">
            <el-checkbox v-model="usersCheckList">ID</el-checkbox>
            <span style="width: 15%;display:inline-block;text-align:right">邮箱</span>
            <span style="width: 15%;display:inline-block;text-align:right">是否激活</span>
            <span style="width: 18%;display:inline-block;text-align:right">用户类型</span>
            <span style="width: 20%;display:inline-block;text-align:right">创建时间</span>
            <span style="float:right;display:inline-block;margin-right:60px;">操作</span>
            </div>
        </div>
        <ul style="float:left;width:100%;">
            <el-checkbox-group v-model="usersCheckList">
            <li style="float:left;width:100%;height:52px;border-bottom:1px solid #E5E5E5;" v-for="(user, index) in users" :key="index">
                <el-checkbox style="width: 4%;display:inline-block;text-align:right;line-height:52px" :label="user.id">
                    {{ user.id }}
                </el-checkbox>
                <span style="width: 18%;display:inline-block;text-align:right">{{ user.email }}</span>
                <span style="width: 10%;display:inline-block;text-align:right">{{ user.is_active }}</span>
                <span style="width: 18%;display:inline-block;text-align:right">{{ user.type }}</span>
                <span style="width: 22%;display:inline-block;text-align:right">{{ user.create_time }}</span>
                <span style="float:right;display:inline-block;margin-right:60px;line-height:52px;">
                  <a @click="show=true;edit(user.id)">  编辑 </a>
                </span>
            </li>
            </el-checkbox-group>
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
        show: false,
        checkList: ['',''],
        tableData3: [
            {
            date: '2017-09-12 00:00:00',
            name: '192.168.250.100',
            address: '上传了一件商品就是这么简单啦啦啦啦啦啦啦啦啦'
            }, {
            date: '2017-09-12 00:00:00',
            name: '192.168.250.100',
            address: '上传了一件商品就是这么简单啦啦啦啦啦啦啦啦啦'
            }, {
            date: '2017-09-12 00:00:00',
            name: '192.168.250.100',
            address: '上传了一件商品就是这么简单啦啦啦啦啦啦啦啦啦'
            },
        ],
        activeNames: ['1'],
        currentPage: 1,
        search: '',
        users: [],
        usersCheckList: [],
        userEdit: {},
        usercheckList: [],
        filterCheckList: [],
        filtershow: false,
        filterList:[],
        totalpage:null
      }
    },
    methods: {
      dataloading: function () {
        var self = this
        var str = self.filterCheckList.join(',')
        axios.get('/account/user?bg=1&num=50&page=' + self.currentPage + '&r='+ str + '&search=' + self.search)
          .then(function (res) {
              console.log(res)
              self.users = res.data.object_list
              self.totalpage = res.data.page.count
          })
          .catch(function (err) {
              console.log(err)
          })
      },
      handleCurrentChange(val) {
        this.dataloading()
      },
      handleIconClick() {
        this.dataloading()
      },
      edit: function (id) {
          var self = this
          axios.get('/account/user/' + id + '?bg=1')
            .then(function (res) {
                console.log(res)
                self.userEdit = res.data
                for (var i = 0; i < res.data.role_set.length;i ++) {
                    self.usercheckList.push(res.data.role_set[i].id)
                }
            })
      },
      submitEdit: function (id) {
          var self = this
          axios.put('/account/user/' + id, {
              birthday: self.userEdit.birthday,
              phone_num: self.userEdit.phone_num,
              locale: self.userEdit.locale,
              fullname: self.userEdit.fullname,
              email: self.userEdit.email,
              is_active: self.userEdit.is_active,
              role_id: self.usercheckList
          })
            .then(function (res) {
                if (res.data.success) {
                alert('提交成功')
                self.show = false
                self.dataloading()
              } else {
                  if (res.data.message) {
                      alert('邮箱已存在')
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
      delUser: function (id) {
        var self = this
        var r = confirm('是否删除用户？')
        if (r) {
        axios.delete('/account/user/' + id)
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
      },
      //角色删选
      filter: function () {
          var self = this
          axios.get('/account/role?page=all')
            .then(function (res) {
                console.log(res)
                self.filterList = res.data.object_list
            })
      },
      submitFilter: function () {
          var self = this
          var str = self.filterCheckList.join(',')
          axios.get('account/user?num=2&r=' + str)
            .then(function (res) {
                self.dataloading()
                self.filtershow = false
            })
      },
      quxiao: function () {
          var div33 = document.getElementById("optional")
          var div1 = document.getElementById("mask")
          div33.style.display="none"
          div1.style.display="none"
      },
    },
    created: function() {
        this.dataloading()
    }
  }
</script>

<style scoped>
.username {
    min-width:1366px;
    width: 100%;
    height: 100%;
    background: #fafafa;
    position: relative;
}
.user-main {
    height: 32px;
    padding: 30px 20px;
}
.user-main .el-input {
    width: 330px;
    height: 36px;
    border-radius: 0; 
}
.username .el-input__inner {
    border-radius: 0;
}
.user-main label {
    margin-left: 20px;
}
.user-main button {
    width: 90px;
    height: 30px;
    border: 0;
    outline: 0;
    color: white;
    background: #E54C87;
    cursor: pointer;
}
.class-z {
    height: 24px;
    padding-top: 10px;
    border-top: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
    background: #F6F6F6;
}

 /* 底部 */
.positioning {
    position: fixed;
    right: 0;
    height: 32px;
    bottom: 0;
    background: #E3E3E3;
}
.el-pagination .btn-next, .el-pagination .btn-prev {
    background: #E3E3E3;
}
.el-pager li {
    background: #E3E3E3;
}

.username .increase {
    position: absolute;
    float: left;
    width: 1000px;
    top: 60px;
    left: 340px;
    z-index: 1000;
    background: #fafafa;
}
.username .mask{ 
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
.username .ment {
    height: 34px;
    background: #F6F6F6;
}

.user-main .data {
    width: 100%;
    padding: 30px 0 0 20px;
}
.user-main .data span {
    color: #4C4C4C;
}
.username .datatwo .role {
    height: 453px;
    padding: 29px 0 0 117px;
}
.username .increase .role {
    padding: 39px 0 0 100px;
}
.user-main .role .el-checkbox {
    font-size: 16px;
    display: inline-block;
    line-height: 32px;
    margin: 0 30px 30px 0;
    cursor: pointer;
    text-align: center;
}

.user-main .record {
    height: 231px;
    padding: 21px 120px 0 116px;
}

.user-main .datatwo {
    position: fixed;
    display: none;
    width: 1000px;
    top: 100px;
    left: 600px;
    height: 792px;
    z-index: 1000;
    background: #fafafa;
}
.username .datatwo input {
    width: 269px;
    height: 28px;
}
.username .operation-nav {
    width: 200px;

}

.username .screent {
    position: absolute;
    top: 0;
    width: 100%;
    margin-left: -20px;
    z-index: 1000;
    background: #FAFAFA;
}
.username .screent .el-checkbox-group {
    margin-top: 40px;
}
.username .bottom {
    position: relative;
    width: 400px;
    margin:50px auto;
}
.username .bottom button {
    display: inline-block;
    width: 70px;
    height: 30px;
    color: #4C4C4C;
    line-height: 30px;
    text-align: center;
}
.username .bottom button  {
    color: white;
    margin-right: 20px;
    background: #E54C87;
}
.username .xuanze {
    float: left;
    width: 100%;
    height: 178px;
    /* background: pink; */
}
.username .xuanze button {
    display: block;
    float: left;
    width: 60px;
    height: 30px;
    color: white;
    line-height: 30px;
    text-align: center;
    margin-left: 743px;
    margin-top: 102px;
    background: #E54C87;
    
}

.username a:hover{
    color: #E54C87;
    text-decoration:underline;
    cursor: pointer;
}
.userEditBtn {
    width: 300px;
    margin:  40px auto;
}

.userEditBtn button{
    width: 50px;
    height: 30px;
    border: 0;
    margin-right: 30px;
    color: white;
    outline: none;
    background: #E54C87;
    border-radius: 4px;   
}
.userEditBtn button:hover {
    border: 1px solid #fff;
}
.userEditBtn button:active {
    background: #fff;
    color: #E54C87;
}
.username .data input {
    width: 150px;
}
.username #shaixuan {
   /* float: left;
    margin-left: 20px;
    color: #747474;
    background: #fafafa;*/
    margin-left: 20px;
}
</style>