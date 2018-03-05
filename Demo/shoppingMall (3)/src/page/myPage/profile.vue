<template>
  <div class="profile">
    <h2>Primary Information</h2>
    <div class="pr-information">
      <div class="text">
        <span class="span tt">Mobile Number</span>
        <span class="span">{{mes.Number}}</span>
      </div>
      <div class="text">
        <span class="span tt">Email Address</span><span class="span">{{mes.Email}}</span>
      </div>
      <div class="ad">
        <h2>Address Book</h2>
        <a class="addadr">Add a New Address</a>
      </div>
    </div>
    <ul class="bottom">
      <li class="botli" v-for="(item,index) in mes.addressBook" :key="index">
        <span v-for="(i,index) in item" :key="index" class="btsp">{{i}}</span>
      </li>
    </ul>
    <div class="pr-active" v-if="active">
      <span><a @click="activeclick">请先激活账户再开始购物</a></span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'profile',
  data () {
    return {
      active: null,
      mes: {
        Number: '+911368595427',
        Email: 'xiongxuanqing@yahoo.com',
        addressBook : [
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238'],
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238'],
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238'],
          ['Howard T Villarreal','2301 Oakwood CircleL','Los Angeles','Los Angeles','900172310','949-340-8238']
        ]
      }
    }
  },
  methods: {
    activeclick: function () {
      axios.get('/auth/email/active')
      .then(function (res) {
        if (res.data.email_change_warning = true) {
          alert('建议更换邮箱')
        }
        alert('已发送激活邮件')
      })
      .catch(function () {

      })
    }
  },


  created: function () {
    var self = this
    axios.get('user/profile')
    .then(function (res) {
      console.log(res)
      self.active = !res.data.is_active
    })
    .catch(function (error) {
      if (error.response.status === 403) {
        self.$router.push({path: '/login'})
      }
    })
  }
  /*function () {
    axios.get('/auth/email/active')
    .then(function (res) {
      console.log(res)
    })
    .catch(function () {
      alert('验证')
    })
  }*/
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.profile {
  width: 100%;
  margin-top:-20px;
}
.profile::after {
  content: "020"; 
  display: block; 
  height: 0; 
  clear: both; 
  visibility: hidden;
}
h2 {
  font-size: 16px;
  color: #0F0F0F;
  width: 400px;
}
.pr-information {
  margin-top: 6px;
  height: 100px;
  width: 860px;
  border-top: 1px solid #E5E5E5;
  border-bottom: 1px solid #E5E5E5;
}
.text {
  display: inline-block;
  height: 50%;
  width: 48%;
  color: #0F0F0F;
}
.span {
  margin-right: 26px;
}
.tt {
  color: #595959;
}
.ad {
  position: relative;
  width: 860px;
  margin-top: 20px;
}
.addadr {
  display: block;
  position: absolute;
  right: 0;
  top: 4px;
  font-size: 12px;
  color: #595959;
}
a:link {
  color: #595959;
}
a:visited {
  color: #595959;
}
a:hover {
  color: #E54C87 ;
  text-decoration: underline;
  text-decoration-style: solid 2px;
}
a:active {
  color: #E54C87 ;
}
.bottom {
  width: 100%;
  float: left;
  margin-top: 10px;
}
.btsp {
  margin-right: 10px;
  font-size: 14px;
  color: #0F0F0F;
}
.botli {
  margin-top: 10px;
}
.pr-active {
  margin-top: 50px;
  float: left;
  width: 860px;
  height: 30px;
  text-align: center;
}
.pr-active span a {
  font-size: 16px;
  color: #E54C87;
}
</style>
