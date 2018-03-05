<template>
<!-- 分类管理 -->
    <div class="management">
        <!-- 头 --> 
        <div class="scred">
            <label style="margin-left:20px;color:#747474;" for="">分类搜索：
                <el-input
                    placeholder="分类名称"
                    icon="search"
                    v-model="search"
                    @keyup.enter.native="handleIconClick"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>
            <button @click="addshow = true">新增分类</button>
        </div>
        <!-- 标题头 -->
        <div class="class-z">
            <span style="display:block;float:left;text-align:right;margin-left:46px;">分类名称<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
            <span style="display:block;float:left;width:20.1%;text-align:right;">排序</span>
            <span style="display:block;float:left;width:15%;text-align:right;">创建时间<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
            <span style="display:block;float:left;width:18%;text-align:right;">商品数量<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
            <span style="display:block;float:left;width:15%;text-align:right;">当前状态<img style="margin-left:8px;" src="static/images/shang.png" alt=""><img src="static/images/xia.png" alt=""></span>
            <span style="display:block;float:left;width:8.5%;text-align:right;">操作</span>
        </div>
        <!-- 新增分类 -->
        <div v-if="addshow" class="fladd" style="padding:20px 20px 0 20px;height:120px;width:100%;background:#E5E5E5">
            <form>
            分类名称: <input type="text"  style="margin-right:40px;" placeholder="英文字母开头"  maxlength="60" v-model="add1">
            中文备注: <input type="text" maxlength="60" v-model="add2">
            </br>
            <button @click="addsubimt">确定</button>
            <a style="cursor: pointer;margin-left:30px;" @click="addshow = false">取消</a>
            </form>
        </div>
        
        <el-tree
        :data="data2"
        :props="defaultProps"
        show-checkbox
        node-key="id"
        default-expand-all
        :expand-on-click-node="false"
        :render-content="renderContent">
        </el-tree>

        <!-- 新增子分类 -->
        <div v-if="addshow2" class="fladd" style="padding:20px 20px 0 20px;height:120px;width:100%;background:#E5E5E5">
            <form>
            分类名称: <input type="text"  style="margin-right:40px;" placeholder="英文字母开头"  maxlength="64" v-model="add3">
            中文备注: <input type="text" maxlength="64" v-model="add4">
            </br>
            <button @click="addchildsubimt">确定</button>
            <a style="cursor: pointer;margin-left:30px;" @click="addshow2 = false">取消</a>
            </form>
        </div>

                    <!-- 弹出管理 -->
                    <div id="mask" class="mask" v-if="editshow"></div>
                    <!-- dasdsad     -->
                    <div id="increase" class="increase" v-if="editshow">
                        <el-collapse v-model="activeNames">
                            <el-collapse-item style="" title="基本资料">
                                <div class="data">
                                   英文名称<input style="margin-left:20px;" v-model="editlist.name"></input>
                                   中文备注<input style="margin-left:20px;" v-model="editlist.name_desc"></input>
                                </div>
                            </el-collapse-item>
                            <el-collapse-item style="" title="关联尺码">
                                <div class="roles">
                                    <span>上衣尺码</span>
                                </div>
                            </el-collapse-item>
                            <el-collapse-item style="" title="关联产品属性">
                                <div class="roles">
                                    <span>打死</span>
                                </div>
                            </el-collapse-item>
                            <el-collapse-item style="" title="洗衣技巧">
                                <div class="skill">
                                    <button>洗衣技巧</button>
                                </div>
                            </el-collapse-item>
                        </el-collapse>
                        <div class="operation">
                            <button @click="editsumbit(editlist.id)">提交</button>
                            <button @click="editshow = false">取消</button> 
                        </div>
                    </div>


        <!-- 底部 --> 
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
let id = 1000;
export default {
    data() {
      return {
        activeNames: ['1'],
        currentPage: 1,
        totalpage: null,
        checked: true,
        search: '',
        picys: [
            {
                cen: 'SWIMWEAR(_中文备注)',
                wer: 'SWIMWEAR(_中文备注)',
                come: 'aasdsadd',
            },
            
        ],


        data2: [/*{
          id: 1,
          name: '一级 1',
          time: 1,
          sub_category: [{
            id: 4,
            label: '二级 1-1',
            /*children: [{
              id: 9,
              label: '三级 1-1-1'
            }, {
              id: 10,
              label: '三级 1-1-2'
            }]
          }]
        }, {
          id: 2,
          label: '一级 2',
          children: [{
            id: 5,
            label: '二级 2-1'
          }, {
            id: 6,
            label: '二级 2-2'
          }]
        }, {
          id: 3,
          label: '一级 3',
          children: [{
            id: 7,
            label: '二级 3-1'
          }, {
            id: 8,
            label: '二级 3-2'
          }]
        } */],
        defaultProps: {
          children: 'sub_category',
          label: 'name'
        },
        addshow: false,
        add1: null,
        add2: null,
        addshow2: false,
        add3: null,
        add4: null,
        fatherid: null,
        editshow: false,
        editlist: {}
      }
    },
    methods: {
      dataloading : function () {
        var self = this
        axios.get('/category?bg=1&sort=order&num=50')
        .then(function (res) {
            self.totalpage = res.data.page.total_pages
            self.data2 = res.data.object_list
        })
        .catch(function (err) {
            alert(err)
        })
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      handleIconClick(ev) {
        var self = this
        axios.get('/category?bg=1&o=alpha&search=' + self.search)
            .then(function (res){
                console.log(res)
                self.data2 = res.data.object_list
                //self.designers = res.data.object_list
            })
      },


      addsubimt: function () {
        var self = this
        axios.post('/category', {
            name: self.add1,
            name_desc: self.add2
        })
        .then(function (res) {
            console.log(res)
            if (res.data.success) {
                alert('添加成功')
                self.add1 = ''
                self.add2 = ''
                self.dataloading()
                self.addshow = false
            } else {
                if (res.data.message == 'name exist') {
                    alert('名称已存在')
                    self.add1 = ''
                    self.add2 = ''
                } else {
                    alert('输入不合法')
                    self.add1 = ''
                    self.add2 = ''
                }
            }
        })
        .catch(function (err) {
            alert('err')
        })
      },

      addchildsubimt: function () {
        var self = this
        axios.post('/category/' + self.fatherid, {
            name: self.add3,
            name_desc: self.add4
        })
        .then(function (res) {
            if (res.data.success) {
                alert('添加成功')
                self.add3 = ''
                self.add4 = ''
                self.dataloading()
                self.addshow2 = false
            } else {
                if (res.data.message == 'name exist') {
                    alert('名称已存在')
                    self.add3 = ''
                    self.add4 = ''
                } else {
                    alert('输入不合法')
                    self.add1 = ''
                    self.add2 = ''
                }
            }
        })
        .catch(function (err) {
            alert('err')
        })
      },

      append(store, data) {
        //store.append({ id: id++, label: 'testtest', children: [] }, data);
        this.addshow2 = true
        this.fatherid = data.id
      },
      hidden(store, data) {
        var self = this
        axios.put('/category/' + data.id + '?action=active_swap')
            .then(function (res) {
                if (res.data.success) {
                    alert('更改成功')
                    self.dataloading()
                } else {
                    alert('未知错误')
                }
            })
            .catch(function (err) {
                alert(err)
            })
      },
      remove(store, data) {
        if (confirm('是否删除')) {
            //store.remove(data);
            var self = this
            axios.delete('/category/' + data.id)
                .then(function (res) {
                    if (res.data.success) {
                        alert('删除成功')
                    }
                    self.dataloading()
                })
                .catch(function (err) {
                    if (err.response.status === 404) {
                        alert('对象不存在')
                    } else if (err.response.status === 403) {
                        alert('没有权限')
                    }
                    self.dataloading()
            })
        }
        return
      },
      edit(store, data) {
        this.editshow = true
        var self = this
        axios.get('/category/' + data.id + '?bg=1')
          .then(function (res) {
              console.log(res)
              self.editlist = res.data
          })
          .catch(function (err) {
              alert(err)
          })
      },
      editsumbit: function (id) {
          var self = this
          axios.put('/category/' + id, self.editlist)
          .then(function (res) {
              if (res.data.success) {
                  alert('修改成功')
                  self.editshow = false
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
              if (err.response.status === 404) {
                    alert('对象不存在')
                    self.editshow = false
                    self.dataloading()
                }
            })
      },
      sort: function (store, data, sort) {
          var self = this
              axios.put('/category/' + data.id + '?action=order_swap', {
                  direction: sort
              })
              .then(function (res) {
                  if (res.data.success) {
                      self.dataloading()
                  }
              })
      },
      renderContent(h, { node, data, store }) {
        return (
          <span>
            <span style="display:inline-block;text-align:left;margin-left:20px;width:5%;">{node.label}({data.name_desc})</span>
            <span style="display:inline-block;width:18.8%;text-align:right;"><img style="margin-left:8px;" src="static/images/shang.png" alt="" on-click={ () => this.sort(store, data, 'up') }/><img src="static/images/xia.png" style="margin-left:8px;" alt="" on-click={ () => this.sort(store, data, 'down') }/></span>
            <span style="display:inline-block;width:16%;text-align:right;">{data.create_time}</span>
            <span style="display:inline-block;width:14%;text-align:right;">{data.product_count}</span>
            <span style="display:inline-block;width:16%;text-align:right;">{(data.is_active)? '使用中':'未激活'}</span>
            <span style="float: right; margin-right: 80px">
              <el-button size="mini" on-click={ () => this.append(store, data) }>添加子分类</el-button>
              <el-button size="mini" on-click={ () => this.edit(store, data) }>编辑</el-button>
              <el-button size="mini" on-click={ () => this.hidden(store, data) }>更改状态</el-button>
              <el-button size="mini" on-click={ () => this.remove(store, data) }>删除</el-button>
            </span> 
          </span>);
      }
    },

    created: function () {
        this.dataloading()
    }
  }
</script>

<style>
.management {
    float: left;
    width: 100%;
    height: 100%;
    background: #fafafa;
}
.management img {
    width: 13px;
    height: 14px;
    cursor:pointer;
}
.duppert li {    
    color: #4C4C4C;
    width: 100%;
    height: 145px;
}
.goin {
    float: right;
    margin-top: 20px;
    margin-right: 18px;
}
.goin button {
    margin-right: 5px;
    border: 0;
    cursor:pointer;
    outline:none;
    color: #4C4C4C;
    background: #fafafa;
}
.class-j button {
    margin-right: 5px;
    border: 0;
    cursor:pointer;
    outline:none;
    color: #4C4C4C;
    background: #F6F6F6;
}
.scred {
    width: 100%;
    height: 32px;
    padding: 30px 0;
}
.scred .el-input {
    width: 330px;
    height: 36px;
    border-radius: 0; 
}
.el-input__inner {
    border-radius: 0;
}
.scred button {
    float: right;
    width: 90px;
    height: 30px;
    margin: 20px 61px 0 0;
    border: 0;
    outline: 0;
    color: white;
    background: #E54C87;
}
.class-z {
    height: 24px;
    padding-top: 10px;
    border-top: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
    background: #F6F6F6;
}
.management  .el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.management  .el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.management  .el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.management  .el-checkbox__inner::after {
  left: 2px;
  top: -1px;
  border-color: #e54c87;
}
.el-checkbox__label {
    margin-left: 20px;
}
.el-checkbox {
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
.positioning .el-pagination__total {
  display: none;
}
.management .mask{ 
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
.management .increase {
    position: absolute;
    float: left;
    left: 600px;
    top: 100px;
    width: 1000px;
    z-index: 1000;
    background: #FAFAFA;
}
.management .roles span {
    padding: 4px;
    border: 0;
    outline: none;
    background: white;
    margin-left: 118px;
    border: 1px solid #999899;
}
.management .el-collapse-item__header {
    padding-left: 0;
}
.management .record button {
    width: 105px;
    height: 32px;
    border: 0;
    outline: none;
    background: white;
    margin-left: 118px;
    border: 1px solid #999899;
}
.management .skill button {
    width: 105px;
    height: 32px;
    border: 0;
    outline: none;
    background: white;
    margin-left: 118px;
    border: 1px solid #999899;
}
.pximg {
    display: inline-block;
    width: 19px;
    height: 19px;
}
.fladd button {
    margin:40px 20px 0 160px;
    width: 60px;
    height: 30px;
    border: 0;
    outline: 0;
    color: white;
    background: #E54C87;
    cursor: pointer;
}
.management button {
    cursor: pointer;
}
.operation {
    position: relative;
    bottom: 20px;
    width: 100%;
    text-align: center;
}
.operation button {
    margin:40px 20px 0 20px;
    width: 60px;
    height: 30px;
    border: 0;
    outline: 0;
    color: white;
    background: #E54C87;
    cursor: pointer;
}
.el-tree-node__children {
    padding-left: 20px;
}
</style>
