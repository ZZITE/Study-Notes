<template>
  <div class="refund">
      <h1>{{ apply }}</h1>
      <div class="refund-main">
        <div class="refund-first">
            <h2><em>*</em>{{ type }}</h2>
            <el-checkbox v-model="checked">{{ only }}</el-checkbox>
            <el-checkbox v-model="checkedtwo">{{ fund }}</el-checkbox>
        </div>
        <div class="refund-dupp">
            <h2><em>*</em>{{ reason }}</h2>
            <el-checkbox v-model="checkedthree">{{ goods }}</el-checkbox>
            <el-checkbox v-model="checkedforu">{{ not }}</el-checkbox>
        </div>
        <div class="refund-third">
            <h2 style="margin: 5px 20px 0 0;"><em>*</em>{{ reft }}</h2>
            <el-select v-model="value4" clearable :placeholder="please" class="wiselect">
                <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="refund-four">
            <h2 style="margin: 5px 22px 0 0;"><em>*</em>{{ out }}</h2>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
            <h3>Most<span style="margin-left:4px;color:#e54c87">$59.10</span>,lnclusive freight <span style="margin-left:4px;color:#e54c87">$5.00</span></h3>
        </div>
        <div class="refund-five">
            <h2 style="margin: 30px 0 0 0;">{{ descr }}</h2>
            <el-input v-model="inputt" :placeholder="disc"></el-input>
        </div>
        <div class="refund-six">
            <h2 style="margin: 5px 37px 0 0;">{{ photo }}</h2>
            <el-upload
            action="https://jsonplaceholder.typicode.com/posts/"
            list-type="picture-card"
            :disabled = "canupload"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            :on-success="imgupload">
            <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog v-model="dialogVisible" size="tiny">
            <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
            <p>{{ pictye }}</p>
            <button type="button" class="el-button el-button--primary" style="margin:30px 0 0 70px;"><span>SlGN lN</span></button>
        </div>
      </div>
      <strong></strong>
      <div class="refund-nav">
          <h2>{{ ring }}</h2>
          <div class="refund-come">
            <span>{{ times }}</span>
            <ul>
                <li v-for="(i,index) in them" :key="index">
                    <img :src="i.images" alt="">
                    <h2 style="margin: 5px 0 0 0;">{{ i.idas }}</h2>
                    <p style="float:left;margin-bottom:10px;">{{ i.asym }}</p>
                    <span style="float:left;color: black;width:164px;margin-bottom:3px;">{{ i.color }}</span>
                    <em style="float:left;font-size:12px;color:black;width:164px;margin-bottom:3px;">{{ i.sizee }}</em>
                    <h3 style="float:left;font-size:12px;color:black;">{{ i.label }}</h3>
                </li>
            </ul>
          </div>
      </div>
  </div>
</template>

<script>

export default {
    name: 'withdraw',
    data() {
        return {
            times: 0,
            canupload: false,  //图片上传次数 
            dialogImageUrl: '',
            dialogVisible: false ,        
            value4: '',
            apply: 'APPLY RETURNS AND EXCHANGES',
            checked: true,
            checkedtwo: true,
            checkedthree: true,
            checkedforu: true,
            type: 'Service type:',
            only: 'Refund only',
            fund: 'Refund of return',
            reason: 'Cargo status:',
            goods: 'Received goods',
            not: 'Goods not received',
            reft: 'Refund reason:',
            please: 'Please select',
            out: 'refund amount:',
            input: '$59.10',
            descr: 'Remarks:',
            inputt: '',
            disc: 'Refund description',
            photo: 'Upload photo:',
            imageUrl: '',
            pictye: '6 sheets at most',
            ring: 'Ordering Information:',
            times: '2017-08-29 04:27:28 Order NO.8T902765',
            images: 'static/images/usa.png',
            them: [
                {
                    images: 'static/images/usa.png',
                    idas: 'idas',
                    asym: 'White Asymmetrical Shirt Collar Long Sleeve Silk-blend Folds Tunic',
                    color: 'Color : White',
                    sizee: 'Size:8',
                    label: 'Label Size : L'
                }
            ],
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
        }
    },
    methods: {
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
        },
      imgupload () {
          if (!(this.times < 2)) {
            this.canupload = true;
            console.log(111)
          } 
      }
    }
}
</script>

<style>
.refund {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    margin-top:-34px;
}
.refund::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
.refund-main {
    float: left;
    width: 541px;
    height: 523px;
}
.refund h1 {
    width: 100%;
    margin-top: 20px;
    border-bottom: 1px solid #B7B7B7;
}
.refund-first {
    margin-top: 20px;
}
.refund em {
    color: #e54c87;
}
.refund h2 {

}
.refund .el-checkbox__inner::after {
    left: 2px;
    top: -1px;
    border-color: #e54c87;
}
.refund .el-checkbox__input.is-checked .el-checkbox__inner {
    width: 12px;
    height: 12px;
    margin-left: 20px;
    border-radius: 0;
    background: white;
    border-color: #b7b7b7;
}
.refund .el-checkbox__inner {
    width: 12px;
    height: 12px;
    margin-left: 20px;
    border-radius: 0;
    border: 1px solid #b7b7b7;
}
.refund-dupp {
    margin-top: 15px;
}
.refund-third {
    margin-top: 20px;
}
.refund-third .el-input__inner {
    width: 259px;
    height: 30px;
    border-radius: 0;
    margin: 10px 0 0 18px;
}
.refund-four {
    margin-top: 20px;
}
.refund-four h3 {
    font-size: 12px;
    margin-top: 10px;
    margin-left: 18px;
    color: #595959;
}
.refund-four .el-input {
    width: 259px;
}
.refund-four .el-input__inner {
    width: 259px;
    height: 30px;
    color: #e54c87;
    border-radius: 0;
    margin: 10px 0 0 18px;
}
.refund-five {
    margin-top: 20px;
}
.refund-five .el-input {
    width: 420px;
}
.refund-five .el-input__inner {
    width: 420px;
    height: 90px;
    padding: 0 0 60px 10px;
    border-radius: 0;
}
.refund-six {
    margin-top: 21px;
}
.refund-six p {
    font-size: 12px;
    margin-left: 127px;
    color: #595959;
}
.refund-six .el-button {
    width: 370px;
    height: 40px;
    margin-top: 14px;
    border-radius: 0;
    border: 0;
    background: #e54c87;
}
.refund strong {
    float: left;
    display: block;
    width: 1px;
    height: 380px;
    margin: 20px 20px 0 20px;
    background: #B7B7B7;
}
.refund-nav {
    float: left;
    width: 278px;
    margin-top: 20px; 
}
.refund-nav h2:nth-child(1) {
    position: relative;
    left: -10px;
}
.refund-come {
    float: left;
    width: 278px;
    height: 100%;
    margin-top: 20px;
}
.refund-come span {
    color: #595959;
    font-size: 12px;
}
.refund-come img {
    float: left;
    width: 78px;
    height: 108px;
    margin-top: 10px;
    margin-right: 10px;
}
.refund-come p {
    font-size: 12px;
    width: 190px;
    height: 27px;
    color: #595959;
}
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #20a0ff;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #CFCFCF;
    width: 90px;
    height: 90px;
    line-height: 90px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>