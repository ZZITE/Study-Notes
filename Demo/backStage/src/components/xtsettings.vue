<template>
<!-- 系统设置 -->
    <div class="xtsetting">
        <!-- 第一个操作 -->
        <div v-if="willShow" class="xtsetting-nav">
            <div class="wether">
                <h2>可购买国家</h2>
            </div>
            <ul style="float: left;width: 760px;height:622px;margin: 0 0 0 120px;">
                <li v-for="(outer,index) in outers" :key="index">
                    {{ outer.emter }}
                </li>
            </ul>
            <div class="wethertwo">
                <h2>操作</h2>
            </div>
            <p @click="fn()" style="float:left;color:#4C4C4C;margin:20px 0 0 485px;">编辑</p>
        </div>
        <!-- 第二个操作 -->
        <div id="main" v-else class="xtsetting-main">
            <div class="wether">
                <h2>可购买国家</h2>
            </div>
            <h3>A</h3>
            <!-- 勾选国家 -->
            <ul style="float: left;width: 760px;height: 475px;margin: 0 0 0 120px;">
                <li v-for="(ender,index) in enders" :key="index">
                    <el-checkbox-group v-model="checkList">
                        <el-checkbox>{{ ender.addr }}</el-checkbox>
                    </el-checkbox-group>
                </li>
            </ul>
            <!-- 已选 -->
            <div class="bottom">
                <el-collapse v-model="activeNames">
                    <el-collapse-item title="已选：" name="1">
                        <ul>
                            <li v-for="(ter,index) in ters" :key="index">
                                {{ ter.xuan }}
                                <em style="width:9px;height:9px;color:#969696;font-weight:bold;">x</em>
                            </li>
                        </ul>
                    </el-collapse-item>
                </el-collapse>
                <!-- 按钮 -->
                <button style="width:60px;height:30px;background:#E54C87;margin:40px 19px 0 330px;border:0;color:white;">确定</button>
                <button @click="shent" style="color:#BDBDBD;border:0;background:#FAFAFA;outline: none;">取消</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            willShow: true,
            activeNames: ['1'],
            checkList: [''],
            outers: [
                {
                    emter: 'China'
                },
                {
                    emter: 'America'
                },            
                {
                    emter: 'Antigua and Barbuda'
                }
            ],
            enders: [
                {
                    addr: 'China'
                },
                {
                    addr: 'Japan'
                },
                {
                    addr: 'America'
                },
                {
                    addr: 'Canada'
                },
                {
                    addr: 'Germany'
                },
                {
                    addr: 'Korea'
                },
                {
                    addr: 'India'
                },
                {
                    addr: 'Thailand'
                },
                {
                    addr: 'Greece'
                },
                {
                    addr: 'Singapore'
                },
                {
                    addr: 'Italy'
                },
                {
                    addr: 'Britain'
                },
                {
                    addr: 'France'
                },
                {
                    addr: 'Russia'
                },
                {
                    addr: 'Egypt'
                },
                {
                    addr: 'Saudi'
                }
                ,
                {
                    addr: 'Malaysia'
                }
                ,
                {
                    addr: 'Brazil'
                }
                ,
                {
                    addr: 'Venezuela'
                }
                ,
                {
                    addr: 'Spain'
                },
                {
                    addr: 'Portugal'
                },
                {
                    addr: 'Chile'
                },
                {
                    addr: 'Mexico'
                },
                {
                    addr: 'Argentina'
                },
                {
                    addr: 'Yemen'
                },
                {
                    addr: 'Iceland'
                },
                {
                    addr: 'Haiti'
                },
                {
                    addr: 'Cuba'
                },
                {
                    addr: 'Netherlands'
                },
                {
                    addr: 'Greenland'
                },
                {
                    addr: 'Sweden'
                },
                {
                    addr: 'Switzerland'
                },
                {
                    addr: 'Luxembourg'
                }
            ],
            ters: [
                {
                    xuan: 'Algeria'
                }
            ]
        }
    },
    methods: {
        fn: function(){
          if(this.willShow==true){
            this.willShow=false;
          }else{
            this.willShow=true
          }
        },
        shent: function() {
            var div1 = document.getElementById("main")
            div1.style.display = "none"
        }
    }
}
</script>

<style>
/* 主体 */
.xtsetting {
    float: left;
    width: 100%;
    height: 948px;
    background: #E5E5E5;
}
/* 操作第一页 */
.xtsetting-nav {
    float: left;
    width: 1000px;
    height: 756px;
    margin:  100px 0 0 330px;
    background: white;
    box-shadow: 1px 1px 5px 1px rgba(112,5,46,0.3);
}
.xtsetting-nav li {
    display: block;
    float: left;
    width: 180px;
    height: 30px;
    margin-top: 29px;
    margin-right: 20px;
    line-height: 30px;
    text-align: center;
    color: #4C4C4C;
    border: 1px solid #999899;
}
.xtsetting-nav .wether {
    width: 100%;
    height: 34px;
    background: #f6f6f6;
    border-bottom: 1px solid #E5E5E5;
}
.wethertwo {
    float: left;
    width: 100%;
    height: 34px;
    background: #f6f6f6;
    border-top: 1px solid #E5E5E5;
    border-bottom: 1px solid #E5E5E5;
}
.wethertwo h2 {
    float: left;
    margin: 9px 0 0 96px;
    font-size: 16px;
    color: #4C4C4C;
}
/* 编辑页 */
.xtsetting-main {
    /* display: none; */
    float: left;
    width: 1000px;
    height: 756px;
    margin:  100px 0 0 330px;
    background: white;
    box-shadow: 1px 1px 5px 1px rgba(112,5,46,0.3);
}
.xtsetting-main .wether {
    width: 100%;
    height: 34px;
    background: #f6f6f6;
    border-bottom: 1px solid #E5E5E5;
}
.wether h2 {
    float: left;
    margin: 9px 0 0 96px;
    font-size: 16px;
    font-weight: bold;
    color: #4C4C4C;
}
/* 编辑页内容 */
.xtsetting-main h3 {
    width: 760px;
    margin: 30px auto;
    border-bottom: 1px solid #E5E5E5;
}
.xtsetting .el-checkbox-group {
    float: left;
    margin-right: 30px;
    margin-bottom: 30px;
}
.xtsetting .el-checkbox__inner {
    width: 14px;
    height: 14px;
    border-radius: 0;
}
/* 编辑页底部 */
.xtsetting .bottom {
    float: left;
    width: 806px;
    height: 150px;
    padding: 16px 97px 0 97px;
    background: #f6f6f6;
    border-top: 1px solid #E5E5E5;
}
.xtsetting .el-collapse-item__header {
    border: 0;
    background: #f6f6f6;
}
.xtsetting .el-collapse {
    border: 0;
}
.xtsetting .el-collapse-item__content {
    padding: 0px 15px;
    background: #f6f6f6;
}
.xtsetting .el-collapse-item__wrap {
    border: 0;
    background: #f6f6f6;
}
.xtsetting .bottom li {
    display: block;
    float: left;
    width: 72px;
    height: 32px;
    padding-left: 10px;
    line-height: 32px;
    color: #E54C87;
    border: 1px solid #E54C87;
}
.xtsetting .el-checkbox__label {
    margin: 0;
}
</style>
