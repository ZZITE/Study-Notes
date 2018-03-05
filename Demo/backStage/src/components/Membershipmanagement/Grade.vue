<template>
  <!-- 等级管理 -->
    <div class="Grade">
        <div class="Grade-sidebar">
            <h2 style="background:#62A8D1;height:40px;color:white;line-height:40px;text-align: center;font-size:16px;">会员等级</h2>
            <ul>
                <li style="float:left;color:black;" v-for="(ent,index) in ents" :key="index">
                    <span style="float:left;margin:10px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">全部：{{ ent.whole }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">普通会员：{{ ent.ordinary }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">铁牌会员：{{ ent.Ironcard }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">铜牌会员：{{ ent.Bronze }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">银牌会员：{{ ent.silver }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">金牌会员：{{ ent.gold }}</span>
                    <span style="float:left;margin:20px 0 0 20px;"><img style="float:left;margin:1px 15px 0 0;" src="static/images/quan.png" alt="">钻石会员：{{ ent.Diamonds }}</span>
                </li>
            </ul>
        </div>
        <div class="Grade-main">
            <h2 style="float:left;position:relative;left:-230px;top:10px;font-size:18px;">等级统计</h2>
        </div>
        <div style="float:left;position:relative;left:150px;top:0;" class="charts" >
            <div id="myChart" style="width:1000px;height:500px"></div>
        </div>
        <div class="Grade-nav">
            <h2 style="float:left;position:relative;left:-1230px;top:10px;font-size:18px;">全部会员等级列表</h2>
        </div>
        <label style="position:relative;top:500px;left:200px;" for="">
            搜索：<input type="text">
        </label>
        <template>
            <el-table :data="tableData3" height="300" border style="float:right;width:1390px;position:relative;top:70px;left:-10px;">
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
                    type="danger"
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
        <div style="float:right;position:relative;top:76px;" class="block">
            <el-pagination
                layout="prev, pager, next"
                :total="1000">
            </el-pagination>
        </div>
    </div>
</template>

<script>
import echarts from 'echarts'

export default {
    data() {
        return{
            ents: [
                { 
                    whole: '531',
                    ordinary: '5131',
                    Ironcard: '512',
                    Bronze: '514',
                    silver: '54525',
                    gold: '1512',
                    Diamonds: '1541'
                },
                
            ],
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
    mounted(options){
    let echarts = require('echarts/lib/echarts')// 引入基本模板，如果在项目中对体积要求比较苛刻，也可以只按需引入需要的模块(可以按需引入的模块列表见见本博客底部)
    // 例如：引入柱状图
    //require('echarts/lib/chart/bar');
    let chartBox=document.getElementsByClassName('charts')[0]
    let myChart=document.getElementById('myChart')
    function resizeCharts() {//为调整图标尺寸的方法
        myChart.style.width=chartBox.style.width+'px'
        myChart.style.height=chartBox.style.height+'px'
            }
        let mainChart = echarts.init(myChart)// 基于准备好的dom，初始化echarts实例
        var option = null;
        // 指定图表的配置项和数据
        option = {
            title: {
                text: '用户等级统计',
                subtext: '实时更新最新等级',
                left: 'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                // orient: 'vertical',
                // top: 'middle',
                bottom: 10,
                left: 'center',
                data: ['普通用户', '铁牌用户','铜牌用户','银牌用户','金牌用户','钻石用户']
            },
            series : [
                {
                    type: 'pie',
                    radius : '65%',
                    center: ['50%', '50%'],
                    selectedMode: 'single',
                    data:[
                        {
                            label: {
                                normal: {
                                    backgroundColor: '#eee',
                                    borderColor: '#777',
                                    borderWidth: 1,
                                    borderRadius: 4,
                                    rich: {
                                        title: {
                                            color: '#eee',
                                            align: 'center'
                                        },
                                        abg: {
                                            backgroundColor: '#333',
                                            width: '100%',
                                            align: 'right',
                                            height: 25,
                                            borderRadius: [4, 4, 0, 0]
                                        },
                                        Sunny: {
                                            height: 30,
                                            align: 'left',
                                            backgroundColor: {
                                                image: weatherIcons.Sunny
                                            }
                                        },
                                        Cloudy: {
                                            height: 30,
                                            align: 'left',
                                            backgroundColor: {
                                                image: weatherIcons.Cloudy
                                            }
                                        },
                                        Showers: {
                                            height: 30,
                                            align: 'left',
                                            backgroundColor: {
                                                image: weatherIcons.Showers
                                            }
                                        },
                                        weatherHead: {
                                            color: '#333',
                                            height: 24,
                                            align: 'left'
                                        },
                                        hr: {
                                            borderColor: '#777',
                                            width: '100%',
                                            borderWidth: 0.5,
                                            height: 0
                                        },
                                        value: {
                                            width: 20,
                                            padding: [0, 20, 0, 30],
                                            align: 'left'
                                        },
                                        valueHead: {
                                            color: '#333',
                                            width: 20,
                                            padding: [0, 20, 0, 30],
                                            align: 'center'
                                        },
                                        rate: {
                                            width: 40,
                                            align: 'right',
                                            padding: [0, 10, 0, 0]
                                        },
                                        rateHead: {
                                            color: '#333',
                                            width: 40,
                                            align: 'center',
                                            padding: [0, 10, 0, 0]
                                        }
                                    }
                                }
                            }
                        },
                        {value:535, name: '普通用户'},
                        {value:510, name: '铁牌用户'},
                        {value:634, name: '铜牌用户'},
                        {value:735, name: '银牌用户'},
                        {value:635, name: '金牌用户'},
                        {value:635, name: '钻石用户'},
                        
                    ],
                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        if (option && typeof option === "object") {
            mainChart.setOption(option, true)
        }
    }
}
var weatherIcons = {
    'Sunny': './data/asset/img/weather/sunny_128.png',
    'Cloudy': './data/asset/img/weather/cloudy_128.png',
    'Showers': './data/asset/img/weather/showers_128.png'
};
</script>

<style>
.Grade {
    float: left;
    width: 100%;
    height: 948px;
    /* background: #E5E5E5; */
}
.Grade-sidebar {
    float: left;
    width: 250px;
    height: 948px;
    border-right: 1px solid #E5E5E5;
}
.Grade-sidebar span:hover {
    color:pink;
    cursor: pointer;
    text-decoration:underline
}
.Grade-main {
    position: relative;
    width: 1409px;
    height: 40px;
    top: 0;
    left: 251px;
    background: #dddddd;
}
.Grade-nav {
    position: relative;
    /* float: left; */
    width: 1409px;
    height: 40px;
    left: 250px;
    top: 490px;
    background: #dddddd;
}
</style>
