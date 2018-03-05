<template>
<!-- 数据分析 -->
    <div class="analy">
        <div class="fangwen">
            <div class="block" style="margin-bottom:30px;">
                <span style="margin-right:25px;" class="demonstration">本月</span>
                <span style="margin-right:30px;" class="demonstration">本周</span>
                <el-date-picker
                v-model="value4"
                type="datetimerange"
                :picker-options="pickerOptions2"
                placeholder="选择时间范围"
                align="right">
                </el-date-picker>
            </div>
            <strong>
                <h2>访客人数</h2>
                <em>10</em>
            </strong>
            <strong>
                <div class="onenice"></div>
                <div class="twonice"></div>
                <img class="imgone" src="static/images/xiantiao.png" alt="">
                <img class="imgtwo" src="static/images/xiantiao2.png" alt="">
                <h2 style="position:relative;left:-50px;top:-5px;float:right;width:100px;margin:0 0 0 0;">下单转化率</h2>
                <span style="float:left;margin: 0 0 0 70px;" class="spanone">00.00%</span>
                <h2 style="text-align:center;margin:130px 0 0 0;">下单转化率</h2>
                <span class="spanone">00.00%</span>
                <h2 style="text-align:center;margin:53px 0 0 0;">下单转化率</h2>
                <span class="spanone">00.00%</span>
                <div class="threenice"></div>
                <div class="fournice"></div>
            </strong>
            <strong>
                <h2>支付人数</h2>
                <em>10</em>
                <h2>支付金额</h2>
                <em>10</em>
            </strong>
            <strong>
                <h2>下单人数</h2>
                <em>10</em>
                <h2>下单金额</h2>
                <em>10</em>
            </strong>
            <strong>
                <h2>金额总计</h2>
                <em>10</em>
            </strong>
        </div>
        <div class="Statistics">
            <div id="myChart" :style="{ width: '1000px', height: '390px',margin:'0' }"></div>
        </div>
        <div class="region">
            <el-table
                :data="tableData3"
                height="403"
                border
                style="width: 703">
                <el-table-column
                prop="date"
                label="日期"
                width="335">
                </el-table-column>
                <el-table-column
                prop="name"
                label="退货金额"
                width="93">
                </el-table-column>
                <el-table-column
                prop="zhanbi"
                label="占比"
                width="90">
                </el-table-column>
                <el-table-column
                prop="money"
                label="订货金额"
                width="93">
                </el-table-column>
                <el-table-column
                prop="zhan"
                label="占比"
                width="90">
                </el-table-column>
            </el-table>
        </div>
        <div class="map">
            <div id="myChant" :style="{ width: '846px', height: '410px',margin:'0' }"></div>
        </div>
        <div class="fromway">
            <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
                prop="date"
                label="日期"
                width="180">
            </el-table-column>
            <el-table-column
                prop="name"
                label="订货单"
                width="180">
            </el-table-column>
            <el-table-column
                prop="address"
                label="退货单">
            </el-table-column>
            <el-table-column
                prop="kehu"
                label="订货客户数">
            </el-table-column>
            <el-table-column
                prop="trkehu"
                label="退货客户数">
            </el-table-column>
            <el-table-column
                prop="dhmoney"
                label="订货金额">
            </el-table-column>
            <el-table-column
                prop="thmoney"
                label="退货金额">
            </el-table-column>
            <el-table-column
                prop="xjmoney"
                label="金额小计">
            </el-table-column>
            </el-table>
        </div>
        <div class="positioning">
            <button style="color:#4D4D4D;background:#E3E3E3;border:0;margin:9px 0 0 15px;">导出数据</button>
            <el-pagination style="float:right;height:100%;"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage1"   
            :page-size="100"
            layout="total, prev, pager, next"
            :total="1000">
            </el-pagination>
        </div>
    </div>
</template>

<script>
import echarts from 'echarts'

var xData = function() {
    var data = [];
    for (var i = 1; i < 13; i++) {
        data.push(i + "天");
    }
    return data;
}();

export default {
    data() {
      return {
        currentPage1: 5,
        currentPage2: 5,
        currentPage3: 5,
        currentPage4: 4,
        tableData: [
            {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },
                        {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },            {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },            {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },            {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },            {
                date: '2016-05-02',
                name: '100',
                address: '100',
                kehu: '100',
                trkehu: '100',
                dhmoney: '100',
                thmoney: '100',
                xjmoney: '100'
            },
        ],
        tableData3: [
            {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
            {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
                        {
                date: '1 美国加利福尼亚州',
                name: '60000',
                zhanbi: '55.55%',
                money: '60000',
                zhan: '55.55%'
            },
        ],
        pickerOptions2: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value4: ''
      };
    },
    mounted() {
    this.drawLine();
    },
    methods: {
        handleClick(tab, event) {
        console.log(tab, event);
      },
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
      },
      drawLine() {
        let myChart = echarts.init(document.getElementById('myChart'))
        let myChant = echarts.init(document.getElementById('myChant'))
        myChart.setOption({
            // backgroundColor: "#344b58",
            "title": {
                textStyle: {
                    color: '#fff',
                    fontSize: '22'
                },
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "shadow",
                    textStyle: {
                        color: "#fff"
                    }

                },
            },
            "grid": {
                "borderWidth": 0,
                "top": 30,
                "bottom": 70,
                textStyle: {
                    color: "#fff"
                }
            },
            "legend": {
                x: '5%',
                top: '0',
                textStyle: {
                    color: '#90979c',
                },
                "data": ['订货金额', '退货金额', '合计金额','订单总量']
            },
            
            "calculable": true,
            "xAxis": [{
                "type": "category",
                "axisLine": {
                    lineStyle: {
                        color: '#90979c'
                    }
                },
                "splitLine": {
                    "show": false
                },
                "axisTick": {
                    "show": false
                },
                "splitArea": {
                    "show": false
                },
                "axisLabel": {
                    "interval": 0,

                },
                "data": xData,
            }],
            "yAxis": [{
                "type": "value",
                "splitLine": {
                    "show": false
                },
                "axisLine": {
                    lineStyle: {
                        color: '#90979c'
                    }
                },
                "axisTick": {
                    "show": false
                },
                "axisLabel": {
                    "interval": 0,

                },
                "splitArea": {
                    "show": false
                },

            }],
            "dataZoom": [{
                "show": true,
                "height": 30,
                "xAxisIndex": [
                    0
                ],
                "start": 10,
                "end": 80,
                handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
                handleSize: '110%',
                handleStyle:{
                    color:"#d3dee5",
                    
                },
                textStyle:{
                    color:"#fff"},
                borderColor:"#90979c"
            }, {
                "type": "inside",
                "show": true,
                "height": 15,
                "start": 1,
                "end": 35
            }],
            "series": [{
                    "name": "订货金额",
                    "type": "bar",
                    "stack": "总量",
                    "barMaxWidth": 35,
                    "barGap": "10%",
                    "itemStyle": {
                        "normal": {
                            "color": "rgba(255,144,128,1)",
                            "label": {
                                "show": true,
                                "textStyle": {
                                    "color": "#fff"
                                },
                                "position": "insideTop",
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            }
                        }
                    },
                    "data": [
                        709,
                        1917,
                        2455,
                        2610,
                        1719,
                        1433,
                        1544,
                        3285,
                        5208,
                        3372,
                        2484,
                        4078
                    ],
                },

                {
                    "name": "退货金额",
                    "type": "bar",
                    "stack": "总量",
                    "itemStyle": {
                        "normal": {
                            "color": "rgba(0,191,183,1)",
                            "barBorderRadius": 0,
                            "label": {
                                "show": true,
                                "position": "right",
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            }
                        }
                    },
                    "data": [
                        327,
                        1776,
                        507,
                        1500,
                        800,
                        482,
                        204,
                        1390,
                        1001,
                        951,
                        381,
                        220
                    ]
                },
                {
                    "name": "订单总量",
                    "type": "bar",
                    "stack": "总量",
                    "itemStyle": {
                        "normal": {
                            "color": "pink",
                            "barBorderRadius": 0,
                            "label": {
                                "show": true,
                                "position": "top",
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            }
                        }
                    },
                    "data": [
                        327,
                        1776,
                        1307,
                        1200,
                        800,
                        482,
                        204,
                        1390,
                        1001,
                        951,
                        381,
                        220
                    ]
                }, {
                    "name": "合计金额",
                    "type": "line",
                    "stack": "总量",
                    symbolSize:10,
                    symbol:'circle',
                    "itemStyle": {
                        "normal": {
                            "color": "rgba(252,230,48,1)",
                            "barBorderRadius": 0,
                            "label": {
                                "show": true,
                                "position": "top",
                                formatter: function(p) {
                                    return p.value > 0 ? (p.value) : '';
                                }
                            }
                        }
                    },
                    "data": [
                        2017,
                        5469,
                        4269,
                        5310,
                        2519,
                        1915,
                        1748,
                        4675,
                        6209,
                        4323,
                        2865,
                        4298
                    ]
                },
            ]
        })
      }
    }
  };
</script>

<style>
.analy {
    float: left;
    width: 100%;
    height: 100%;
    background: #F6F6F6;
}
.fangwen {
    float: left;
    width: 522px;
    height: 384px;
    margin: 30px 75px 0 20px;
}
.fangwen .el-input__inner {
    width: 330px;
    height: 32px;
    font-size: 12px;
    text-align: center;
    color: #E54C87;
    border-radius: 0;
}
.fangwen .el-input__icon {
    right: 30px;
}
.el-picker-panel {
    margin-left: 280px;
}
.fangwen strong:nth-child(2) {
    float: left;
    display: block;
    width: 150px;
    height: 111 px;
    border: 1px solid #E5E5E5;
}
.fangwen h2 {
    margin-top: 30px;
    margin-left: 40px;
    color: #747474;
    font-size: 16px;
}
.fangwen em {
    margin-left: 53px;
    margin-top: 9px;
    color: #353535;
    font-size: 36px;
}
.fangwen strong:nth-child(3) {
    float: left;
    display: block;
    width: 220px;
    height: 208px;
}
.fangwen strong:nth-child(4) {
    float: left;
    display: block;
    width: 148px;
    height: 208px;
    border: 1px solid #E5E5E5;
}
.fangwen strong:nth-child(5) {
    position: relative;
    float: left;
    top: -111px;
    display: block;
    width: 150px;
    height: 223px;
    border: 1px solid #E5E5E5;
}
.fangwen strong:nth-child(6) {
    float: right;
    display: block;
    width: 148px;
    height: 113px;
    border-left: 1px solid #E5E5E5;
    border-right: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
}
.spanone {
    display: block;
    font-size: 24px;
    color: #E54C87;
    text-align: center;
}
.onenice {
    position: relative;
    top: 28px;
    width: 64px;
    height: 2px;
    border-top: 1px solid #999899;
    border-bottom: 1px solid #999899;
}
.twonice {
    float: right;
    position: relative;
    top: 24px;
    width: 64px;
    height: 2px;
    border-top: 1px solid #999899;
    border-bottom: 1px solid #999899;
}
.imgone {
    float: left;
    position: relative;
    top: 101px;
}
.imgtwo {
    float: left;
    position: relative;
    top: 165px;
}
.threenice {
    position: relative;
    top: -28px;
    width: 64px;
    height: 2px;
    border-top: 1px solid #999899;
    border-bottom: 1px solid #999899;
}
.fournice {
    float: right;
    position: relative;
    top: -31px;
    width: 64px;
    height: 2px;
    border-top: 1px solid #999899;
    border-bottom: 1px solid #999899;
}
.Statistics {
    float: left;
    width: 1000px;
    height: 390px;
    margin-top: 30px;
}
.region {
    float: left;
    width: 703px;
    height: 403px;
    margin-top: 58px;
    margin-left: 20px;
}
.map {
    float: left;
    width: 845px;
    height: 410px;
    margin: 58px 0 0 34px;
    background: pink;
}
.fromway {
    float: left;
    width: 100%;
    height: 100%;
    margin-top: 60px;
}
 /* 底部 */
.positioning {
    position: fixed;
    width: 1643px;
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
.positioning .el-pagination__total {
  display: none;
}
</style>
