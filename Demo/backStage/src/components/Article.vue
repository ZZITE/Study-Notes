<template>
<!-- 文章管理 -->
    <div class="Article">
        <div class="Article-main">
            <input type="text" placeholder="请输入关键字">
            <button style="display: inline-block;height: 38px;line-height: 38px;padding: 0 18px;background-color: #009688;color: #fff;white-space: nowrap;text-align: center;font-size: 14px;
            border: none;border-radius: 2px;cursor: pointer;outline: none;margin:0 0 0 10px;">查询</button>
            <button style="display: inline-block;height: 38px;line-height: 38px;padding: 0 18px;background-color: #1E9FFF;color: #fff;white-space: nowrap;text-align: center;font-size: 14px;
            border: none;border-radius: 2px;cursor: pointer;opacity: .9;">添加文章</button>
            <button style="display: inline-block;height: 38px;line-height: 38px;padding: 0 18px;background-color: #5FB878;color: #fff;white-space: nowrap;text-align: center;font-size: 14px;
            border: none;border-radius: 2px;cursor: pointer;opacity: .9;">推荐文章</button>
            <button style="display: inline-block;height: 38px;line-height: 38px;padding: 0 18px;background-color: #009688;color: #fff;white-space: nowrap;text-align: center;font-size: 14px;
            border: none;border-radius: 2px;cursor: pointer;opacity: .9;">审核文章</button>
            <button style="display: inline-block;height: 38px;line-height: 38px;padding: 0 18px;background-color: #FF5722;color: #fff;white-space: nowrap;text-align: center;font-size: 14px;
            border: none;border-radius: 2px;cursor: pointer;opacity: .9;">批量删除</button>
        </div>
        <template>
            <el-table :data="tableData3" height="760" border style="width:1630px;margin-left:15px;">
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column prop="title" label="文章标题" width="600">
                </el-table-column>
                <el-table-column prop="name" label="作者" width="150">
                </el-table-column>
                <el-table-column prop="state" label="审核状态" width="150">
                </el-table-column>
                <el-table-column prop="Jurisdiction" label="浏览权限" width="150">
                </el-table-column>
                <el-table-column prop="date" label="日期" width="180">
                </el-table-column>
                <el-table-column label="操作" width="325">
                <template scope="scope">
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
            tableData3: [
                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },
                                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
                    date: '2014-6-11 11:11:42',
                },                {
                    title: '6999元！华硕联手腾讯发布首款智能机器人：史上最贴心家庭助手',
                    name: '王小虎',
                    state: '审核通过',
                    Jurisdiction: '开放浏览',
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
        }
    }
}
</script>

<style>
.Article {
    float: left;
    width: 100%;
    height: 948px;
    /* background: #E5E5E5; */
}
.Article-main {
    width: 1600px;
    height: 40px;
    padding: 15px;
    margin: 20px auto;
    background: #f2f2f2;
}
.Article-main input {
    float: left;
    width: 182px;
    height: 34px;
}
.Article .el-checkbox__inner {
    border-radius: 0;
}
</style>
