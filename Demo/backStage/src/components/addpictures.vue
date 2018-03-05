<template>
<div>
    <!--右侧 -->
        <div class="pictures">
        <h2>{{ pict }}</h2>
        <el-upload style="margin-left:12px;"
            action="https://jsonplaceholder.typicode.com/posts/"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove">
            <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog v-model="dialogVisible" size="tiny">
            <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
        <div class="zhuangtai">
            <h2>{{ main }}</h2>
            <el-input v-model="input" placeholder=""></el-input>
            <h2>{{ url }}</h2>
            <el-input v-model="inputz" placeholder=""></el-input>
            <div class="button-main">   
                <el-button>取消</el-button>
                <el-button>确定发布</el-button>
            </div> 
        </div>
    </div>
    <home></home>
</div>
</template>

<script>
import home from '@/components/homepage.vue'
 export default {
    components: {
        home
    },
    data() {
      return {
        pict: '图片：',
        main: '文字内容：',
        dialogImageUrl: '',
        dialogVisible: false,
        input: '',
        inputz: '',
        url: '跳转连接'
      };
    },
    methods: {
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      }
    }
  }
</script>

<style>
.pictures {
    float: right;
    width: 300px;
    height: 929px;
    padding: 19px 0 0 20px;
}
.pictures h2 {
    color: #747474;
}
.pictures .el-upload--picture-card {
    width: 100px;
    height: 100px;
    border-radius: 0;
}
.pictures .el-upload-list--picture-card .el-upload-list__item {
    width: 229px;
    height: 96px;
}
.pictures .el-upload-list--picture-card .el-upload-list__item img {
    width: 100%;
    height: 100%;
}
.pictures .el-upload--picture-card i {
    display: block;
    line-height: 100px;
}
.el-upload-list--picture-card .el-upload-list__item-actions {
    width: 100%;
    height: 100%;  
}
.zhuangtai {
    width: 100%;
    height: 300px;
    margin-top: 30px;
}
.zhuangtai .el-input {
    width: 229px;
    height: 32px;
    margin-top: 10px;
    margin-bottom: 29px;
}
.zhuangtai .el-input__inner {
    border-radius: 0;
}
.button-main {
    margin-left: 39px;
}
.button-main button:nth-child(1) {
    border: 0;
    color: #C4C4C4;
}
.button-main button:nth-child(2) {
    width: 86px;
    height: 32px;
    background: #E54C87;
    border-radius: 0;
    border: 0;
    color: white;
}
</style>
