<template>
<!-- 找回密码页面 -->
  <div class="forgot">
      <div class="forgotbuy">
          <h2>{{ title }}</h2>
          <div class="forgotnew">
              <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" class="demo-ruleForm">
                    <el-form-item prop="passd">
                        <el-input :placeholder="yuan" type="password" v-model.number="ruleForm2.passd"></el-input>
                    </el-form-item>
                    <el-form-item prop="pass">
                        <el-input :placeholder="ned" type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
                    </el-form-item>
                    <el-form-item prop="checkPass">
                        <el-input :placeholder="conf" type="password" v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
                     
                     </el-form-item>
                    <el-form-item class="adada">
                        <el-button type="primary" @click="submitForm('ruleForm2')">{{ buttone }}</el-button>
                    </el-form-item>
                </el-form>
          </div>
      </div>
  </div>
</template>
<script>
import axios from 'axios'
// 执行正则表达式
export default {
    data() {
    var checkAge = (rule, value, callback) => {
        var regExp = /^[a-zA-Z][a-zA-Z0-9]{7,31}$/;
        if (value === '') {
          callback(new Error('Please enter the original password'))
        } else if (regExp.test(value) === false) {
          callback(new Error('8-16 letters and numbers can not be pure numbers or pure English'))
        } else {
          callback()
        }
      };
      var validatePass = (rule, value, callback) => {
      	var regExp = /^[a-zA-Z][a-zA-Z0-9]{7,31}$/;
        if (value === '') {
          callback(new Error('Please set up a new password'));
        } 
        if (regExp.test(value) === false) {
        	callback(new Error('8-16 letters and numbers can not be pure numbers or pure English'))
        }
        else {
          if (this.ruleForm2.checkPass !== '') {
            this.$refs.ruleForm2.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePasss = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('Confirm the new password'));
        } else if (value !== this.ruleForm2.pass) {
          callback(new Error('The password for the two time is inconsistent!'));
        } else {
          callback();
        }
      };
      return {
        title: 'RETURNS AND EXCHANGES',
        yuan: 'Old Password',
        ned: 'New Password',
        conf: 'Confim Password',
        buttone: 'SUBMlT',
        ruleForm2: {
          pass: '',
          checkPass: '',
          passd: '',
        },
        rules2: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePasss, trigger: 'blur' }
          ],
          passd: [
            { validator: checkAge, trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        var self = this
        this.$refs[formName].validate((valid) => {
          if (valid) {
            axios.post('http://192.168.0.112:8000/auth/password/change',{
              old_password: this.ruleForm2.passd,
              new_password: this.ruleForm2.checkPass,
            })
            .then(function(res){
              if (res.data.message == 'verify error') {
                alert('旧密码验证错误')
              } else if (res.data.success == false) {
                alert ('修改失败')
              } else {
                alert ('修改成功')
                self.$router.push({path: '/'})
              } 
            })
            .catch(function(err) {
              alert('请求失败')
            });
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
/* 最外层div */
    .forgot {
        width: 1080px;
        height: 100%;
        margin: 0 auto;
        margin-top: -15px;
    }
    /* 找回密码页面块 */
    .forgotbuy {
        float: right;
        width: 860px;
        height: 100%;
    }
    .forgotbuy h2 {
        width: 100%;
        height: 25px;
        font-size: 16px;
        color: #0F0F0F;
        line-height: 20px;
        border-bottom: 1px solid #b7b7b7;
    }
    /* 输入块区 */
    .forgotnew {
        width: 370px;
        margin: 0 auto;
        margin-top: 50px;
    }
    .forgotnew .el-button {
        width: 100%;
        border-radius: 0;
        border-color: #e54c87;
        background: #e54c87;
        height: 36px;
    }
    .forgotnew .el-button:active{
      border-color: #ccc;
      background: #ccc;
    }
    .forgotnew .el-input__inner {
        border-radius: 0;
    }
.el-form-item.is-error .el-input__inner, .el-form-item.is-error .el-textarea__inner {
    border-color: #E54C87;
}
.el-form-item.is-error .el-input__inner, .el-form-item.is-error .el-textarea__inner:active {
  border-color: #E54C87;
}
.el-form-item.is-error .el-input__inner, .el-form-item.is-error .el-textarea__inner {
  border-color: #E54C87;
}
</style>