<template>
<!-- 注册页面 -->
    <div class="login-wrap">
        <div class="ms-login">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="帐号"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="密码" v-model="ruleForm.password" @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>
                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
                </div>
                <!-- <p style="font-size:12px;line-height:30px;color:#999;">Tips : 用户名和密码随便填。</p> -->
            </el-form>
        </div>
    </div>  
</template>

<script>
import axios from 'axios'
        var validateEmail = (rule, value, callback) => {
          var reg = /^[a-zA-Z0-9]([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)$/; //邮箱正则
          if (value === '') {
            callback(new Error('请输入邮箱'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('格式错误'))
          }
        };
                var validateEass = (rule, value, callback) => {
        var regExp = /^[a-zA-Z][a-zA-Z0-9]{7,31}$/;
        if (value === '') {
          callback(new Error('请输入密码'))
        } else if (regExp.test(value) === false) {
          callback(new Error('密码为8-16位以英文字母开头+数字'))
        } else {
          callback()
        }
      }
    export default {
        data: function(){
            return {
                ruleForm: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        { validator: validateEmail, trigger: 'blur' }
                    ],
                    password: [
                        { validator: validateEass, trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            submitForm(formName) {
                const self = this;
                self.$refs[formName].validate((valid) => {
                    if (valid) {
                    axios.post('/admin/login',{
                        email: self.ruleForm.username,
                        password: self.ruleForm.password
                        })
                        .then(function(res){
                            console.log(res)
                          if (res.data.success) {
                              localStorage.setItem('ms_username',self.ruleForm.username);
                              localStorage.setItem('onlytoken',res.data.olytoken);
                              self.$router.push('/picty');
                          } else if (res.data.message == 'verify error') {
                              alert('账号或密码错误')
                          } else {
                              alert('没有权限')
                          }
                        })
                        .catch(function(err){
                        console.log(err);
                        alert('服务器异常')
                    });
                    }
/*                    if (valid) {
                        localStorage.setItem('ms_username',self.ruleForm.username);
                        self.$router.push('/home');
                        */
                    else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    }
</script>

<style>
    .login-wrap{
        position: relative;
        height:900px;
    }
    .ms-title{
        position: absolute;
        top:50%;
        width:100%;
        margin-top: -230px;
        text-align: center;
        font-size:30px;
        color: #fff;
    }
    .el-input__inner {
        border-radius: 0;
    }
    .ms-login{
        position: absolute;
        left:50%;
        top:50%;
        width:300px;
        height:160px;
        margin:-150px 0 0 -190px;
        padding:40px;
        border-radius: 5px;
        background: #fff;
    }
    .login-btn{
        text-align: center;
    }
    .login-btn button{
        width:100%;
        height:36px;
        border: 0;
        background: #E54C87;
        border-radius: 0;
    }
    .el-button--primary:focus, .el-button--primary:hover {
         background: #E54C87;
    }
    .login-btn button:active {
        background: #f8458a;
    }
</style>