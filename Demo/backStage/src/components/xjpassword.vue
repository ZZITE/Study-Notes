<template>
    <!-- 修改密码 -->
    <div class="xjpassword">
        <div class="xjpassword-main">
            <h2>{{ work }}</h2>
            <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-width="100px" class="demo-ruleForm">
                <el-form-item label="原始密码" prop="age">
                    <el-input v-model.number="ruleForm2.age"></el-input>
                </el-form-item>
                <el-form-item label="新密码" prop="pass">
                    <el-input type="password" v-model="ruleForm2.pass" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="checkPass">
                    <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <button type="primary" @click="submitForm('ruleForm2')">登入</button>
                    <!-- <el-button @click="resetForm('ruleForm2')">重置</el-button> -->
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
  export default {
    data() {
      var checkAge = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('密码不能为空'));
        }
        setTimeout(() => {
          if (!Number.isInteger(value)) {
            callback(new Error('请输入数字值'));
          } else {
            if (value < 18) {
              callback(new Error(''));
            } else {
              callback();
            }
          }
        }, 1000);
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm2.checkPass !== '') {
            this.$refs.ruleForm2.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm2.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      return {
        work: '修改密码',
        ruleForm2: {
          pass: '',
          checkPass: '',
          age: ''
        },
        rules2: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          age: [
            { validator: checkAge, trigger: 'blur' }
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
.xjpassword {
    float: left;
    width: 100%;
    height: 948px;
    background: #E5E5E5;
}
.xjpassword-main {
    width: 500px;
    height: 326px;
    margin: 0 auto;
    margin-top: 330px;
    padding: 18px 30px 0 30px;
    box-shadow: 1px 1px 5px 1px rgba(112,5,46,0.3);
    background: white;
}
.xjpassword-main h2 {
    margin-bottom: 29px;
    text-align: center;
    font-size: 16px;
    color:rgba(15,15,15,1);
}
.xjpassword-main .el-input__inner {
    border-radius: 0;
}
.xjpassword-main button {
    width: 370px;
    height: 40px;
    border: 0;
    outline:none;
    color: white;
    background:rgba(229,76,135,1);
}
.xjpassword-main button:active {
    background:rgba(229,76,135,0.9);
}
</style>
