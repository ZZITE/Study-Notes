<template>
<!-- 个人中心联系 -->
  <div class="contact">
      <h1>{{ coupon }}</h1>
      <div class="contact-one">
          <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
            <el-form-item prop="type">
                <el-input type="leixing" v-model="ruleForm2.type" :placeholder="leixing"></el-input>
            </el-form-item>
            <el-form-item prop="pass">
                <el-input type="name" v-model="ruleForm2.pass" :placeholder="name"></el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
                <el-input type="name" v-model="ruleForm2.checkPass" :placeholder="danhao"></el-input>
            </el-form-item>
            <el-form-item prop="email">
                <el-input v-model="ruleForm2.email" :placeholder="youjian"></el-input>
            </el-form-item>
            <div class="comkk">
                <el-form-item prop="message">
                    <el-input v-model="ruleForm2.message" :placeholder="mesage"></el-input>
                </el-form-item>
            </div>
            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm2')">提交</el-button>
            </el-form-item>
            </el-form>
      </div>
      <strong></strong>
      <div class="contact-two">
        <p>{{ hours }}</p>
        <h2>{{ style }}</h2>
        <h3><em>{{ call }} </em>{{ numbert }}</h3>
        <span>{{ est }}</span>
      </div>
      <div class="contact-first"></div>
  </div>
</template>

<script>
export default {
    name: 'contact',
     data() {
    	    var validatetype = (rule, value, callback) => {
          var reg = /[a-zA-Z0-9\u4E00-\u9FA5\uf900-\ufa2d]/;
          if (value === '') {
            callback(new Error('请输入'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
        };
         var validateName = (rule, value, callback) => {
          //  验证用户名和邮件
          var reg = /^[a-zA-Z0-9]([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)$/; //邮箱正则
          if (value === '') {
            callback(new Error('请输入'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
        };
         var validatePass = (rule, value, callback) => {
          //  验证用户名
          var reg = /[\u4e00-\u9fa5_a-zA-Z0-9_]{4,10}/; 
          if (value === '') {
            callback(new Error('请输入'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
        };
         var validatePass2 = (rule, value, callback) => {
          //  验证用户名
          var reg = /^[0-9a-zA_Z]{5,20}/; ; 
          if (value === '') {
            callback(new Error('请输入'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
        };
       var validatemessage = (rule, value, callback) => {
          var reg = /^[\u4e00-\u9fa5_a-zA-Z0-9]+$/;
          if (value === '') {
            callback(new Error('请输入'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
        };
      return {
            coupon: 'Contact Us ',
            hours: 'If you don′t receive any reply within 48 hours, please drop us an email at',
            style: 'services@stylewe.com',
            call: 'Call',
            numbert: '+ 1(877)277-7209',
            est: '9am-6pm EST weekdays, 9am-5pm EST weekends',
            leixing: 'Type',
            name: 'Name',
            danhao: 'Order No (No,you can′t fill it out)',
            youjian: 'E-mail',
            mesage: 'Message',
            ruleForm2: {
                pass: '',
                checkPass: '',
                email: '',
                type: '',
                message: '',
            },
            rules2: {
            pass: [
                { validator: validatePass, trigger: 'blur' }
            ],
            checkPass: [
                { validator: validatePass2, trigger: 'blur' }
            ],
            email: [
                { validator: validateName, trigger: 'blur' }
            ],
            type: [
                { validator: validatetype, trigger: 'blur' }
            ],
            message: [
                { validator: validatemessage, trigger: 'blur' }
            ]
            }
        };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
}
</script>

<style>
    .contact {
        width: 860px;
        height: 421px;
        margin: 0 auto;
        margin-top: -20px;
    }
    .contact h1 {
        width: 100%;
        height: 30px;
        border-bottom: 1px solid #B7B7B7;
        font-size: 16px;
        color: #0f0f0f;
    }
    .contact strong {
        float: left;
        display: block;
        width: 1px;
        height: 380px;
        margin: 20px 30px 0 30px;
        background: #b7b7b7;
    }
    .contact-one {
        float: left;
        width: 374px;
        height: 400px;
        margin-left: 51px;
        margin-top: 20px;
    }
    .contact-two {
        float: right;
        width: 374px;
        height: 400px;
    }
    .contact-two P {
        margin-top: 157px;
        font-size: 14px;
        color: #0F0F0F;
        text-align: center;
    }
    .contact-two h2 {
        font-size: 14px;
        color: #E54C87;
        text-align: center;
    }
    .contact-two h3 {
        margin-top: 10px;
        text-align: center;
        color: #E54C87;
    }
    .contact-two em {
        color: #0F0F0F;
    }
    .contact-two {
        text-align: center;
        color: #595959;
    }
    .contact-one .el-button {
        width: 100%;
        border-radius: 0;
        border: 0;
        background: #e54c87;
    }
    .contact-one .el-button:active {
      border-color: #ccc;
      background: #ccc;
    }
    .contact-one .el-input__inner {
        border-radius: 0;
    }
    .comkk .el-input__inner {
        height: 80px;
        padding: 0 0 50px 10px;
    }

 .el-button {
    width: 100%;
    border-radius: 0;
    border-color: #e54c87;
    background: #e54c87;
    height: 36px;
}

</style>