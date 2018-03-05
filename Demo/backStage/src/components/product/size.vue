<template>
<!-- 尺码管理 -->
    <div class="size">
        <div class="size-header">
            <!-- 头 -->
            <label style="float:left;margin-left:20px;" for="">尺码搜索：
                <el-input
                    placeholder="输入尺码名称"
                    icon="search"
                    v-model="search"
                    @keyup.enter.native="handleIconClick"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>

            <button style="float:right;margin-top:50px;margin-right:30px;cursor: pointer;;" @click="addshow=true;addsize()">新增尺码</button>
        </div>
     
        <div class="de-section" style="" v-for="(item, index) in size" :key="index">
        <!-- 显示主体 -->
          <h2>{{item.initial}}</h2>
          <div class="de-name">
            <ul style="float:left;height:100%;overflow:hidden;">
              <li style="float:left;" v-for="(i, index) in item.item" :key="index">
                <a  class="de-a" @click="edit(i.id);addshow = true">   
                    {{ i.name }}({{i.name_desc}})
                </a>
              </li>
            </ul>
          </div>
      </div>

              <!-- 弹窗 -->

            <div id="mask" v-if="addshow" class="mask"></div>

              <div class="spender" v-if="addshow">
                <el-collapse>
                    <el-collapse-item title="基本资料" name="1">
                        <div class="data" style="margin-top:20px;font-size:14px">
                            名称<input style="margin-left:20px;margin-right:20px" v-model="addsizename"></input>
                            名称描述<input style="margin-left:20px" v-model="addname_desc"></input>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item title="尺码表格" name="2">
                      <div style="width:100%;padding:20px 0 0 8px;">
                        <!-- 表格 -->
                        <div style="width:600px;margin:0 0 0 90px;" class="table">
                            <div style="float:right;margin-right:30px;margin-top:20px;">
                                <button @click="add2" style="width:20px;height:70px;">添加列</button>
                            </div>
                            <table border=1 width=250 align=center style="height:200;overflow:scroll;">
                            <caption @click="tt">表格</caption>
                            <tr bgcolor="#F6F6F6">
                                <!-- 表头 -->
                                <th v-for="(head, index) in tableData.th" :key="index" @click="inputshow = index;tableData.th[index] = '';">
                                <p v-if="inputshow !== index">{{head}}</p>
                                <input type="text" v-model="tableData.th[index]" v-if="inputshow == index" @blur="inputshow = -1">
                                </th>
                            </tr>
                                <!-- 表格内容 -->
                            <tr v-for="(i, todo) in tableData.tbody" :key="todo" align=center>
                                <td v-for="(j, index) in i.context" :key="index" @click="inputshow2 = index;inputshow3 = todo;tableData.tbody[todo].context[index] =''">
                                <p v-if="inputshow2 !== index || inputshow3 !== todo">{{j}}</p>
                                <input type="text" v-model="tableData.tbody[todo].context[index]" v-if="inputshow2 == index && inputshow3 == todo" @blur="inputshow2 = -1;inputshow3 = -1">
                                </td>
                            </tr>

                            </table>
                            
                            <div style="vertical-align: middle;">
                                <button @click="add" style="margin:20px auto; width:70px;height:20px">添加行</button>
                            </div>
                            <label style="margin-left:25px;" for="">单位：
                                <input type="text" v-model="tableData.company">
                            </label>
                            </div>

                      </div>
                    </el-collapse-item>
                    <el-collapse-item title="可用分类" name="3">

                        <el-tree
                        :data="data2"
                        show-checkbox
                        :default-checked-keys="addsizeid"
                        node-key="id"
                        ref="tree"
                        highlight-current
                        :props="defaultProps">
                        </el-tree>

                    </el-collapse-item>
                </el-collapse>

                <div class="sizeBtn" style="width:100%;text-align:center;margin:20px 0 20px -30px;">
                    <button @click="addsubmit" v-if="!sizeid">提交</button>
                    <button @click="editsubmit" v-if="sizeid">确定</button>
                    <button @click="closebtn">取消</button>
                    <button @click="delSize">删除</button>
                </div>
              </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            // 表格数据
            thshow: true,
            inputshow: -1,
            inputshow2: -1,
            inputshow3: -1,
            tableData: {
                th: ['名称/尺寸'],
                tbody: [
                ],
                company: ''
            },
            // 分类选择
            data2: [],
            defaultProps: {
                children: 'sub_category',
                label: 'name'
            },
            search: '',
            size: {
            },
            addshow: false,
            addsizename: '',
            addname_desc: '',
            addsizeid: [],
            sizeid: null
        }
    },
    methods: {
        dataloading: function () {
            var self = this
            axios.get('/size-standard?bg=1&page=all&o=alpha')
            .then(function (res) {
                self.size = res.data.object_list
            })
            .catch(function (err) {
                alert(err)
            })
        },
        handleIconClick() {
            var self = this
            axios.get('/size-standard?bg=1&o=alpha&search=' + self.search)
                .then(function (res){
                    console.log(res)
                    self.size = res.data.object_list
                })
        },
        getCheckedKeys() {
            this.addsizeid = this.$refs.tree.getCheckedKeys()
        },
        //表格
        add: function () {
            var cc = []
            cc.length = this.tableData.th.length
            for (var i = 0; i < cc.length; i++) {
                cc[i] = '默认'
            }
            this.tableData.tbody.push({
                context: cc
            })
        },
        add2: function () {
            this.tableData.th.push('默认')
            for (var i = 0; i < this.tableData.tbody.length; i ++) {
                this.tableData.tbody[i].context.push('默认')
            }
        },
        tt: function () {
            console.log(this.tableData)
        },
        //添加size
        addsize: function () {
            var self = this
            axios.get('/category?bg=1&sort=order&page=all')
            .then(function (res) {
                self.data2 = res.data.object_list
            })
            .catch(function (err) {
                alert(err)
            })
        },
        addsubmit: function () {
            var self = this
            self.addsizeid = self.$refs.tree.getCheckedKeys()
            axios.post('/size-standard', {
                name: self.addsizename,
                name_desc: self.addname_desc,
                size_json: JSON.stringify(self.tableData),
                category_ids: self.addsizeid
            })
                .then(function (res) {
                    if (res.data.success) {
                        alert('提交成功')
                        self.addshow = false
                        self.addsizename = ''
                        self.addname_desc = ''
                        self.tableData = {
                            th: ['名称/尺寸'],
                            tbody: [
                            ],
                            company: ''
                        }
                        self.addsizeid = []
                        self.dataloading()
                    } else {
                        if (res.data.message == 'name exist') {
                            alert('尺码名字已存在，不允许重复')
                        } else {
                            alert('输入非法')
                        }
                    }
                })
                .catch(function (err) {
                    alert(err)
                })
        },
        edit: function (id) {
            var self = this
            axios.get('/size-standard/' + id + '?bg=1')
                .then(function (res) {
                    self.sizeid = res.data.id
                    self.addsizename = res.data.name
                    self.addname_desc = res.data.name_desc
                    self.addsizeid = res.data.category_ids
                    self.tableData = JSON.parse(res.data.size_json)
                    self.addsize()
                })
                .catch(function (err) {
                    if (err.response.status === 404) {
                        alert('对象不存在')
                    }
                    self.addshow = false
                    self.dataloading()
                })
            },
            editsubmit: function () {
                var self = this
                self.addsizeid = self.$refs.tree.getCheckedKeys()                
                axios.put('/size-standard/' + self.sizeid, {
                    name: self.addsizename,
                    name_desc: self.addname_desc,
                    size_json: JSON.stringify(self.tableData),
                    category_ids: self.addsizeid
                })
                .then(function (res) {
                    console.log(res)
                    if (res.data.success) {
                        alert('提交成功')
                        self.addsizename = ''
                        self.addname_desc = ''
                        self.tableData = {
                            th: ['名称/尺寸'],
                            tbody: [
                            ],
                            company: ''
                        }
                        self.addsizeid = []
                        self.sizeid = null
                        self.addshow = false
                        self.dataloading()
                    } else {
                        if (res.data.message == 'name exist') {
                            alert('尺码名字已存在，不允许重复')
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


        delSize: function () {
            var self = this
            var r = confirm('是否删除尺码？')
            if (r) {
            axios.delete('/size-standard/' + self.sizeid)
                .then(function (res) {
                    if (res.data.success) {
                        alert('删除成功')
                    }
                    self.addshow = false
                    self.dataloading()
                })
                .catch(function (err) {
                    if (err.response.status === 404) {
                        alert('对象不存在')
                    } else if (err.response.status === 403) {
                        alert('没有权限')
                    }
                    self.addshow = false
                    self.dataloading()
                })
            } else {
                return;
            }
        },
        closebtn: function () {
            this.sizeid = null
            this.addsizename = ''
            this.addname_desc = ''
            this.tableData = {
                th: ['名称/尺寸'],
                tbody: [],
                company: ''
            }
            this.addsizeid = []
            this.addshow = false
        }

    },
    created: function () {
        this.dataloading()
    }
}
</script>

<style>
.size {
    width: 100%;
    background: #fafafa;
}
.size-header {
  width: 100%;
  padding: 30px 0 0 0px;
  background: #fafafa;
}
.size-header .el-input__icon+.el-input__inner {
  width: 330px;
  height: 32px;
  border-radius: 0;
}
.size-header .el-input__icon {
  right: 20px;
}
.size-header .el-input {
  width: 330px;
  height: 32px;
  margin-left: 20px;
}
.size-header button {
    width: 90px;
    height: 30px;
    background: #E54C87;
    border: 0;
    color: white;
    outline:none;
}
.size h2 {
    height: 26px;
    margin-left: 20px;
    border-bottom: 1px solid #E5E5E5; 
}
.size .de-section {
  width: 100%;
  float: left;
}
.size .de-name {
  width: 100%;
}
.size .de-a:hover{
  color:#E54C87;
  text-decoration: underline;
}
.size .de-a {
  float: left;
  width: 100%;
  display: block;
  font-size: 14px;
  color: #595959;
  margin-left: 39px;
  margin-top: 10px;
  margin-bottom: 10px; 
}
.size .de-content::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}

.size .spender {
    position: absolute;
    width: 1000px;
    left: 500px;
    top: 80px;
    z-index: 1000;
    background: white;
}
.size .mask{ 
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
.size .spender .el-collapse-item__header {
    background: #F6F6F6;
}
.size .bjsize .el-collapse-item__header {
    background: #F6F6F6;
}
.size .bjfenlei .el-collapse-item__header {
    background: #F6F6F6;
}
.spender .el-collapse-item__header {
    padding-left: 96px;
}
.size .spender .data {
    padding: 0 0 30px 117px;
}
.size .spender .el-collapse-item__header {
    margin: 0;
}

.size .el-input__inner {
    border-radius: 0;
}

.sizeBtn button{
    width: 50px;
    height: 30px;
    margin-left: 30px;
    border: 0;
    color: white;
    outline: none;
    background: #E54C87;
    border-radius: 4px;
    cursor: pointer;  
}
.sizeBtn button:hover {
    border: 1px solid #fff;
}
.sizeBtn button:active {
    background: #fff;
    color: #E54C87;
}
.size a{
    cursor: pointer;
}
/*表格*/
.table table {
  border-collapse:collapse;
  width: 500px;
  height: 100%;
}
.table caption, th {
  text-align: center;
}
.table td,th{
  width: 100px;
  height: 40px;
}
.table input {
  width: 48px;
  height: 20px;
}
.table td:first-child {
  background: #F6F6F6;
}
.table button {
  display:block;
  border: 1px solid #E54C87;
  background:#fff;
  color:#E54C87;
}
.table button:focus {
  border: none;
}

.size .el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.size  .el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.size  .el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.size  .el-checkbox__inner::after {
  left: 2px;
  top: -1px;
  border-color: #e54c87;
}

</style>