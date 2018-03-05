<template>
  <div class="login-main">
    <div class="login-maintwo">
      <!-- 第三方 -->
      <h2>{{ socal }}</h2>
      <div class="login-awrap">
        <a href="http://192.168.0.112:8000/auth/google">  <!-- @click="loginBy('google')"-->
          <span>
            <img src="static/images/guge.png" alt="">
          </span>
          <em>{{ Google }}</em>
        </a>
      </div>
      <a href="">
        <span>
            <img src="static/images/book.png" alt="">
        </span>
        <em>{{ Facebook }}</em>
      </a>
    </div>
    <!-- 登入页面 -->
    <div class="sign">
      <h2>{{ IN }}</h2>
      <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
        <el-form-item prop="name">
          <el-input v-model="ruleForm2.name" :placeholder="mname"></el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input type="password" v-model="ruleForm2.pass" auto-complete="off" :placeholder="main"></el-input>
        </el-form-item>
        <el-form-item class="class">
          <el-button type="primary" @click="login('ruleForm2')">{{ dengru }}</el-button>
        </el-form-item>
      </el-form>
      <el-checkbox v-model="checked">{{ stay }}</el-checkbox>
      <a class="sign-pass" @click="open3">{{ fort }}</a>
    </div>
    <strong></strong>
    <!-- 注册页面 -->
    <div class="gister">
      <h2>{{ REG }}</h2>
      <el-form :model="ruleForm3" :rules="rules2" ref="ruleForm3" class="demo-ruleForm">
        <el-form-item prop="mail">
          <el-input style="width:369px" v-model="ruleForm3.mail" auto-complete="off" :placeholder="youxiang2"></el-input>
        </el-form-item>
        <el-form-item prop="pasd">
          <el-input style="width:369px" type="password" v-model="ruleForm3.pasd" auto-complete="off" :placeholder="mima2"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="signup('ruleForm3')">{{ zhuce }}</el-button>
        </el-form-item>
      </el-form>
      <p>When you <span>Register,</span> you agree to our <em>User Agreement</em>
      and acknowlegge reading our <em>User Privacy Notice</em>
      </p>
    </div>
     <div class="g-recaptcha" data-sitekey="6LdQby8UAAAAAKyVYq-g2kCEIcK96DL82DCLcqfK" style="margin-left:400px"></div>
  </div>
</template>
<script src="https://www.google.com/recaptcha/api.js"> 
</script>
<script>
import axios from 'axios'
          //  邮箱
         var validateEmail = (rule, value, callback) => {
          var reg = /^[a-zA-Z0-9]([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)$/; //邮箱正则
          if (value === '') {
            callback(new Error('Please enter the mailbox'));
          }else if(reg.test(value) === true){
            callback();
          } else {
           callback(new Error('Input error'))
          }
        };
      //验证密码正则表达式
      var validatePassword = (rule, value, callback) => {
        var regExp = /^[a-zA-Z][a-zA-Z0-9]{7,31}$/;
        if (value === '') {
          callback(new Error('Please input a password'))
        } else if (regExp.test(value) === false) {
          callback(new Error('Password error'))
        } else {
          callback()
        }
      }
      // 注册
      // 姓正则表达式
      /*
      var change = (rule, value, callback) => {
       var regExp = /[\u4e00-\u9fa5_a-zA-Z0-9_]{4,10}/ //只能输入数字和英文还有中文
          if (value === '') {
            callback(new Error('请输入'));
          }else if(regExp.test(value) === false){
            callback();
          } else {
           callback(new Error('输入错误'))
          }
      };
      */
      // 姓名正则表达式
      /*var validatePPass = (rule, value, callback) => {
          var regExp=/^[\u4e00-\u9fa5]{2,4}$/;
          if (value === '') {
            callback(new Error('请输入'));
          }else if(regExp.test(value) === false){
            callback(new Error('输入错误'))
          } else {
            callback();
        }
      };
      */
      // 邮箱正则表达式
      var validateAass = (rule, value, callback) => {
          var regExp=/^[a-zA-Z0-9]([a-zA-Z0-9_-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)$/;
          if (value === '') {
            callback(new Error('Please enter the mailbox'));  
          }else if(regExp.test(value) === false){
            callback(new Error('Mailbox error'))
          } else {
            callback();
        }
      };
      // 密码正则表达式
        var validateEass = (rule, value, callback) => {
        var regExp = /^[a-zA-Z][a-zA-Z0-9]{7,31}$/;
        if (value === '') {
          callback(new Error('Please input a password'))
        } else if (regExp.test(value) === false) {
          callback(new Error('8-16 letters and numbers can not be pure numbers or pure English'))
        } else {
          callback()
        }
      }
export default {
    data() {
        return {
            fort: 'Forgot password',
            stay: 'Stay signed in',
            mname: 'Email address',
            main: 'Passwprd',
            dengru: 'SlGN lN',
            xingshi: 'First name',
            xingming: 'Last name',
            youxiang2: 'Email address',
            mima2: 'Password',
            zhuce: 'REGlSTER',
            checked: true,
            input2:'',
            input3:'',
            input4: '',
            input5: '', 
            input6: '',
            input7: '', 
            socal: 'CONNECT WlTH SOClAL',
            Google: 'Google',
            Facebook: 'Facebook',
            IN: 'SlGN lN',
            REG: 'REGlSTER',
            // 登入内容属性
            ruleForm2: {
                pass: '',
                name: ''
            },
            // 注册内容属性
            ruleForm3: {
              pasd: '',
              mail: ''
            },
            // 定义
            rules2: {
              pass: [
                { validator: validatePassword, trigger: 'blur' }
              ],
              name: [
                { validator: validateEmail, trigger: 'blur' }
              ],
              mail: [
                { validator: validateAass, trigger: 'blur'}
              ], 
              pasd: [
                { validator: validateEass, trigger: 'blur'}
              ]
            }
          };
        },
        // 执行成功回调
        methods: {
          open3() {
              this.$prompt('Enter the mailbox so that we can send confirmation mail', {
                confirmButtonText: '确定',
                showCancelButton: false,
                customClass: 'apple',
                inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
                inputErrorMessage: 'Mailbox error'
              }).then(({ value }) => {
                axios.post('/auth/password/restore/request',{
                  email: value,
                })
                .then(function(res){
                  console.log(res)
                  if(res.data.success == false) {
                    alert("邮箱不存在、失败")
                  } else if(res.data.success == true) {
                    if (res.data.email_change_warning == true) {
                      alert('建议更改邮箱')
                    }
                    alert("发送成功")
                    this.$message({
                    type: 'success',
                    message: 'Your email address is: ' + value
                  });
                  }
                })
                .catch(function(err){
                  
                });
              }).catch(() => {
                this.$message({
                  type: 'info',
                  message: 'Cancel input'
                });       
              });
          },
          // 注册
          signup(formName) {
            var self = this;
            var url;
            var fromdata;
              url = '/auth/register'
              fromdata = {
                email: this.ruleForm3.mail,
                password: this.ruleForm3.pasd,
                g_recaptcha_response: null,
            }
            try { (grecaptcha.getResponse())
              fromdata.g_recaptcha_response = grecaptcha.getResponse()
            } catch (err) {
              fromdata.g_recaptcha_response = 'nogrecaptcha'
            }
            this.$refs[formName].validate((valid) => {
              if (valid) {
              axios({
                method: 'post',
                url: url,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}, // application/x-www-form-urlencoded
                data: fromdata
              })
              .then(function (response) {
                console.log(response.data)
                // this.$router.push({path: '/Home'});
                if(response.data.need_captcha){
                   self.captcha()
                }
                if(response.data.success == false) {
                  alert("注册失败")
                  if(response.data.message == 'email existing') {
                    alert("邮箱已存在")
                    self.$refs['ruleForm3'].resetFields()
                  } 
                  if(response.data.captcha_success ==false) {
                    alert("验证码失败")
                  }
                } else if(response.data.success == true) {
                  alert("注册成功")
                  console.log(response.data)
                  self.$refs['ruleForm3'].resetFields()
                  self.$router.push({path: '/login'})
                }
                })
                .catch(function (error) {
                  console.log(error);
                  alert('shibai')
                  // console.log(data)
                });
              } else {
                console.log('error submit!!')
                return false;
                self.$refs['ruleForm2'].resetFields()
  
              }
            });
          },
          // 登入
          login(formName) {
            var self = this;
            var ente;
            var fromdata;
              ente = '/auth/login'
              fromdata = {
                email: this.ruleForm2.name,
                password: this.ruleForm2.pass,
                g_recaptcha_response: null
            }
            try { (grecaptcha.getResponse())
              fromdata.g_recaptcha_response = grecaptcha.getResponse()
            } catch (err) {
              fromdata.g_recaptcha_response = 'nogrecaptcha'
            }
            this.$refs[formName].validate((valid) => {
              if (valid) {
              axios({
                method: 'post',
                url: ente,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}, // application/x-www-form-urlencoded,
                data: fromdata,
              })
              .then(function (response) {
                console.log(response.data)
                if(response.data.need_captcha){
                   self.captcha()
                }
                if(response.data.success == false) {
                  alert("登入失败")
                  if(response.data.message == 'verify error') {
                    alert("密码错误")
                    self.ruleForm2.pass = ''                   
                  } 
                  if(response.data.captcha_success ==false) {
                    alert("验证码失败")
                  }
                } else if(response.data.success == true) {
                  window.localStorage.setItem('token', response.data.olytoken)
                  axios.defaults.headers['olytoken'] = window.localStorage.getItem('token')
                  alert("登入成功")
                  self.$router.push({path: '/'});
                  // self.$router.push({path: '/Home'});
                }
                })
                .catch(function (error) {
                  console.log(error);
                  // self.$router.push({path: '/'});
                  // console.log(data)
                });
              } else {
                console.log('error submit!!')
                return false;
                self.$refs['ruleForm2'].resetFields()
              }
            });
          },

          //第三方
          loginBy() {
            axios({
                method: 'get',
                url: 'http://192.168.0.112:8000/auth/google',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'} // application/x-www-form-urlencoded,
              })
              .then(function(res) {
                console.log(res)
              })
              .catch(function (error) {
                console.log(error)
                alert('err')
              })
          },

          //谷歌验证码
          captcha : function () {
            var s = document.getElementsByTagName('script')[document.getElementsByTagName('script').length-1]
            s.type = 'text/javascript'
            s.src = 'https://www.google.com/recaptcha/api.js'
          },
          removecaptcha: function () {
          }
        },
        mounted: function () {
          if (this.$route.query.success == 'True') {
            alert('激活成功，请重新登录')
            this.$router.push({path: '/login'})
          } else if (this.$route.query.success == 'False') {
            alert('激活链接已失效,重新登录再激活')
          }
          return
        }     
    }
</script>

<style>
.login-main {
    width: 1080px;
    height: 654px;
    margin: 0 auto;
    margin-top: 20px;

}
/* 谷歌和face跳转样式 */
.login-maintwo {
  height: 44px;
  padding: 20px 314px;
  border-bottom: 1px solid #e5e5e5;
}
.login-maintwo h2 {
  float: left;
  font-size: 12px;
  margin-top: 18px;
}
.login-maintwo a {
  display: block;
  float: left;
  font-size: 18px;
  width: 110px;
  height: 34px;
  margin-left: 20px;
  padding: 10px 0 0 20px;
  line-height: 24px;
  background: #4f95f7;
  color: white;
}
.login-maintwo a:nth-child(3) {
  width: 122px;
  background: #4467af;
}
.login-maintwo img {
  float: left;
  width: 15px;
  height: 20px;
}
.login-maintwo span {
  float: left;
  width: 21px;
  height: 21px;
  margin-right: 8px;
  padding: 2px 2px 2px 2px;
  background: white;
}
.login-main strong {
  float: left;
  display: block;
  height: 290px;
  margin-top: 20px;
  border-left: 1px solid #e5e5e5;
}
/* 登入样式 */
.sign {
  float: left;
  width: 369px;
  height: 331px;
  margin: 39px 85px 0 85px;
}
.sign h2 {
  font-size: 16px;
  margin-bottom: 20px;
  text-align: center;
}
.sign .el-input__inner {
  border-radius: 0;
}
.class .el-button {
  width: 100%;
  margin-bottom: 10px;
  border-radius: 0;
  border: 0;
  background: #e54c87;
}
.sign .el-checkbox__label {
  font-size: 12px;
}
.sign-pass {
  float: right;
  padding: 5px 0 0 0;
  font-size: 12px;
  color: black;
}
.sign-pass:hover {
  color: #e54c87;
}
.sign .el-form-item:nth-child(3) {
  margin-bottom: 0px;
}
.sign .el-checkbox__inner {
    width: 12px;
    height: 12px;
    border-radius: 0;
    border-color: #b7b7b7;
}
.sign .el-checkbox__input.is-checked .el-checkbox__inner {
  background: white;
  border-color: #b7b7b7;
}
.sign .el-checkbox__input .is-focus {
  border-color: #b7b7b7;
}
.sign .el-checkbox__inner::after {
  left: 2px;
  top: -1px;
  border-color: #e54c87;
}
/* 注册样式 */
.gister {
  float: left;
  width: 369px;
  height: 331px;
  margin: 39px 85px 0 85px;
}
.gister h2 {
  font-size: 16px;
  text-align: center;
  margin-bottom: 20px;
}
.gister .el-input__inner {
  border-radius: 0;
}
.gister .el-button {
  float: left;
  width: 369px;
  height: 36px;
  border-radius: 0;
  border: 0;
  background: #e54c87;
}
.gister p {
  font-size: 12px;
}
.gister span {
  font-weight: bold;
}
.gister em {
  font-weight: bold;
  color: #e54c87;
}
.gister .el-form demo-ruleForm {
  width: 350px;
}
.class {
  position: relative;
  top: 0;
}
.class .el-button {
  height: 36px;
}
.login-main .el-message-box {
  width: 400px;
  height: 178px;
}
.login-main .el-message-box__content {
  padding: 0;
}
.login-main .el-message-box__headerbtn {
    position: absolute;
    top: 19px;
    background: 0 0;
    border: none;
    outline: 0;
    padding: 0;
    cursor: pointer;
}
.login-main .el-icon-close ::before {
  width: 10px;
  height: 10px;
}
.login-main .el-message-box__headerbtn .el-message-box__close:hover {
  color: #F85292;
  opacity: 0.5;
}
.login-main .el-message-box .el-button--primary {
  position: relative;
  width: 90px;
  height: 26px;
  top: -54px;
  left: -29px;
  font-size: 14px;
  line-height: 0;
  border: 0;
  border-radius: 0;
  background: #F85292;
}
.login-main .el-message-box .el-input__inner {
  width: 230px;
  height: 26px;
  border-radius: 0;
}
.login-main .el-message-box {
  border-radius: 0;
}
.login-main .el-message-box .el-input {
  float: left;
  left: 31px;
}
.login-main .el-message-box__input {
  float: left;
}
.login-main .el-message-box p {
  font-size: 12px;
  margin-left: 30px;
  margin-top: 25px;
  color: #0F0F0F;
} 
.login-main .el-message-box .el-message-box__errormsg {
  float: left;
  margin-top: 10px;
  margin-left: 100px;
}
.v-modal {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    opacity: .5;
    background: rgba(0,0,0,0.2);
}
</style>