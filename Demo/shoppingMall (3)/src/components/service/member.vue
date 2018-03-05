<template>
<!-- 会员介绍 -->
    <div class="Member">
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column prop="date" label="特权 / 等级" width="110">
            </el-table-column>
            <el-table-column prop="register" label="注册会员(积分0-50)" width="150">
            </el-table-column>
            <el-table-column prop="Bronze" label="铜牌会员(积分51-500)" width="170">
            </el-table-column>
            <el-table-column prop="silver" label="银牌会员(积分501-5000)" width="180">
            </el-table-column>
            <el-table-column prop="gold" label="金牌会员(积分5001-5万)" width="180">
            </el-table-column>
            <el-table-column prop="Diamonds" label="钻石会员(积分5万以上)" width="180">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tableData: [
                {
                    date: '专属勋章',
                    register: '无',
                    Bronze: '有',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有' 
                },
                {
                    date: 'Cps推广返利',
                    register: '无',
                    Bronze: '有',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有' 
                },
                {
                    date: '专属产品',
                    register: '无',
                    Bronze: '有',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有' 
                },
                {
                    date: '专属活动',
                    register: '无',
                    Bronze: '有',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有' 
                },
                {
                    date: '专属折扣',
                    register: '无',
                    Bronze: '有',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有' 
                },
                {
                    date: '三级cps返利',
                    register: '无',
                    Bronze: '无',
                    silver: '有',
                    gold: '有',
                    Diamonds: '有'
                },
                {
                    date: 'C2B发起',
                    register: '无',
                    Bronze: '无',
                    silver: '无',
                    gold: '有',
                    Diamonds: '有'
                },
                {
                    date: '物流特权',
                    register: '无',
                    Bronze: '无',
                    silver: '无',
                    gold: '无',
                    Diamonds: '有'
                },
                {
                    date: '专属客服',
                    register: '无',
                    Bronze: '无',
                    silver: '无',
                    gold: '无',
                    Diamonds: '有'
                }
            ]
        }
    }
}
</script>

<style>
.Member .el-table .cell, .el-table th>div {
    /* width: 150px; */
    padding-right: 0;
}
</style>
