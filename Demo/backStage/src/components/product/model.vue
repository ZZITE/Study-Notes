<template>
<!-- 尺码管理 -->
    <div class="size">
        <div class="size-header">
            <!-- 头 -->
            <label style="float:left;margin-left:20px;" for="">尺码搜索：
                <el-input
                    placeholder="输入尺码名称"
                    icon="search"
                    v-model="input2"
                    :on-icon-click="handleIconClick">
                </el-input>
            </label>

            <button style="float:right;margin-top:50px;margin-right:30px;cursor: pointer;;" @click="addshow=true">新增尺码</button>
        </div>
     
        <div class="de-section" style="" v-for="(item, index) in designers" :key="index">
        <!-- 显示主体 -->
          <h2>{{item.initial}}</h2>
          <div class="de-name">
            <ul style="float:left;height:100%;overflow:hidden;">
              <li style="float:left;" v-for="(i, index) in item.name" :key="index">
                <a @click="currentActive = index" class="de-a">   
                    {{ i }}
                </a>
              </li>
            </ul>

        <!-- 弹窗 -->

            <div id="mask" v-if="addshow" class="mask"></div>

              <div v-if="addshow" class="spender">
                <el-collapse v-model="activeNames">
                    <el-collapse-item title="基本资料" name="1">
                        <div class="data" style="margin-top:20px;font-size:14px">
                            名称<input style="margin-left:20px" v-model="addname"></input>
                        </div>
                    </el-collapse-item>
                    <el-collapse-item title="尺码表格" name="2">
                      <div style="width:100%;padding:20px 0 0 8px;">
                        <sizetable></sizetable>
                      </div>
                    </el-collapse-item>
                    <el-collapse-item title="可用分类" name="3">

                        <el-select v-model="value" placeholder="请选择">
                            <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                            </el-option>
                        </el-select>

                    </el-collapse-item>
                </el-collapse>

                <div class="sizeBtn" style="width:100%;text-align:center;margin-top:120px;">
                    <button @click="">保存</button>
                    <button @click="addshow=false">关闭</button>
                    <button @click="">删除</button>
                </div>
              </div>


          </div>
      </div>
    </div>
</template>
<script>
import sizetable from '@/components/table.vue';
export default {
    components: {
        sizetable
    },
    data() {
        return {
            options: [{
                    value: '选项1',
                    label: '黄金糕'
                    }, {
                    value: '选项2',
                    label: '双皮奶'
                    }, {
                    value: '选项3',
                    label: '蚵仔煎'
                    }, {
                    value: '选项4',
                    label: '龙须面'
                    }, {
                    value: '选项5',
                    label: '北京烤鸭'
                    }],
                    value: '',
            main: 'Founded in 2013, this bag brand focuses on simplicity and rumination. It stresses the design of dimensionally geometrical lines. In terms of material, the bags are made of the first layer of cowhide leather or sheepskin with scratch and scar, which feels soft. The concept of design is to emphasize the idea of Simplicity by the contrast between the cross-cutting Design material and texture. She hopes to open a small business on the streets in Europe to share some bags with stories. By placing the Retro rumination above the trend of artistic feelings, a bag with a story can eventually find the rightful owner.',
            designers: [
                {
                inputer: '点击一下',
                initial: 'A',
                name: ['不用中文翻译.直接显示中文','A certain size(中文翻译)','A certain size(中文翻译)','Mobile NumberD']
                },
            ],
            addshow: false,
            addname: ''
        }
    },
    methods: {
    handleIconClick(ev) {
      console.log(ev);
    }
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
    padding-left: 20px;
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
    height: 840px;
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
</style>