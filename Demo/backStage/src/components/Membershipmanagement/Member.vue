<template>
<!-- 会员列表 -->
    <div class="Member">
        <div class="Member-main">
            <label style="float:left;margin:0 20px 0 0;" for="">会员名称
                <input style="width: 400px;height: 28px;" type="text" placeholder="输入会员名称、电话、邮箱">
            </label>
            <div style="float:left;" class="block">
                <span class="demonstration">添加时间</span>
                <el-date-picker
                v-model="value2"
                align="right"
                type="date"
                placeholder="选择日期"
                :picker-options="pickerOptions1">
                </el-date-picker>
            </div>
            <button style="width:68px;height:32px;background: #2a8bcc;border:0;color:white;margin:5px 0 0 20px;outline: none;">查询</button>
        </div>
        <div class="Member-ment">
            <button style="width:100px;height:32px;background:#e59729;border:0;color:white;margin:5px 0 0 20px;outline: none;border-radius:5%;">+添加用户</button>
            <button style="width:100px;height:32px;background:#d15b47;border:0;color:white;margin:5px 0 0 20px;outline: none;border-radius:5%;">批量删除</button>
            <p style="float:right;margin:30px 0 0 0;">共：<em style="font-weight:bold;">2345条</em></p>
        </div>
        <template>
            <el-table :data="tableData3" height="600" border style="width:1630px;margin-left:15px;">
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column prop="id" label="ID" sortable width="80">
                </el-table-column>
                <el-table-column prop="name" label="用户名" sortable width="100">
                </el-table-column>
                <el-table-column prop="Gender" label="性别" width="70">
                </el-table-column>
                <el-table-column prop="telp" label="手机" width="130">
                </el-table-column>
                <el-table-column prop="email" label="邮箱" width="180">
                </el-table-column>
                <el-table-column prop="address" label="地址" width="400">
                </el-table-column>
                <el-table-column prop="date" label="加入时间" sortable width="170">
                </el-table-column>
                <el-table-column prop="Grade" label="等级" width="100">
                </el-table-column>
                <el-table-column prop="state" label="状态" width="80">
                </el-table-column>
                <el-table-column label="操作" width="245">
                <template scope="scope">
                    <el-button
                    size="small"
                    type="warning"
                    @click="handlety(scope.$index, scope.row)">停用</el-button>
                    <el-button
                    size="small"
                    type="info"
                    @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button
                    size="small"
                    type="danger"
                    @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
                </el-table-column>
            </el-table>
        </template>
        <div style="float:right;margin:20px 10px 0 0;" class="block">
            <el-pagination
                layout="prev, pager, next"
                :total="1000">
            </el-pagination>
        </div>
    </div>
</template>

<script>
export default {
data() {
    return {
        pickerOptions1: {
            shortcuts: [{
            text: '今天',
            onClick(picker) {
                picker.$emit('pick', new Date());
            }
            }, {
            text: '昨天',
            onClick(picker) {
                const date = new Date();
                date.setTime(date.getTime() - 3600 * 1000 * 24);
                picker.$emit('pick', date);
            }
            }, {
            text: '一周前',
            onClick(picker) {
                const date = new Date();
                date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
                picker.$emit('pick', date);
            }
            }]
        },
        value2: '',
        tableData3: [
                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },
                                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },                {
                    id: '1',
                    address: '福建省厦门市思明区海域思明区谊爱路8号之2号',
                    name: '王小虎',
                    Gender: '男',
                    telp: '13801457635',
                    email: '123456789@qq.com',
                    Grade: '钻石会员',
                    state: '已启用',
                    date: '2014-6-11 11:11:42',
                },
            ]
        }
    },
    methods: {
        handleEdit(index, row) {
            console.log(index, row);
        },
        handleDelete(index, row) {
            console.log(index, row);
        },
        handlety(index, row) {
            console.log(index, row);
        }
    }
};
</script>

<style>
.Member {
    float: left;
    width: 100%;
    height: 948px;
    /* background: #E5E5E5; */
}
.Member-main {
    width: 1600px;
    height: 40px;
    padding: 15px;
    margin: 20px auto;
}
.Member-ment {
    width: 1600px;
    height: 40px;
    padding: 15px;
    margin: 20px auto;
    border: 1px solid #E5E5E5;
}
.Member .el-input__icon+.el-input__inner {
    border-radius: 0;
}
</style>
