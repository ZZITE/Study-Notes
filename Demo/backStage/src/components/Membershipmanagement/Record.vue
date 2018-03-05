<template>
<!-- 会员记录管理 -->
    <div class="Record">
        <div class="Record-main">
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
        <div class="Record-ment">
            <button style="width:100px;height:32px;background:#d15b47;border:0;color:white;margin:5px 0 0 20px;outline: none;border-radius:5%;">批量删除</button>
            <p style="float:right;margin:30px 0 0 0;">共：<em style="font-weight:bold;">2345条</em></p>
        </div>
        <label style="float:right;margin:0 15px 20px 0;" for="">
            搜索：<input type="text">
        </label>
        <template>
            <el-table :data="tableData3" height="600" border style="width:1630px;margin-left:15px;">
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column prop="id" label="用户ID" sortable width="105">
                </el-table-column>
                <el-table-column prop="name" label="用户名" width="200">
                </el-table-column>
                <el-table-column prop="integral" label="积分" width="170">
                </el-table-column>
                <el-table-column prop="browse" label="浏览(条)" sortable width="210">
                </el-table-column>
                <el-table-column prop="buy" label="购物(比)" sortable width="210">
                </el-table-column>
                <el-table-column label="操作" width="660">
                <template scope="scope">
                    <el-button
                    size="small"
                    type="warning"
                    @click="handlety(scope.$index, scope.row)">停用</el-button>
                    <el-button
                    size="small"
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
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },
                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
                },                {
                    id: '1',
                    name: '王小虎',
                    browse: '71',
                    buy: '34',
                    integral: '146',
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
.Record {
    float: left;
    width: 100%;
    height: 948px;
    /* background: #E5E5E5; */
}
.Record-main {
    width: 1600px;
    height: 40px;
    padding: 15px;
    margin: 20px auto;
}
.Record-ment {
    width: 1600px;
    height: 40px;
    padding: 15px;
    margin: 20px auto;
    border: 1px solid #E5E5E5;
}
.Record .el-input__icon+.el-input__inner {
    border-radius: 0;
}
.el-table th>.cell {
    text-align: center;
}
.el-table .cell {
    text-align: center;
}
</style>